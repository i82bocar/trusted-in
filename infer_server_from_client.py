
import os
import re
import sys
import json
from pathlib import Path
from collections import defaultdict

BINARY_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.pdf', '.ico', '.zip', '.gz', '.tar', '.db', '.sqlite', '.so', '.dll', '.exe'}
TEXT_EXTS = {'.py', '.txt', '.md', '.json', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.xml', '.html', '.js', '.ts', '.tsx', '.css', '.qrc', '.ui'}

URL_RE = re.compile(r'https?://[a-zA-Z0-9._\-:/?#%=&]+')
JWT_RE = re.compile(r'eyJ[a-zA-Z0-9_\-]{10,}\.[a-zA-Z0-9_\-]{10,}\.[a-zA-Z0-9_\-]{10,}')
AUTH_HDR_RE = re.compile(r'Authorization\s*[:=]\s*[\'\"]?(Bearer|Basic|Api[- ]?Key)[\s\'\":]+([A-Za-z0-9._\-]+)?', re.IGNORECASE)
HEADER_NAME_RE = re.compile(r'[\"\'](x-[a-z0-9\-]+)[\"\']\s*[:=]\s*', re.IGNORECASE)
GRAPHQL_RE = re.compile(r'\b(query|mutation)\s+\w+\s*\(', re.IGNORECASE)
GQL_ENDPOINT_HINT_RE = re.compile(r'/graphql(\b|/|\?)', re.IGNORECASE)
WEBSOCKET_RE = re.compile(r'wss?://[a-zA-Z0-9._\-:/?#%=&]+')

REQUESTS_IMPORT_RE = re.compile(r'\bimport\s+requests\b|\bfrom\s+requests\s+import\b')
HTTPX_IMPORT_RE = re.compile(r'\bimport\s+httpx\b|\bfrom\s+httpx\s+import\b')
AIOHTTP_IMPORT_RE = re.compile(r'\bimport\s+aiohttp\b|\bfrom\s+aiohttp\s+import\b')
QTNETWORK_IMPORT_RE = re.compile(r'QNetworkAccessManager|QNetworkRequest|QNetworkReply')
GRPC_IMPORT_RE = re.compile(r'\bimport\s+grpc\b|\bfrom\s+grpc\s+import\b')

SDK_HINTS = [
    ('supabase', re.compile(r'\bsupabase\b|\bfrom\s+supabase\s+import', re.IGNORECASE)),
    ('firebase', re.compile(r'firebase|google\\.cloud\\.firestore|firebase_admin', re.IGNORECASE)),
    ('boto3/aws', re.compile(r'\bboto3\b|\bx-amz-|s3://', re.IGNORECASE)),
    ('azure', re.compile(r'azure\.', re.IGNORECASE)),
    ('gcp', re.compile(r'google\\.cloud\.', re.IGNORECASE)),
    ('sentry', re.compile(r'sentry_sdk', re.IGNORECASE)),
    ('datadog', re.compile(r'datadog', re.IGNORECASE)),
]

PAGINATION_HINT_RE = re.compile(r'(limit|offset|page(size)?)\s*[:=]\s*')
VERSIONING_HINT_RE = re.compile(r'/v\d+(/|\b)')
HEALTH_HINT_RE = re.compile(r'/health(check)?\b|/status\b|/metrics\b')
AUTH_ENDPOINT_HINT_RE = re.compile(r'/auth(/|$)|/login|/logout|/refresh', re.IGNORECASE)

def is_text_file(path: Path):
    ext = path.suffix.lower()
    if ext in BINARY_EXTS:
        return False
    if ext in TEXT_EXTS:
        return True
    try:
        with open(path, 'rb') as f:
            chunk = f.read(2048)
        chunk.decode('utf-8')
        return True
    except Exception:
        return False

def read_text(path: Path):
    try:
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ""

def scan_repo(root: Path, max_bytes=500_000):
    findings = {
        'urls': set(),
        'websockets': set(),
        'url_contexts': [],
        'jwt_examples': set(),
        'auth_headers': set(),
        'header_names': set(),
        'graphql_presence': False,
        'graphql_endpoints': set(),
        'http_libs': set(),
        'sdk_hints': set(),
        'pagination_hints': set(),
        'versioning_paths': set(),
        'health_paths': set(),
        'auth_paths': set(),
        'configs': {},
        'reqs': {},
    }
    files_scanned = 0

    for path in root.rglob('*'):
        if not path.is_file():
            continue
        if path.stat().st_size > max_bytes:
            continue
        if not is_text_file(path):
            continue

        files_scanned += 1
        text = read_text(path)

        # URLs
        for m in URL_RE.finditer(text):
            url = m.group(0)
            findings['urls'].add(url)
            # capture small context window
            start = max(0, m.start()-80); end = m.end()+80
            ctx = text[start:end].replace('\n', ' ')
            findings['url_contexts'].append((str(path), ctx))

        # WebSocket URLs
        for m in WEBSOCKET_RE.finditer(text):
            findings['websockets'].add(m.group(0))

        # JWT
        for m in JWT_RE.finditer(text):
            findings['jwt_examples'].add(m.group(0)[:20] + '...')

        # Auth headers
        for m in AUTH_HDR_RE.finditer(text):
            findings['auth_headers'].add(m.group(0))

        # Custom headers
        for m in HEADER_NAME_RE.finditer(text):
            findings['header_names'].add(m.group(1).lower())

        # GraphQL
        if GRAPHQL_RE.search(text):
            findings['graphql_presence'] = True
        for m in GQL_ENDPOINT_HINT_RE.finditer(text):
            findings['graphql_endpoints'].add(m.group(0))

        # HTTP libs
        if REQUESTS_IMPORT_RE.search(text): findings['http_libs'].add('requests')
        if HTTPX_IMPORT_RE.search(text): findings['http_libs'].add('httpx')
        if AIOHTTP_IMPORT_RE.search(text): findings['http_libs'].add('aiohttp')
        if QTNETWORK_IMPORT_RE.search(text): findings['http_libs'].add('QtNetwork')
        if GRPC_IMPORT_RE.search(text): findings['http_libs'].add('grpc')

        # SDK hints
        for name, regex in SDK_HINTS:
            if regex.search(text):
                findings['sdk_hints'].add(name)

        # Patterns
        for m in PAGINATION_HINT_RE.finditer(text):
            findings['pagination_hints'].add(m.group(0))
        for m in VERSIONING_HINT_RE.finditer(text):
            findings['versioning_paths'].add(m.group(0))
        for m in HEALTH_HINT_RE.finditer(text):
            findings['health_paths'].add(m.group(0))
        for m in AUTH_ENDPOINT_HINT_RE.finditer(text):
            findings['auth_paths'].add(m.group(0))

        # Config files
        if path.name in ('requirements.txt', 'pyproject.toml', 'Pipfile'):
            findings['reqs'][path.name] = read_text(path)
        if path.suffix.lower() in ('.env', '.ini', '.yaml', '.yml', '.json', '.cfg'):
            rel = str(path.relative_to(root))
            if any(k in path.name.lower() for k in ('config', 'setting', 'secret', 'env')):
                findings['configs'][rel] = read_text(path)[:8000]

    # Normalize sets to sorted lists for JSON-able
    for k in list(findings.keys()):
        if isinstance(findings[k], set):
            findings[k] = sorted(findings[k])

    findings['files_scanned'] = files_scanned
    return findings

def infer_report(findings: dict):
    urls = findings.get('urls', [])
    base_domains = defaultdict(int)
    for u in urls:
        m = re.match(r'https?://([^/]+)/?', u)
        if m:
            base_domains[m.group(1)] += 1
    top_domains = sorted(base_domains.items(), key=lambda x: -x[1])

    def bullet(items, maxn=None):
        items = list(items)
        if maxn is not None:
            items = items[:maxn]
        return '\n'.join(f'- {i}' for i in items) if items else '- (none found)'

    report = []
    report.append(f"# Client-side inferred server report\n")
    report.append(f"Files scanned: **{findings.get('files_scanned',0)}**\n")

    report.append("## Detected URLs")
    report.append(bullet(urls[:30]))

    if top_domains:
        report.append("\n**Top domains:**\n" + bullet([f'{d} ({c} hits)' for d,c in top_domains[:10]]))

    if findings.get('websockets'):
        report.append("\n## WebSockets")
        report.append(bullet(findings['websockets'][:20]))

    report.append("\n## Network libraries used in client")
    report.append(bullet(findings.get('http_libs', [])))

    report.append("\n## SDK / 3rd-party clues")
    report.append(bullet(findings.get('sdk_hints', [])))

    report.append("\n## Authentication")
    report.append("Authorization header patterns:")
    report.append(bullet(findings.get('auth_headers', [])[:10]))
    if findings.get('jwt_examples'):
        report.append("\nExample tokens (truncated):")
        report.append(bullet(findings.get('jwt_examples', [])[:5]))
    report.append("\nSuspicious custom header names:")
    report.append(bullet(findings.get('header_names', [])[:20]))

    report.append("\n## API patterns")
    report.append("Versioned paths (e.g., /v1):")
    report.append(bullet(findings.get('versioning_paths', [])))
    report.append("\nPagination (limit/offset/page):")
    report.append(bullet(findings.get('pagination_hints', [])))
    report.append("\nHealth/status/metrics paths:")
    report.append(bullet(findings.get('health_paths', [])))
    report.append("\nAuth paths (login/refresh/logout):")
    report.append(bullet(findings.get('auth_paths', [])))

    report.append("\n## GraphQL")
    report.append(f"Queries/mutations detected?: **{'Yes' if findings.get('graphql_presence') else 'No'}**")
    if findings.get('graphql_endpoints'):
        report.append("Possible GraphQL endpoints in routes:")
        report.append(bullet(findings.get('graphql_endpoints', [])))

    if findings.get('configs'):
        report.append("\n## Relevant config files (trimmed)")
        for name, content in findings['configs'].items():
            report.append(f"\n### {name}\n```\n{content}\n```")

    if findings.get('reqs'):
        report.append("\n## Dependencies (excerpt)")
        for name, content in findings['reqs'].items():
            report.append(f"\n### {name}\n```\n{content[:4000]}\n```")

    report.append("\n---\n## Slide-ready summary (fill the blanks)\n")
    report.append("""- API type: {REST/GraphQL/gRPC} (from libs and endpoints).
- Base URL: {main domain}.
- Auth: {JWT/OAuth/API key} (from headers and paths).
- Versioning: {/v1, /v2} if present.
- Pagination: {limit/offset or cursor}.
- Third-party services: {Supabase/Firebase/AWS/etc.} if any.
- Observability: {health/metrics present or not}.
- Zero-knowledge?: {yes/no} - confirm if server only receives ciphertexts.
""")

    return '\n'.join(report)

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    findings = scan_repo(root)
    report_md = infer_report(findings)
    out = Path('server_architecture_inferred.md')
    out.write_text(report_md, encoding='utf-8')
    Path('server_architecture_findings.json').write_text(json.dumps(findings, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Wrote: {out.resolve()} and server_architecture_findings.json')

if __name__ == '__main__':
    main()
