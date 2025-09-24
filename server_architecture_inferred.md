# Client-side inferred server report

Files scanned: **4706**

## Detected URLs
- http://creativecommons.org/ns#
- http://purl.org/dc/dcmitype/StillImage
- http://purl.org/dc/elements/1.1/
- http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd
- http://www.inkscape.org/
- http://www.inkscape.org/namespaces/inkscape
- http://www.w3.org/1999/02/22-rdf-syntax-ns#
- http://www.w3.org/2000/svg
- https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts
- https://developer.microsoft.com/en-us/microsoft-edge/testdrive/demos/variable-fonts
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide
- https://developers.google.com/fonts/docs/android
- https://developers.google.com/fonts/docs/getting_started
- https://developers.google.com/web/fundamentals/design-and-ux/typography/variable-fonts
- https://doc.qt.io/qt-5/qframe.html#-prop
- https://doc.qt.io/qt-5/qframe.html#details
- https://doc.qt.io/qt-5/stylesheet-examples.html
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar
- https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton

**Top domains:**
- doc.qt.io (32 hits)
- github.com (15 hits)
- project.spinncode.com (4 hits)
- developers.google.com (3 hits)
- trustedin.app (3 hits)
- purl.org (2 hits)
- www.inkscape.org (2 hits)
- www.w3.org (2 hits)
- fontawesome.com (2 hits)
- stackoverflow.com (2 hits)

## Network libraries used in client
- QtNetwork
- requests

## SDK / 3rd-party clues
- boto3/aws
- datadog
- firebase
- sentry
- supabase

## Authentication
Authorization header patterns:
- (none found)

Suspicious custom header names:
- (none found)

## API patterns
Versioned paths (e.g., /v1):
- /v1
- /v2
- /v4

Pagination (limit/offset/page):
- limit = 
- limit:
- offset =
- offset = 
- offset:
- offset: 
- offset=
- page = 
- page:

Health/status/metrics paths:
- /health
- /metrics
- /status

Auth paths (login/refresh/logout):
- /Login
- /login
- /logout
- /refresh

## GraphQL
Queries/mutations detected?: **No**
Possible GraphQL endpoints in routes:
- /GraphQL
- /graphql

## Relevant config files (trimmed)

### generated-files\json\Settings.json
```
{
  "QPushButton": [
    {
      "name": "saveSettingsBtn",
      "icon": "../Qss/icons/icons/material_design/save.png"
    },
    {
      "name": "resetSettingsBtn",
      "icon": "../Qss/icons/icons/material_design/settings_backup_restore.png"
    },
    {
      "name": "resetVaultBtn",
      "icon": "../Qss/icons/icons/material_design/warning.png"
    }
  ],
  "QComboBox": [
    {
      "name": "autoLockComboBox",
      "items": [
        {
          "name": "30"
        },
        {
          "name": "1"
        },
        {
          "name": "5"
        },
        {
          "name": "10"
        },
        {
          "name": "Never"
        }
      ]
    },
    {
      "name": "comboBox_4",
      "items": [
        {
          "name": "English"
        },
        {
          "name": "Spanish"
        }
      ]
    },
    {
      "name": "encryptionComboBox",
      "items": [
        {
          "name": "AES-256"
        },
        {
          "name": "ChaCha20"
        },
        {
          "name": "PBKDF2"
        }
      ]
    },
    {
      "name": "clipboardComboBox",
      "items": [
        {
          "name": "1"
        },
        {
          "name": "5"
        },
        {
          "name": "10"
        },
        {
          "name": "30"
        },
        {
          "name": "Never"
        }
      ]
    }
  ],
  "QCustomThemeDarkLightToggle": [
    {
      "name": "CustomThemeDarkLightToggle",
      "darkThemeIcon": "../Qss/icons/icons/material_design/dark_mode.png",
      "lightThemeIcon": "../Qss/icons/icons/material_design/light_mode.png"
    }
  ]
}
```

## Dependencies (excerpt)

### requirements.txt
```
PySide6
QT-PyQt-PySide-Custom-Widgets
cryptography
requests
appdirs
fpdf2
pycryptodome
pysqlcipher3

```

---
## Slide-ready summary (fill the blanks)

- API type: {REST/GraphQL/gRPC} (from libs and endpoints).
- Base URL: {main domain}.
- Auth: {JWT/OAuth/API key} (from headers and paths).
- Versioning: {/v1, /v2} if present.
- Pagination: {limit/offset or cursor}.
- Third-party services: {Supabase/Firebase/AWS/etc.} if any.
- Observability: {health/metrics present or not}.
- Zero-knowledge?: {yes/no} - confirm if server only receives ciphertexts.
