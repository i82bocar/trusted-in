# Create a new file ReportGenerator.py
from fpdf import FPDF
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        
    def generate_report(self, report_data, output_path=None):
        """Generate PDF report from security data"""
        self.pdf.add_page()
        
        # Header
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.cell(0, 10, 'Security Audit Report', 0, 1, 'C')
        self.pdf.ln(10)
        
        # Metadata
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(0, 10, f"Generated: {datetime.fromisoformat(report_data['timestamp']).strftime('%Y-%m-%d %H:%M')}", 0, 1)
        self.pdf.cell(0, 10, f"User: {report_data['user']}", 0, 1)
        self.pdf.ln(10)
        
        # Security Score
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 10, f"Vault Health Score: {report_data['vault_score']}%", 0, 1)
        self.pdf.ln(5)
        
        # Findings Section
        self._add_findings_section(report_data['scan_results'])
        
        # Item Statistics
        self._add_statistics_section(report_data)
        
        # Save or return PDF
        if output_path:
            self.pdf.output(output_path)
            return output_path
        return self.pdf.output(dest='S')

    
    def _add_findings_section(self, scan_results):
        """Add security findings section"""
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 10, 'Security Findings', 0, 1)
        self.pdf.set_font('Arial', '', 10)
        
        findings = [
            f"Weak Passwords: {scan_results['weak_passwords']}",
            f"Reused Passwords: {scan_results['reused_passwords']}",
            f"Old Passwords: {scan_results['old_passwords']}",
            f"Breached Credentials: {scan_results['breach_count']}"
        ]
        
        for finding in findings:
            self.pdf.cell(0, 7, finding, 0, 1)
        self.pdf.ln(10)
    
    def _add_statistics_section(self, report_data):
        """Add vault statistics section"""
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 10, 'Vault Contents', 0, 1)
        self.pdf.set_font('Arial', '', 10)
        
        for item_type, count in report_data['item_stats'].items():
            self.pdf.cell(0, 7, f"{item_type}: {count}", 0, 1)
        self.pdf.ln(10)