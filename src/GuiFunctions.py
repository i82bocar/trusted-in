import os
import re
import random
import string
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
import json
import base64

from qtpy.QtCore import QSize, QTimer, QObject, QRunnable, QSettings, QThreadPool, Qt, QUrl, QDate, QDateTime, QEvent, QCoreApplication
from qtpy.QtWidgets import QApplication, QWidget, QLabel, QFrame, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QInputDialog, QFileDialog, QMessageBox, QLineEdit
from qtpy.QtGui import QPixmap, QIcon, QDesktopServices, QFont

from src.BackendWorker import BackendWorker
from src.Auth import Auth
from src.DonutChartWidget import DonutChartWidget
from src.ReportGenerator import ReportGenerator

from src.ui_NotificationModal import Ui_NotificationModal as NotificationModalForm
from src.ui_VaultForm import Ui_VaultFormComponent as VaultForm
from src.ui_VaultItemDetails import Ui_VaultItemDetailsForm as VaultItemDetailsForm
from src.ui_EditUsernameForm import Ui_EditUsernameForm as EditUsernameForm
from src.ui_EncryptionForm import Ui_EncryptionForm as EncryptionForm
from src.ui_About import Ui_AboutForm as AboutForm
from src.ui_Generator import Ui_GeneratorComponent as PasswordForm

from Custom_Widgets.QCustomQDialog import QCustomQDialog
from Custom_Widgets.QCustomVerticalSeparator import QCustomVerticalSeparator
from Custom_Widgets.QCustomModals import QCustomModals
from Custom_Widgets.QCustomTheme import QCustomTheme
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator

class GuiFunctions(QRunnable, QObject):
    def __init__(self, MainWindow):
        super().__init__()
        QObject.__init__(self) 
        self.main = MainWindow  # Store the mainwindow instance
        self.ui = MainWindow.ui  # Store the ui instance

        self.themeEngine = QCustomTheme()
        self.resources = self.themeEngine.PATH_RESOURCES

        # Initialize backend worker
        self.backendWorker = BackendWorker(self) #GuiFunctions
        # self.backendWorker.start()

        # auth
        self.auth = Auth()

        # Forms components
        self.loginForm = self.ui.loginComponentLoader.component
        self.settingsForm = self.ui.settingsComponentLoader.component
        self.generatorForm = self.ui.generatorComponentLoader.component
        self.vaultForm = self.ui.vaultComponentLoader.component
        self.userForm = self.ui.userComponentLoader.component
        self.dashboard = self.ui.dashboardComponentLoader.component
        self.securityScanForm = self.ui.securityScanComponentLoader.component 
        self.sidebar = self.ui.sideBarComponentLoader.component 
        self.rightSidebar = self.ui.rightBarComponentLoader.component 
        self.footer = self.ui.footerComponentLoader.component 


        self.loginForm.registerBtn.clicked.connect(lambda: self.registerUser())
        self.loginForm.loginBtn.clicked.connect(lambda: self.loginUser())
        self.loginForm.recoveryMailBtn.clicked.connect(lambda: self.sendRecoveryEmail())
        self.loginForm.verifyTokenBtn.clicked.connect(lambda: self.verifyToken())
        self.loginForm.resetPassBtn.clicked.connect(lambda: self.resetPassword())
        self.loginForm.forgotpassBtn.clicked.connect(lambda: self.startPasswordRecovery())

        # logout
        self.logout()
        # self.userEmail = ""
        
        self.userEmail = None
        self.resettingPassword = None

        self.settings = QSettings()

        self.loadSettings()
        self.settingsForm.saveSettingsBtn.clicked.connect(lambda: self.saveSettings())
        self.settingsForm.resetSettingsBtn.clicked.connect(lambda: self.resetSettings())
        self.settingsForm.changePasswordBtn.clicked.connect(self.handleChangePasswordRequest)
        self.settingsForm.exportVaultBtn.clicked.connect(self.exportEncryptedVault)
        self.settingsForm.resetVaultBtn.clicked.connect(self.confirmResetVault)
        self.settingsForm.syncVaultBtn.clicked.connect(self.syncVaultItems)
        self.settingsForm.importVaultBtn.clicked.connect(self.importEncryptedVault)

        self.generatorForm.lengthSlider.valueChanged.connect(self.updateLengthLabel)
        self.generatorForm.generateButton.clicked.connect(self.generatePassword)
        self.generatorForm.toggleVisibilityButton.clicked.connect(self.togglePasswordVisibility)
        self.generatorForm.copyButton.clicked.connect(self.copyPasswordToClipboard)
        self.generatorForm.addBtn.clicked.connect(self.showVaultForm)

        # Connect profile update button
        self.userForm.editUsernameBtn.clicked.connect(self.updateUsername)
        # Connect delete account button
        self.userForm.deleteAccountBtn.clicked.connect(self.deleteAccount)
        self.userForm.logoutBtn.clicked.connect(self.logout)

        # 
        self.initVaultForm()
        self.vaultForm.addBtn.clicked.connect(self.showVaultForm)
        self.vaultForm.searchInput.textChanged.connect(self.filterVaultItems)
        self.vaultForm.refreshBtn.clicked.connect(self.loadVaultItems)
        self.vaultForm.clearSearchBtn.clicked.connect(lambda: self.vaultForm.searchInput.setText(""))

        # 
        # self.loadVaultItems()
        # self.displayUserProfile()

        # 
        self.dashboard.addBtn.clicked.connect(self.showVaultForm)
        self.dashboard.notificationBtn.clicked.connect(self.rightSidebar.customSidebar.expandMenu)
        self.dashboard.quickFixBtn.clicked.connect(self.sidebar.vaultBtn.click)
        self.dashboard.breachBtn.clicked.connect(self.sidebar.vaultBtn.click)
        self.dashboard.vaultBtn.clicked.connect(self.sidebar.vaultBtn.click)
        self.dashboard.updatePassBtn.clicked.connect(self.sidebar.vaultBtn.click)
        self.dashboard.viewpassBtn.clicked.connect(self.sidebar.vaultBtn.click)
        self.dashboard.viewWeakPass.clicked.connect(self.sidebar.vaultBtn.click)
        self.dashboard.generatorBtn.clicked.connect(self.sidebar.generatorBtn.click)
        self.dashboard.settingsBtn.clicked.connect(self.sidebar.settingsBtn.click)
        self.dashboard.userBtn.clicked.connect(self.sidebar.userBtn.click)

        # 
        self.securityScanForm.securityScanBtn.clicked.connect(self.startSecurityScan)
        self.donutChartWidget = DonutChartWidget()
        self.securityScanForm.donutChartContainer.layout().addWidget(self.donutChartWidget)
        self.securityScanForm.addBtn.clicked.connect(self.showVaultForm)
        self.securityScanForm.generateReportBtn.clicked.connect(self.generateSecurityReport)

        # 
        self.rightSidebar.clearBtn.clicked.connect(self.clearSidebarNotifications)

        # # Add this after initializing backend worker
        self.password_stats = {
            'weak_passwords': [],
            'reused_passwords': [],
            'old_passwords': []
        }

        self.inactivity_timer = QTimer()
        self.inactivity_timer.timeout.connect(self.handleInactivityTimeout)
        self.startActivityTracking()

        self.clipboard_timer = QTimer()
        self.clipboard_timer.timeout.connect(self.clearClipboard)
        self.updateClipboardStatus()

        self.app = QCoreApplication.instance()
        if self.app is None:
            self.app = QCoreApplication([])

        self.app.aboutToQuit.connect(self.handleAppQuit)

        self.sidebar.aboutBtn.clicked.connect(self.showAboutForm)
            
    def isValidEmail(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def registerUser(self):
        self.resettingPassword = False
        firstName = self.loginForm.firstNameInput.text().strip()
        lastName = self.loginForm.lastNameInput.text().strip()
        email = self.loginForm.emailInput.text().strip()
        password = self.loginForm.passwordInput.text().strip()
        confirmPassword = self.loginForm.confirmPasswordInput.text().strip()
        agreed = self.loginForm.agreeCheckbox.isChecked()

        if not firstName or not lastName:
            self.showMessageModal("Missing Fields", "First and last name are required.", type="warning", duration=2000)
            return

        if not email or not password:
            self.showMessageModal("Missing Fields", "Email and password are required.", type="warning", duration=2000)
            return

        if not self.auth.isValidEmail(email):
            self.showMessageModal("Invalid Email", "Please enter a valid email address.", type="warning", duration=2000)
            return

        if password != confirmPassword:
            self.showMessageModal("Mismatch", "Passwords do not match.", type="warning", duration=2000)
            return

        if len(password) < 8:
            self.showMessageModal("Weak Password", "Password must be at least 8 characters long.", type="warning", duration=2000)
            return

        if not agreed:
            self.showMessageModal("Terms Not Accepted", "You must agree to the terms and conditions.", type="warning", duration=2000)
            return

        self.userEmail = email

        self.backendWorker.registerUserWorker(
            firstName, lastName, email, self.auth.hashPassword(password)
        )

    
    def loginUser(self):
        self.resettingPassword = False
        email = self.loginForm.loginEmail.text().strip()
        password = self.loginForm.loginPassword.text().strip()

        if not email or not password:
            self.showMessageModal("Missing Fields", "Email and password are required.", type="warning", duration=2000)
            return

        if not self.auth.isValidEmail(email):
            self.showMessageModal("Invalid Email", "Please enter a valid email address.", type="warning", duration=2000)
            return

        self.backendWorker.loginUserWorker(email, self.auth.hashPassword(password))
        self.userEmail = email
    
    def handleLoginSuccessful(self, message):
        self.showMessageModal("Login Successful", "Successfully logged in. Welcome!", duration=5000)

        # Move on to the next step
        # verify email
        self.sendRecoveryEmail()    
        
    def handleLoginFailed(self, error_message):
        self.showMessageModal("Login Error", f"Login failed: {error_message}",  type="warning", duration=2000)
    
    def handleUserUploadFinished(self, response):
        if response.get("success"):
            self.showMessageModal(
                "User Uploaded",
                "User details uploaded successfully.",
                type="info",
                duration=5000
            )
        else:
            error_msg = (
                response.get("upload_user_response") or
                response.get("error") or
                "Unknown error occurred during user upload."
            )
            self.showMessageModal(
                "Upload Failed",
                f"Failed to upload user details: {error_msg}",
                type="warning",
                duration=5000
            )

    def startPasswordRecovery(self):
        self.showMessageModal(
            title="Reset Password!!",
            description=(
                "<b>⚠️ DESTRUCTIVE ACTION!</b><br><br>"
                "This will <b>permanently delete ALL</b> items in your vault:<br>"
                "- All passwords<br>"
                "- All secure notes<br>"
                "- All payment cards<br>"
                "- All contacts<br><br>"
                "<b>⚠️ Sync your items first to upload them before changing your local password!</b><br><br>"
                "This cannot be undone!"
            ),
            type="warning",
            okayText="Got it!",
            cancelBtnType="default",
            duration=-1 
        )
        self.resettingPassword = True

    def sendRecoveryEmail(self):
        if self.resettingPassword:
            email = self.loginForm.recoveryMail.text().strip()
            self.userEmail = email
        else:
            email = self.userEmail

        if not email and not self.userEmail:
            self.showMessageModal("Missing Fields", "Email is required.", type="warning", duration=2000)
            return

        if not self.auth.isValidEmail(email):
            self.showMessageModal("Invalid Email", "Please enter a valid email address.", type="warning", duration=2000)
            return

        self.showMessageModal("Email Verification", "Requesting email verification token, please wait.", duration=2000, loading=True)

        # self.backendWorker.sendRecoveryEmail(email)
        self.backendWorker.resendVerificationEmailWorker(email)
    
    def handleResendVerificationEmailFinished(self, response):
        if response.get("success"):
            self.showMessageModal("Email Sent", f"Verification email sent successfully to {self.userEmail}.", type="info", duration=5000)
            
        else:
            error_msg = response.get("resend_verification_email_response") or response.get("error") or "Unknown error"
            self.showMessageModal("Error", f"Use the default pin to login. Failed to resend verification email: {error_msg}", type="warning", duration=5000)

        self.loginForm.accountPages.setCurrentWidget(self.loginForm.passwordTokenPage)

    def handleVerifyEmailFinished(self, response):
        if response.get("success"):
            self.showMessageModal("Email Verified", "Your email has been verified successfully.", type="info", duration=5000)
            if not self.resettingPassword:
                # e.g. move UI to next step or login page
                self.goToMainContent()
            else:
                # reset password
                self.loginForm.accountPages.setCurrentWidget(self.loginForm.resetPasswordPage)
        else:
            error_msg = response.get("verify_email_response") or response.get("error") or "Unknown error"
            self.showMessageModal("Verification Failed", f"Failed to verify email: {error_msg}", type="warning", duration=5000)


    def verifyToken(self):
        token = self.loginForm.mailToken.text().strip()
        email = self.userEmail

        if not token:
            self.showMessageModal("Missing Fields", "Token is required.", type="warning", duration=2000)
            return

        if token == "123456":
            # Use default pin for testing
            self.showMessageModal("Default Pin", "Using default pin to login.", type="info", duration=2000)
            self.handleVerifyEmailFinished({
                "success": True,
                "verify_email_response": "Default pin used for testing."
            })
        else:            # Validate token format (e.g. length, characters)
            if not self.backendWorker.isValidToken(token):
                self.showMessageModal("Invalid Token", "Please enter a valid token sent to your email address.", type="warning", duration=2000)
                return

            self.showMessageModal("Email Verification", "Sending your verification token.", duration=2000, loading=True)

            self.backendWorker.verifyEmailWorker(email, token)
    
    def resetPassword(self):
        password = self.loginForm.newPassword.text().strip()
        confirmPassword = self.loginForm.confirmNewPassword.text().strip()
        email = self.loginForm.recoveryMail.text().strip()

        if not password:
            self.showMessageModal("Missing Fields", "Both passwords are required.", type="warning", duration=2000)
            return

        if password != confirmPassword:
            self.showMessageModal("Mismatch", "Passwords do not match.", type="warning", duration=2000)
            return

        if len(password) < 8:
            self.showMessageModal("Weak Password", "Password must be at least 8 characters long.", type="warning", duration=2000)
            return
        
        # Update password
        self.backendWorker.updatePasswordWorker(email, self.auth.hashPassword(password))

    def handlePasswordUpdateSuccess(self, message):
        self.showMessageModal("Password updated Successful", message, duration=5000)

        # Move on to the next step     
        self.logout()

    def handlePasswordUpdateFailed(self, error_message):
        self.showMessageModal("Error updating password", f"Error: {error_message}",  type="warning", duration=2000)
    
    def goToMainContent(self):
        self.resettingPassword = False
        self.ui.mainBodyPages.setCurrentWidget(self.ui.contentPage)

        # 
        self.backendWorker.uploadUserDetailsWorker(self.userEmail)

        # 
        self.loadSettings()

        # 
        self.displayUserProfile()

        # Initialize settings
        settings = QSettings()
        
        # Set defaults if they don't exist
        if not settings.contains(f"{self.userEmail}/backup/last_backup"):
            settings.setValue(f"{self.userEmail}/backup/last_backup", "Never")
       
        
        # Initial update
        self.updateStatusDisplay()
        self.startActivityTracking()
        self.loadVaultItems()

    def showEncryptionDialog(self, parent=None):
        """Shows encryption method selection dialog and returns the chosen method"""
        # Create custom dialog
        if not hasattr(self, "encryptionDialog"):
            self.encryptionDialog = QCustomQDialog(
                parent=self.main,
                frameless=True,
                windowMovable=True,
                showForm=EncryptionForm(),
                setModal=True,
                showYesButton=False,
                showCancelButton=False
            )
            
            # Store the selected method
            form = self.encryptionDialog.shownForm
            form.saveBtn.clicked.connect(lambda: self.saveEncryptionMethod(self.encryptionDialog))
        self.encryptionDialog.show()
        self.encryptionDialog.update()

    def ensureEncryptionMethod(self):
        """Ensures an encryption method is set, prompts if not"""
        settings = QSettings()
        currentMethod = settings.value(f"{self.userEmail}/security/encryption")
        if not currentMethod or currentMethod == "None" or currentMethod == "":
            if self.userEmail is not None:
                self.showEncryptionDialog()
    
    def saveEncryptionMethod(self, dialog):
        form = dialog.shownForm
        selectedMethod = form.encryptionCombo.currentText()
        if selectedMethod == "None":
            self.showMessageModal(
                "Security Warning",
                "Storing data without encryption is extremely insecure!",
                type="warning",
                duration=3000,
                parent=dialog
            )
        else:
            self.settings.setValue(f"{self.userEmail}/security/encryption", selectedMethod)
            self.updateStatusDisplay()
            dialog.close()
    
    def logout(self):
        """Log out the current user"""
        self.resettingPassword = False
        self.userEmail = None
        try:
            self.inactivity_timer.stop()
        except:
            pass
        self.ui.mainBodyPages.setCurrentWidget(self.ui.welcomePage)

    def showMessageModal(self, title, description, position='top-right', duration=-1, parent = None, okayText=None, cancelText=None, okayAction=None, cancelAction=None, type="warning", okayBtnType=None, cancelBtnType=None, loading=False):
        if not parent:
            parent = self.main
        
        modal = QCustomModals.CustomModal(
            showForm=NotificationModalForm(),
            parent=parent,
            position=position,
            duration=duration,
            isClosable=False
        )

        modal.shownForm.header.setText(title)
        modal.shownForm.body.setText(description)

        if okayText:
            modal.shownForm.okayBtn.setText(okayText)
        else:
            modal.shownForm.okayBtn.hide()

        if cancelText:
            modal.shownForm.cancelBtn.setText(cancelText)
        else:
            modal.shownForm.cancelBtn.hide()

        if not okayText and not cancelText:
            modal.shownForm.footer.hide()
        
        if not loading:
            modal.shownForm.loadingProgressBar.hide()

        # connect button actions
        if not okayAction:
            modal.shownForm.okayBtn.clicked.connect(modal.close)
        else:
            modal.shownForm.okayBtn.clicked.connect(lambda: (modal.close(), okayAction()))

        if not cancelAction:
            modal.shownForm.cancelBtn.clicked.connect(modal.close)
        else:
            modal.shownForm.cancelBtn.clicked.connect(lambda: (modal.close(), cancelAction()))


        # Show the modal
        modal.show()

        if type == "info":
            modal.shownForm.notifIcon.setProperty("type", "info")

        if okayBtnType == "warning":
            modal.shownForm.okayBtn.setProperty("type", "warning")

        if cancelBtnType == "warning":
            modal.shownForm.cancelBtn.setProperty("type", "warning")

        modal.shownForm.notifIcon.style().unpolish(modal.shownForm.notifIcon) 
        modal.shownForm.notifIcon.style().polish(modal.shownForm.notifIcon)

        modal.shownForm.okayBtn.style().unpolish(modal.shownForm.okayBtn) 
        modal.shownForm.okayBtn.style().polish(modal.shownForm.okayBtn)

        modal.shownForm.cancelBtn.style().unpolish(modal.shownForm.cancelBtn) 
        modal.shownForm.cancelBtn.style().polish(modal.shownForm.cancelBtn)

        self.addNotificationToSidebar(title, description)
    
    def addNotificationToSidebar(self, title: str, message: str):
        """Add a notification to the right sidebar notification list."""
        container = self.rightSidebar.notificationsContainer
        layout = container.layout()

        # Notification wrapper
        notif_widget = QWidget()
        notif_layout = QVBoxLayout(notif_widget)
        notif_layout.setContentsMargins(8, 8, 8, 8)
        notif_layout.setSpacing(4)

        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 10, QFont.Bold))

        separator_1 = QCustomHorizontalSeparator()
        separator_2 = QCustomHorizontalSeparator()

        # Message
        message_label = QLabel(message)
        message_label.setWordWrap(True)

        # Timestamp
        timestamp_label = QLabel(QDateTime.currentDateTime().toString("MMM dd, hh:mm AP"))
        timestamp_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Add to layout
        notif_layout.addWidget(title_label)
        notif_layout.addWidget(separator_1)
        notif_layout.addWidget(message_label)
        notif_layout.addWidget(separator_2)
        notif_layout.addWidget(timestamp_label)

        # Insert above the spacer
        layout.insertWidget(layout.count() - 1, notif_widget)

    def clearSidebarNotifications(self):
        layout = self.rightSidebar.notificationsContainer.layout()
        # Remove all widgets except spacer
        for i in reversed(range(layout.count() - 1)):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.deleteLater()


    def saveSettings(self):
        sf = self.settingsForm

        # General
        self.settings.setValue(f"{self.userEmail}/general/autoLockTimer", sf.autoLockComboBox.currentText())
        self.settings.setValue(f"{self.userEmail}/general/breachAlerts", sf.breachAlertSwitch.isChecked())
        self.settings.setValue(f"{self.userEmail}/general/clipboardExpirationNotifications", sf.clipboardNotifySwitch.isChecked())

        # Vault
        self.settings.setValue(f"{self.userEmail}/vault/encryptionMethod", sf.encryptionComboBox.currentText())

        # Clipboard
        self.settings.setValue(f"{self.userEmail}/clipboard/expirationTime", sf.clipboardComboBox.currentText())
        self.settings.setValue(f"{self.userEmail}/clipboard/clearOnClose", sf.clearClipboardSwitch.isChecked())

        self.showMessageModal("App Settings", "Settings saved successfully", duration=2000)


    def loadSettings(self):
        self.ensureEncryptionMethod()
        sf = self.settingsForm

        # General
        value = str(self.settings.value(f"{self.userEmail}/general/autoLockTimer", "1"))
        index = sf.autoLockComboBox.findText(value)
        if index != -1:
            sf.autoLockComboBox.setCurrentIndex(index)

        sf.breachAlertSwitch.setChecked(self.settings.value(f"{self.userEmail}/general/breachAlerts", False, bool))
        sf.clipboardNotifySwitch.setChecked(self.settings.value(f"{self.userEmail}/general/clipboardExpirationNotifications", False, bool))

        # Vault
        encryption = self.settings.value(f"{self.userEmail}/vault/encryptionMethod", "AES-256")
        index = sf.encryptionComboBox.findText(encryption)
        if index != -1:
            sf.encryptionComboBox.setCurrentIndex(index)

        # Clipboard
        expirationValue = str(self.settings.value(f"{self.userEmail}/clipboard/expirationTime", "1"))
        index = sf.clipboardComboBox.findText(expirationValue)
        if index != -1:
            sf.clipboardComboBox.setCurrentIndex(index)

        sf.clearClipboardSwitch.setChecked(self.settings.value(f"{self.userEmail}/clipboard/clearOnClose", False, bool))

        self.updateStatusDisplay()


    def resetSettings(self):
        self.settings.clear()
        self.loadSettings()
        self.showMessageModal("App Settings", "Settings have been reset", type="warning", duration=2000)
    
    def updateSetting(self, key: str, value):
        self.settings.setValue(key, value)

    # 
    def generatePassword(self, sf=None):
        if sf is None:
            sf = self.generatorForm 

        length = sf.lengthSlider.value()

        useUpper = sf.includeUppercaseSwitch.isChecked()
        useLower = sf.includeLowercaseSwitch.isChecked()
        useNumbers = sf.includeNumbersSwitch.isChecked()
        useSymbols = sf.includeSymbolsSwitch.isChecked()

        characters = ""
        if useUpper:
            characters += string.ascii_uppercase
        if useLower:
            characters += string.ascii_lowercase
        if useNumbers:
            characters += string.digits
        if useSymbols:
            characters += string.punctuation

        if not characters:
            self.showMessageModal("Password Generator", "Please select at least one character set.", type="warning", duration=2000)
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        sf.generatedPasswordLineEdit.setText(password)

    def togglePasswordVisibility(self, lineEdit = None, btn = None, sf = None):
        if not lineEdit and not btn:
            if sf is None:
                sf = self.generatorForm
            lineEdit = sf.generatedPasswordLineEdit
            btn = sf.toggleVisibilityButton

        echoMode = lineEdit.echoMode()
        if echoMode == lineEdit.EchoMode.Password:
            lineEdit.setEchoMode(lineEdit.EchoMode.Normal)
            btn.setText("Hide")
        else:
            lineEdit.setEchoMode(lineEdit.EchoMode.Password)
            btn.setText("Show")
    
    def copyPasswordToClipboard(self, sf=None, showMessage=True):
        if sf is None:
            sf = self.generatorForm
        clipboard = sf.generatedPasswordLineEdit.text()
        if clipboard:
            QApplication.clipboard().setText(clipboard)
            if showMessage:
                self.showMessageModal("Password Generator", "Password copied successifully.", duration=2000)

    def updateLengthLabel(self, value, sf=None):
        if sf is None:
            sf = self.generatorForm
        sf.lengthLabel.setText(f"Length: {value}")

    # 
    def initVaultForm(self):
        # Initialize a custom dialog for the vault form
        self.vaultFormDialog = QCustomQDialog(
            parent=self.main,
            frameless = True,
            windowMovable = False,
            showForm = VaultForm(),
            setModal = True,
            showYesButton = False,
            showCancelButton = False,
        )

        form = self.vaultFormDialog.shownForm

         # Close dialog on cancel
        form.cancelButton.clicked.connect(self.vaultFormDialog.close)

        # Save button logic
        form.saveButton.clicked.connect(self.saveVaultItem)
        # form.generatePasswordBtn.clicked.connect(lambda: (self.ui.contentPages.setCurrentWidget(self.ui.generatorPage), self.vaultFormDialog.close()))
        form.generatePasswordBtn.clicked.connect(lambda: self.showGeneratorForm())
        form.showPasswordBtn.clicked.connect(lambda: self.togglePasswordVisibility(lineEdit = form.passwordLineEdit, btn = form.showPasswordBtn))
        # Switch stacked widget page based on item type
        form.itemTypeComboBox.currentIndexChanged.connect(
            lambda index: form.vaultStackedWidget.setCurrentIndex(index)
        )

        form.itemTypeComboBox.setCurrentIndex(0)
        form.vaultStackedWidget.setCurrentIndex(0)

    def showVaultForm(self):
        # close self.generatorFormDialog
        try:
            self.generatorFormDialog.close()
        except:
            pass

        try:
            self.vaultFormDialog.show()
        except:
            self.initVaultForm()
            self.vaultFormDialog.show()
    
    def initGeneratorForm(self):
        # Initialize a custom dialog for the generator form
        self.generatorFormDialog = QCustomQDialog(
            parent=self.main,
            frameless = True,
            windowMovable = False,
            showForm = PasswordForm(),
            setModal = True,
            showYesButton = False,
            showCancelButton = False,
        )

        form = self.generatorFormDialog.shownForm

        form.lengthSlider.valueChanged.connect(lambda value: self.updateLengthLabel(value, sf=form))
        form.generateButton.clicked.connect(lambda: self.generatePassword(sf=form))
        form.toggleVisibilityButton.clicked.connect(lambda: self.togglePasswordVisibility(lineEdit=form.passwordLineEdit, btn=form.toggleVisibilityButton, sf=form))
        # Copy password to clipboard and also fill the password field in the vault form
        form.copyButton.clicked.connect(lambda: (self.copyPasswordToClipboard(sf=form, showMessage=False), 
                                                # Hide generator form if shown
                                                self.generatorFormDialog.close() if self.generatorFormDialog.isVisible() else None,
                                                # Show the vault form dialog if not already shown
                                                self.showVaultForm(),
                                                self.vaultFormDialog.shownForm.passwordLineEdit.setText(form.generatedPasswordLineEdit.text()),
                                                self.vaultFormDialog.shownForm.passwordLineEdit.setFocus(),
                                                 ))
        form.addBtn.clicked.connect(self.showVaultForm)
    
    def showGeneratorForm(self):
        # close self.vaultFormDialog
        try:
            self.vaultFormDialog.close()
        except:
            pass
        # Show the generator form dialog
        try:
            self.generatorFormDialog.show()
        except:
            self.initGeneratorForm()
            self.generatorFormDialog.show()

    def getVaultItemData(self):
        self.ensureEncryptionMethod()
        form = self.vaultFormDialog.shownForm
        data = {}

        itemType = form.itemTypeComboBox.currentText()
        data["type"] = itemType
        data["name"] = form.itemNameLineEdit.text()
        data["notes"] = form.notesPlainTextEdit.toPlainText()

        if itemType == "Passwords":
            data["site"] = form.siteNameLineEdit.text()
            data["username"] = form.usernameLineEdit.text()
            data["password"] = form.passwordLineEdit.text()
        elif itemType == "Notes":
            data["title"] = form.noteTitleLineEdit.text()
            data["body"] = form.noteBodyPlainTextEdit.toPlainText()
        elif itemType == "Payment Cards":
            data["number"] = form.cardNumberLineEdit.text()
            data["expiry"] = form.expiryDateEdit.text()
            data["cvv"] = form.cvvLineEdit.text()
            data["holder"] = form.cardHolderLineEdit.text()
            data["address"] = form.billingAddressLineEdit.text()
        elif itemType == "Contacts":
            data["contactName"] = form.contactNameLineEdit.text()
            data["contactEmail"] = form.contactEmailLineEdit.text()
            data["contactPhone"] = form.contactPhoneLineEdit.text()

        return data

    def saveVaultItem(self):
        data = self.getVaultItemData()

        # === Common validation ===
        if not data["name"]:
            self.showMessageModal("Missing Field", "Item Name is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
            return

        if data["type"] == "Password":
            if not data["username"]:
                self.showMessageModal("Missing Field", "Username/Email is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            if not data["password"]:
                self.showMessageModal("Missing Field", "Password is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return

        elif data["type"] == "Note":
            if not data["title"]:
                self.showMessageModal("Missing Field", "Note title is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            if not data["body"]:
                self.showMessageModal("Missing Field", "Note content is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return

        elif data["type"] == "Payment Card":
            if not data["number"]:
                self.showMessageModal("Missing Field", "Card number is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            if not data["expiry"]:
                self.showMessageModal("Missing Field", "Card expiry is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            if not data["cvv"]:
                self.showMessageModal("Missing Field", "Card CVV is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            if not data["holder"]:
                self.showMessageModal("Missing Field", "Card holder name is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return

        elif data["type"] == "Contact":
            if not data["contactName"]:
                self.showMessageModal("Missing Field", "Contact name is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            if not data["contactEmail"]:
                self.showMessageModal("Missing Field", "Contact email is required.", type="warning", duration=2000, parent=self.vaultFormDialog)
                return
            # Optional: validate email format, phone format etc.

        # === Save logic ===
        try:
            if not self.userEmail:
                raise Exception("No user logged in")
                
            if hasattr(self, 'editingVaultItemId') and self.editingVaultItemId:
                # Call update method for existing item
                self.backendWorker.updateVaultItemWorker(
                    self.editingVaultItemId, 
                    self.userEmail, 
                    data
                )
            else:
                # Call create method for new item
                self.backendWorker.saveVaultItemWorker(self.userEmail, data)
                
            # Reset the form after successful save
            self.resetVaultForm()
            
            # Clear editing state
            if hasattr(self, 'editingVaultItemId'):
                del self.editingVaultItemId

        except Exception as e:
            self.showMessageModal("Error updating item", f"Error: {str(e)}", type="warning", duration=3000, parent=self.vaultFormDialog)

    def resetVaultForm(self):
        """Reset all fields in the vault form to their default state"""
        if hasattr(self, 'vaultFormDialog'):
            form = self.vaultFormDialog.shownForm
            
            # Reset common fields
            form.itemNameLineEdit.clear()
            form.notesPlainTextEdit.clear()
            
            # Reset password fields
            form.siteNameLineEdit.clear()
            form.usernameLineEdit.clear()
            form.passwordLineEdit.clear()
            
            # Reset note fields
            form.noteTitleLineEdit.clear()
            form.noteBodyPlainTextEdit.clear()
            
            # Reset payment card fields
            form.cardNumberLineEdit.clear()
            form.expiryDateEdit.setDate(QDate.currentDate())
            form.cvvLineEdit.clear()
            form.cardHolderLineEdit.clear()
            form.billingAddressLineEdit.clear()
            
            # Reset contact fields
            form.contactNameLineEdit.clear()
            form.contactEmailLineEdit.clear()
            form.contactPhoneLineEdit.clear()
            
            # Reset to first tab
            form.itemTypeComboBox.setCurrentIndex(0)

    # Add new handler methods
    def handleVaultItemSaved(self, result):
        """Handle successful vault item save"""
        self.vaultFormDialog.close()
        self.showMessageModal("Success", "Vault item saved successfully.", type="success", duration=2500)
        # You might want to refresh the vault table here
        self.loadVaultItems()
        self.resetVaultForm() 

    def handleVaultItemError(self, error_msg):
        """Handle vault item save error"""
        self.showMessageModal("Error saving item", 
                            f"Could not save vault item: {error_msg}", 
                            type="warning", 
                            duration=3000, 
                            parent=self.vaultFormDialog)
    
    def loadVaultItems(self):
        """Trigger loading of vault items"""
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning", duration=2000)
            return
        
        # Get password stats first
        self.backendWorker.getPasswordStatsWorker(self.userEmail)
        self.backendWorker.loadVaultItemsWorker(self.userEmail)

        # 
        self.backendWorker.scanVaultSecurityWorker(self.userEmail)
        self.backendWorker.loadVaultItemStatsWorker(self.userEmail)
    
    def handleVaultItemsLoaded(self, items: list):
        """Handle loaded vault items"""
        self.vault_items = items  # Store items for later use
        if not items:
            print("[INFO] No vault items found")
            return
            
        print(f"[INFO] Loaded {len(items)} vault items")   
        self.populateVaultTabs(items)
    
    def handlePasswordStatsResult(self, stats):
        """Store password statistics for use in vault display"""
        self.password_stats = stats
        # Trigger vault refresh if needed
        if hasattr(self, 'vault_items'):
            self.populateVaultTabs(self.vault_items)
    
    def populateVaultTabs(self, items: list):
        """Populate vault tabs with items, organized by type (layout version)"""
        vf = self.vaultForm
        # Clear all tabs first by removing all widgets
        self.clearLayout(vf.passwordList.layout())
        self.clearLayout(vf.notesList.layout())
        self.clearLayout(vf.paymentCardsList.layout())
        self.clearLayout(vf.contactsList.layout())
        
        # Add stretch to push items to top
        vf.passwordList.layout().addStretch()
        vf.notesList.layout().addStretch()
        vf.paymentCardsList.layout().addStretch()
        vf.contactsList.layout().addStretch()
        
        # Organize items by type
        for item in items:
            try:
                # Add to appropriate tab's layout (inserting before the stretch)
                if item['type'] == 'Passwords':
                    # Create the widget for this item
                    widget = self.createVaultItemWidget(item, vf.passwordList)
                    layout = vf.passwordList.layout()
                    layout.insertWidget(layout.count() - 1, widget)
                elif item['type'] == 'Notes':
                    widget = self.createVaultItemWidget(item, vf.notesList)
                    layout = vf.notesList.layout()
                    layout.insertWidget(layout.count() - 1, widget)
                    
                elif item['type'] == 'Payment Cards':
                    widget = self.createVaultItemWidget(item, vf.paymentCardsList)
                    layout = vf.paymentCardsList.layout()
                    layout.insertWidget(layout.count() - 1, widget)
                    
                elif item['type'] == 'Contacts':
                    widget = self.createVaultItemWidget(item, vf.contactsList)
                    layout = vf.contactsList.layout()
                    layout.insertWidget(layout.count() - 1, widget)
                    
                # Connect signals for action buttons
                for child in widget.findChildren(QPushButton):
                    if child.toolTip() == "View item details":
                        child.clicked.connect(lambda _, i=item: self.viewVaultItem(i))
                    elif child.toolTip() == "Edit item":
                        child.clicked.connect(lambda _, i=item: self.editVaultItem(i))
                    elif child.toolTip() == "Delete item":
                        child.clicked.connect(lambda _, i=item: self.deleteVaultItem(i))

            except Exception as e:
                print(f"Error processing vault item {item.get('id', 'unknown')}: {e}")

    def viewVaultItem(self, item_data):
        """Show detailed view of a vault item using QStackedWidget"""
        # Create dialog
        details_dialog = QCustomQDialog(
            parent=self.main,
            frameless=True,
            windowMovable=True,
            showForm=VaultItemDetailsForm(),
            setModal=True,
            showYesButton=False,
            showCancelButton=False
        )

        form = details_dialog.shownForm
        data = item_data.get('data', {})
        item_type = item_data['type'].lower()
        # Set basic info that appears on all tabs
        form.itemNameLabel.setText(item_data.get('name', 'Untitled'))
        form.itemNotesTextEdit.setPlainText(data.get('notes', ''))
        form.itemTypeLabel.setText(item_data['type'])
        form.itemDetailsPages.setCurrentIndex(0)
        # Set the appropriate page in the stacked widget
        if item_type == 'passwords':
            form.itemDetailsPages.setCurrentWidget(form.passwordPage)
            
            # Populate password fields
            form.siteValueLabel.setText(data.get('site', 'Not specified'))
            form.usernameValueLabel.setText("••••••••")
            form.passwordValueLabel.setText("••••••••") 
            
            # open site 
            if self.isValidUrl(data.get('site', '')):
                form.openSiteBtn.clicked.connect(lambda: self.openLink(data.get('site', '')))

            # Toggle password visibility
            form.showPasswordBtn.clicked.connect(lambda: self.toggleCvvVisibility(
                label=form.passwordValueLabel,
                btn=form.showPasswordBtn,
                cvv=data.get('password', '')
            ))
            form.showUsernameBtn.clicked.connect(lambda: self.toggleCvvVisibility(
                label=form.usernameValueLabel,
                btn=form.showUsernameBtn,
                cvv=data.get('username', '')
            ))

            # Copy buttons
            form.copySiteBtn.clicked.connect(lambda: self.copyToClipboard(data.get('site', '')))
            form.copyUsernameBtn.clicked.connect(lambda: self.copyToClipboard(data.get('username', '')))
            form.copyPasswordBtn.clicked.connect(lambda: self.copyToClipboard(data.get('password', '')))
            
        elif item_type == 'notes':
            form.itemDetailsPages.setCurrentWidget(form.notePage)
            form.noteTitleLabel.setText(data.get('title', 'Untitled Note'))
            form.noteContentTextEdit.setPlainText(data.get('body', ''))
            
        elif item_type == 'payment cards':
            form.itemDetailsPages.setCurrentWidget(form.paymentCardPage)
            
            # Populate card fields
            form.cardNumberValueLabel.setText(data.get('number', 'Not specified'))
            form.cardExpiryValueLabel.setText(data.get('expiry', 'Not specified'))
            form.cardHolderValueLabel.setText(data.get('holder', 'Not specified'))
            
            # Mask CVV by default
            form.cardCvvValueLabel.setText("•••")
            form.showCvvBtn.clicked.connect(lambda: self.toggleCvvVisibility(
                label=form.cardCvvValueLabel,
                btn=form.showCvvBtn,
                cvv=data.get('cvv', '')
            ))
            
            # Copy buttons
            form.copyCvvBtn.clicked.connect(lambda: self.copyToClipboard(data.get('cvv', '')))
            form.copyCardNumberBtn.clicked.connect(lambda: self.copyToClipboard(data.get('number', '')))
            form.copyExpiryBtn.clicked.connect(lambda: self.copyToClipboard(data.get('expiry', '')))
            form.copyHolderBtn.clicked.connect(lambda: self.copyToClipboard(data.get('holder', '')))
            
        elif item_type == 'contacts':
            form.itemDetailsPages.setCurrentWidget(form.contactPage)
            
            # Populate contact fields
            form.contactNameValueLabel.setText(data.get('contactName', 'Not specified'))
            form.contactEmailValueLabel.setText(data.get('contactEmail', 'Not specified'))
            form.contactPhoneValueLabel.setText(data.get('contactPhone', 'Not specified'))
            
            # Copy buttons
            form.copyNameBtn.clicked.connect(lambda: self.copyToClipboard(data.get('contactName', '')))
            form.copyEmailBtn.clicked.connect(lambda: self.copyToClipboard(data.get('contactEmail', '')))
            form.copyPhoneBtn.clicked.connect(lambda: self.copyToClipboard(data.get('contactPhone', '')))
        
        # Connect close button
        form.closeBtn.clicked.connect(details_dialog.close)
        details_dialog.show()
    
    def filterVaultItems(self, query: str):
        """Filter vault items across all tabs based on search query - searches ALL fields including comments"""
        query = query.lower().strip()

        # Loop through each vault tab's layout
        layouts = [
            self.vaultForm.passwordList.layout(),
            self.vaultForm.notesList.layout(),
            self.vaultForm.paymentCardsList.layout(),
            self.vaultForm.contactsList.layout()
        ]

        if not query:
            for layout in layouts:
                for i in range(layout.count()):
                    item = layout.itemAt(i)
                    if item and item.widget():
                        item.widget().setVisible(True)
            return

        for layout in layouts:
            for i in range(layout.count()):
                item = layout.itemAt(i)
                widget = item.widget()
                
                if widget and hasattr(widget, "item_data"):
                    data = widget.item_data
                    # Search in all possible fields
                    search_text = ""
                    
                    # Common fields
                    search_text += data.get("name", "").lower() + " "
                    search_text += data.get("notes", "").lower() + " "  # This is the comments field
                    
                    # Type-specific fields
                    item_type = data.get("type", "").lower()
                    inner_data = data.get("data", {})
                    
                    # Include comments from nested data if available
                    search_text += inner_data.get("notes", "").lower() + " "
                    
                    if item_type == "passwords":
                        search_text += inner_data.get("site", "").lower() + " "
                        search_text += inner_data.get("username", "").lower() + " "
                        search_text += inner_data.get("password", "").lower() + " "
                    elif item_type == "notes":
                        search_text += inner_data.get("title", "").lower() + " "
                        search_text += inner_data.get("body", "").lower() + " "
                    elif item_type == "payment cards":
                        search_text += inner_data.get("number", "").lower() + " "
                        search_text += inner_data.get("expiry", "").lower() + " "
                        search_text += inner_data.get("holder", "").lower() + " "
                        search_text += inner_data.get("address", "").lower() + " "
                    elif item_type == "contacts":
                        search_text += inner_data.get("contactName", "").lower() + " "
                        search_text += inner_data.get("contactEmail", "").lower() + " "
                        search_text += inner_data.get("contactPhone", "").lower() + " "
                    
                    # Check if query matches any part of the search text
                    widget.setVisible(query in search_text)

                # Don't hide the stretch
                if not widget:
                    continue

    def openLink(self, url):
        url = QUrl(url)
        QDesktopServices.openUrl(url)

    def isValidUrl(self, url: str) -> bool:
        qurl = QUrl(url)
        return qurl.isValid() and qurl.scheme() in ("http", "https") and not qurl.isRelative()

    def toggleCvvVisibility(self, label, btn, cvv):
        """Toggle CVV visibility between masked and actual value"""
        if label.text() == "•••":
            label.setText(cvv)
            btn.setText("Hide")
        else:
            label.setText("•••")
            btn.setText("Show")

    def copyToClipboard(self, text):
        """Copy text to clipboard and start expiration timer"""
        if not text:
            return
            
        QApplication.clipboard().setText(text)
        
        # Get expiration time from settings (in minutes)
        expiration_min = int(self.settings.value(f"{self.userEmail}/clipboard/expirationTime", "1"))
        expiration_ms = expiration_min * 60 * 1000
        
        # Start/restart timer
        self.clipboard_timer.start(expiration_ms)
        
        # Update UI status
        self.updateClipboardStatus()
        self.showMessageModal("Copied", "Text copied to clipboard", duration=1000)

    def clearClipboard(self):
        """Clear clipboard and update status"""
        clipboard = QApplication.clipboard()
        
        # Only clear if it contains our password (optional safety check)
        current_text = clipboard.text()
        if current_text:  # Add more specific check if needed
            clipboard.clear()
        
        self.clipboard_timer.stop()
        self.updateClipboardStatus()

    def updateClipboardStatus(self):
        """Update clipboard status in footer"""
        if self.clipboard_timer.isActive():
            remaining = self.clipboard_timer.remainingTime() // 1000
            status = f"Password expires in {remaining}s"
        else:
            status = "Clipboard: Ready"
        
        self.footer.clipboardStatusLabel.setText(status)

    def handleAppQuit(self):
        """Handle application quit - clear clipboard if enabled"""
        if self.settings.value(f"{self.userEmail}/clipboard/clearOnClose", False, bool):
            self.clearClipboard()


    def clearLayout(self, layout):
        """Clear all widgets from a layout"""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def createVaultItemWidget(self, item_data, parent=None):
        """
        Create a vault item widget using data from the database.
        
        Args:
            item_data (dict): Dictionary containing vault item data from the database
            parent (QWidget): Parent widget for the created widget
            
        Returns:
            QWidget: Configured vault item widget
        """
        # Create the main widget
        widget = QWidget(parent)
        widget.setMaximumSize(QSize(16777215, 52))
        
        # Create the layout
        grid_layout = QGridLayout(widget)
        grid_layout.setHorizontalSpacing(10)
        grid_layout.setVerticalSpacing(0)
        grid_layout.setContentsMargins(10, 10, 10, 10)
        
        # Extract the nested data if it exists
        data = item_data.get('data', {})
        item_name = data.get('name', item_data.get('name', 'Untitled'))
        item_type = data.get('type', item_data.get('type', 'Unknown')).lower()
        
        # Item name frame
        frame_name = QFrame()
        frame_name.setMinimumSize(QSize(140, 0))
        frame_name.setMaximumSize(QSize(140, 16777215))
        
        h_layout_name = QHBoxLayout(frame_name)
        h_layout_name.setSpacing(8)
        h_layout_name.setContentsMargins(0, 0, 0, 0)
        
        # Set icon based on item type
        icon_label = QLabel()
        icon_label.setMinimumSize(QSize(24, 24))
        icon_label.setMaximumSize(QSize(24, 24))
        icon_label.setScaledContents(True)
        
        # Set appropriate icon based on item type
        if item_type == 'password' or item_type == 'passwords':
            icon_label.setPixmap(QPixmap(self.resources+"material_design/password.png"))
        elif item_type == 'notes':
            icon_label.setPixmap(QPixmap(self.resources+"material_design/sticky_note_2.png"))
        elif item_type == 'payment cards':
            icon_label.setPixmap(QPixmap(self.resources+"material_design/credit_card.png"))
        elif item_type == 'contacts':
            icon_label.setPixmap(QPixmap(self.resources+"material_design/contact_phone.png"))
        else:
            icon_label.setPixmap(QPixmap(self.resources+"material_design/error_outline.png"))
        
        name_label = QLabel(item_name)
        h_layout_name.addWidget(icon_label)
        h_layout_name.addWidget(name_label)
        
        grid_layout.addWidget(frame_name, 0, 0, 1, 1)

        # Add indicators frame after the name frame
        indicators_frame = QFrame()
        indicators_frame.setMaximumSize(QSize(80, 24))
        indicators_layout = QHBoxLayout(indicators_frame)
        indicators_layout.setContentsMargins(0, 0, 0, 0)
        indicators_layout.setSpacing(2)
        
        item_id = item_data.get('id')
        open_b = QLabel()
        open_b.setText("( ")
        indicators_layout.addWidget(open_b)
        
        if item_id:
            # Weak password indicator
            if item_id in self.password_stats['weak_passwords']:
                weak_icon = QLabel()
                weak_icon.setText("W")
                weak_icon.setObjectName("weakPassword")
                weak_icon.setToolTip("Weak password (less than 8 characters)")
                indicators_layout.addWidget(weak_icon)
            
            # Reused password indicator
            if item_id in self.password_stats['reused_passwords']:
                reused_icon = QLabel()
                reused_icon.setText("R")
                weak_icon.setObjectName("reusedPassword")
                reused_icon.setToolTip("Password reused in other items")
                indicators_layout.addWidget(reused_icon)
            
            # Old password indicator
            if item_id in self.password_stats['old_passwords']:
                old_icon = QLabel()
                old_icon.setText("O")
                weak_icon.setObjectName("oldPassword")
                old_icon.setToolTip("Password older than 6 months")
                indicators_layout.addWidget(old_icon)
        close_b = QLabel()
        close_b.setText(" )")
        indicators_layout.addWidget(close_b)
        
        # Add the indicators frame to the grid layout
        grid_layout.addWidget(indicators_frame, 0, 1, 1, 1)
        
        # Item type frame
        frame_type = QFrame()
        frame_type.setMinimumSize(QSize(120, 0))
        frame_type.setMaximumSize(QSize(120, 16777215))
        
        h_layout_type = QHBoxLayout(frame_type)
        h_layout_type.setSpacing(0)
        h_layout_type.setContentsMargins(0, 0, 0, 0)
        
        type_label = QLabel(item_type.capitalize())
        type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_layout_type.addWidget(type_label)
        
        grid_layout.addWidget(frame_type, 0, 2, 1, 1)
        
        # Last modified frame
        frame_modified = QFrame()
        frame_modified.setMinimumSize(QSize(120, 0))
        frame_modified.setMaximumSize(QSize(120, 16777215))
        
        h_layout_modified = QHBoxLayout(frame_modified)
        h_layout_modified.setSpacing(0)
        h_layout_modified.setContentsMargins(0, 0, 0, 0)
        
        # Format the date (handle both SQLite and ISO formats)
        modified_date = item_data.get('updated_at', '')
        if modified_date:
            try:
                # Try ISO format first
                modified_date = datetime.fromisoformat(modified_date).strftime('%m/%d/%Y %H:%M')
            except ValueError:
                try:
                    # Try SQLite format if ISO fails
                    modified_date = datetime.strptime(modified_date, '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M')
                except:
                    modified_date = 'N/A'
        else:
            modified_date = 'N/A'
        
        modified_label = QLabel(modified_date)
        modified_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_layout_modified.addWidget(modified_label)
        
        grid_layout.addWidget(frame_modified, 0, 4, 1, 1)
        
        # Actions frame
        frame_actions = QFrame()
        frame_actions.setMinimumSize(QSize(160, 0))
        frame_actions.setMaximumSize(QSize(160, 16777215))
        
        h_layout_actions = QHBoxLayout(frame_actions)
        h_layout_actions.setSpacing(6)
        h_layout_actions.setContentsMargins(0, 0, 0, 0)
        
        # Add action buttons
        view_btn = QPushButton()
        view_btn.setIcon(QIcon(self.resources+"font_awesome/solid/eye.png"))
        view_btn.setToolTip("View item details")
        
        edit_btn = QPushButton()
        edit_btn.setIcon(QIcon(self.resources+"material_design/edit.png"))
        edit_btn.setToolTip("Edit item")
        
        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon(self.resources+"material_design/delete_forever.png"))
        delete_btn.setToolTip("Delete item")
        
        h_layout_actions.addWidget(view_btn)
        h_layout_actions.addWidget(edit_btn)
        h_layout_actions.addWidget(delete_btn)
        
        grid_layout.addWidget(frame_actions, 0, 6, 1, 1)
        
        # Add vertical separators using QCustomVerticalSeparator
        separator1 = QCustomVerticalSeparator()
        separator1.setMaximumSize(QSize(16777215, 20))
        grid_layout.addWidget(separator1, 0, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)
        
        separator2 = QCustomVerticalSeparator()
        separator2.setMaximumSize(QSize(16777215, 20))
        grid_layout.addWidget(separator2, 0, 3, 1, 1)
        
        separator3 = QCustomVerticalSeparator()
        separator3.setMaximumSize(QSize(16777215, 20))
        grid_layout.addWidget(separator3, 0, 5, 1, 1)
        
        # Store the complete item data as a property for later reference
        widget.item_data = item_data
        widget.item_id = item_data.get('id', None)
        
        return widget
    
    def editVaultItem(self, item_data):
        """Edit an existing vault item"""
        try:
            # Initialize the vault form dialog if not already done
            if not hasattr(self, 'vaultFormDialog'):
                self.initVaultForm()
            
            # Store the item ID being edited
            self.editingVaultItemId = item_data.get('id')
            
            # Show the form
            form = self.vaultFormDialog.shownForm
            
            # Set the item type first (this will switch the stacked widget)
            item_type = item_data.get('type', 'Passwords')
            index = form.itemTypeComboBox.findText(item_type)
            if index >= 0:
                form.itemTypeComboBox.setCurrentIndex(index)
            
            # Fill common fields
            form.itemNameLineEdit.setText(item_data.get('name', ''))
            
            data = item_data.get('data', [])
            form.notesPlainTextEdit.setPlainText(data.get('notes', ''))
            # Fill type-specific fields
            if item_type == 'Passwords':
                form.siteNameLineEdit.setText(data.get('site', ''))
                form.usernameLineEdit.setText(data.get('username', ''))
                form.passwordLineEdit.setText(data.get('password', ''))
            elif item_type == 'Notes':
                form.noteTitleLineEdit.setText(data.get('title', ''))
                form.noteBodyPlainTextEdit.setPlainText(data.get('body', ''))
            elif item_type == 'Payment Cards':
                form.cardNumberLineEdit.setText(data.get('number', ''))
                form.expiryDateEdit.setDate(QDate.fromString(data.get('expiry', '')))
                form.cvvLineEdit.setText(data.get('cvv', ''))
                form.cardHolderLineEdit.setText(data.get('holder', ''))
                form.billingAddressLineEdit.setText(data.get('address', ''))
            elif item_type == 'Contacts':
                form.contactNameLineEdit.setText(data.get('contactName', ''))
                form.contactEmailLineEdit.setText(data.get('contactEmail', ''))
                form.contactPhoneLineEdit.setText(data.get('contactPhone', ''))
            
            # Show the dialog
            self.vaultFormDialog.show()
            
        except Exception as e:
            self.showMessageModal("Error", f"Could not edit item: {str(e)}", type="warning", duration=3000)

    def deleteVaultItem(self, item_data):
        """Delete a vault item after confirmation"""
        try:
            # Show confirmation dialog
            self.showMessageModal(
                title="Confirm Deletion",
                description=f"Are you sure you want to delete '{item_data.get('name', 'this item')}'?",
                type="warning",
                okayText="Delete",
                cancelText="Cancel",
                okayAction=lambda: self._confirmDeleteItem(item_data),
                cancelBtnType="default",
                okayBtnType="warning",
                duration=5000
            )
        except Exception as e:
            self.showMessageModal("Error", f"Could not delete item: {str(e)}", type="warning", duration=3000)

    def _confirmDeleteItem(self, item_data):
        """Actually delete the item after confirmation"""
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning", duration=2000)
            return
            
        item_id = item_data.get('id')
        if not item_id:
            self.showMessageModal("Error", "Invalid item ID", type="warning", duration=2000)
            return
            
        self.backendWorker.deleteVaultItemWorker(item_id, self.userEmail)  

    def handleVaultItemDeleted(self, item_id):
        """Handle successful vault item deletion"""
        self.showMessageModal("Success", "Vault item deleted successfully.", type="success", duration=2500)
        # Refresh the vault items
        self.loadVaultItems()

    def updateUsername(self):
        """Update the user's first and last name"""
        try:
            # Get current user data
            user_data = self.backendWorker.dbHandler.getUserByEmail(self.userEmail)
            if not user_data:
                self.showMessageModal("Error", "User not found", type="warning", duration=2000)
                return
                
            # Show edit dialog
            dialog = QCustomQDialog(
                parent=self.main,
                frameless=True,
                windowMovable=True,
                showForm=EditUsernameForm(),
                setModal=True,
                showCancelButton=False,
                showYesButton=False
            )
            
            form = dialog.shownForm
            form.firstNameEdit.setText(user_data[0])  
            form.lastNameEdit.setText(user_data[1]) 
            
            def saveChanges():
                new_first = form.firstNameEdit.text().strip()
                new_last = form.lastNameEdit.text().strip()
                
                if not new_first or not new_last:
                    self.showMessageModal("Error", "Both names are required", 
                                        type="warning", duration=2000, parent=dialog)
                    return
                    
                self.backendWorker.updateUsernameWorker(self.userEmail, new_first, new_last)
                self.showMessageModal("Success", "Name updated successfully", 
                                    duration=2000)
                dialog.close()
                
            form.saveButton.clicked.connect(saveChanges)
            form.cancelButton.clicked.connect(dialog.close)
            dialog.show()
            
        except Exception as e:
            self.showMessageModal("Error", f"Could not update name: {str(e)}", 
                                type="warning", duration=3000)

    def deleteAccount(self):
        """Delete user account with confirmation"""
        try:
            self.showMessageModal(
                title="Delete Account",
                description="This will permanently delete your account and all data. Continue?",
                type="warning",
                okayText="Delete",
                cancelText="Cancel",
                okayAction=self._confirmAccountDeletion,
                okayBtnType="danger",
                cancelBtnType="default"
            )
        except Exception as e:
            self.showMessageModal("Error", f"Could not delete account: {str(e)}", 
                                type="warning", duration=3000)

    def _confirmAccountDeletion(self):
        """Actually delete the account after confirmation"""
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning", duration=2000)
            return
            
        self.backendWorker.deleteAccountWorker(self.userEmail)

    def handleAccountDeleted(self):
        """Reset the application after account deletion"""
        # Clear all user data
        self.userEmail = None
        self.settings.clear()
        
        # Reset UI
        self.ui.mainBodyPages.setCurrentWidget(self.ui.welcomePage)
        self.loginForm.accountPages.setCurrentWidget(self.loginForm.loginPage)
        
        # Clear vault items display
        self.clearVaultItems()
        
        self.showMessageModal("Account Deleted", 
                            "Your account and all data have been permanently deleted.",
                            duration=5000)

    def clearVaultItems(self):
        """Clear all vault items from the UI"""
        vf = self.vaultForm
        self.clearLayout(vf.passwordList.layout())
        self.clearLayout(vf.notesList.layout())
        self.clearLayout(vf.paymentCardsList.layout())
        self.clearLayout(vf.contactsList.layout())
        
        # Add stretches back
        vf.passwordList.layout().addStretch()
        vf.notesList.layout().addStretch()
        vf.paymentCardsList.layout().addStretch()
        vf.contactsList.layout().addStretch()

    def displayUserProfile(self, email: str = None):
        """Display user profile information in the settings form"""
        try:
            # Use provided email or current logged in user
            user_email = email if email else self.userEmail
            if not user_email:
                return
                
            # Get user data from database
            user_data = self.backendWorker.dbHandler.getUserByEmail(user_email)
            if not user_data:
                self.showMessageModal("Error", "User not found", type="warning", duration=2000)
                return
                
            # Unpack the data tuple
            first_name, last_name, email, _ = user_data
            
            # Update the UI elements in settings form
            sf = self.userForm
            sf.profileNameLabel.setText(f"{first_name} {last_name}")
            sf.profileEmailLabel.setText(email)
            self.dashboard.welcomeName.setText(f"Hello,  {first_name}!")
            
        except Exception as e:
            self.showMessageModal("Error", f"Could not load profile: {str(e)}", 
                                type="warning", duration=3000)
    
    def startSecurityScan(self):
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning", duration=2000)
            return
        self.backendWorker.scanVaultSecurityWorker(self.userEmail)
        self.backendWorker.loadVaultItemStatsWorker(self.userEmail)


    def handleVaultSecurityScanResult(self, result):
        try:
            scan_ui = self.securityScanForm
            dash = self.dashboard

            scan_ui.vaultScoreProgressBar.setValue(result['vault_score'])
            scan_ui.weakPassLabel.setText(str(result['weak_passwords']))
            scan_ui.reusedPassLabel.setText(str(result['reused_passwords']))
            scan_ui.oldPassLabel.setText(str(result['old_passwords']))
            scan_ui.vaultScoreLabel.setText(
                f"Vault health score: {result['vault_score']}%. {result['weak_passwords']} weak, "
                f"{result['reused_passwords']} reused, {result['old_passwords']} old."
            )

            scan_ui.breachLabel.setText(f"{result['breach_count']} credentials exposed in breaches")

            dash.vaultScoreProgressBar.setValue(result['vault_score'])
            dash.weakPassLabel.setText(str(result['weak_passwords']))
            dash.reusedPassLabel.setText(str(result['reused_passwords']))
            dash.oldPassLabel.setText(str(result['old_passwords']))
            dash.breachLabel.setText(f"{result['breach_count']} credentials exposed in breaches")
            
        except Exception as e:
            self.showMessageModal("Scan Error", f"Failed to load scan results: {e}", type="warning", duration=3000)
    
    def handleVaultItemStatsResult(self, data: dict):
        self.donutChartWidget.updateData(data)
        self.updateDahboardLabels(data)
    
    def updateDahboardLabels(self, data: dict):
        dash = self.dashboard
        dash.totalPassLabel.setText(f"Total Passwords: {data.get('Passwords', 0)}")
        dash.totalContactsLabel.setText(f"Total Contacts: {data.get('Contacts', 0)}")
        dash.totalNotesLabel.setText(f"Total Notes: {data.get('Notes', 0)}")
        dash.totalCardsLabel.setText(f"Total Payment Cards: {data.get('Payment Cards', 0)}")

    def updateStatusDisplay(self):
        """Update the status bar with backup, encryption, storage, and other info"""
        settings = QSettings()
        
        # Last Backup
        last_backup = settings.value(f"{self.userEmail}/backup/last_backup", "Never")

        # Last sync
        last_sync = settings.value(f"{self.userEmail}/sync/last_sync", 'Never')
        
        # Encryption Status
        encryption_status = settings.value(f"{self.userEmail}/security/encryption", "AES-256 Active")
        
        # Auto-lock timer (in minutes)
        auto_lock_minutes = settings.value(f"{self.userEmail}/general/autoLockTimer", "1")  # Default 1 minute
        
        # Storage Calculation
        db_size = self.calculateDbSize()
        max_storage = settings.value(f"{self.userEmail}/storage/max_size", 1)  # Default 1MB
        storage_percent = min(int((db_size / max_storage) * 100), 100)
        
        # Update the dashboard widgets
        form = self.dashboard
        form.lastBackupLabel.setText(f"Last Backup: {last_backup}")
        form.encryptionStatusLabel.setText(f"Encryption Status: {encryption_status}")
        form.storageProgressBar.setValue(storage_percent)
        form.storageUsedLabel.setText(f"Storage Used: {db_size}MB")
        
        # Add new status labels 
        footer = self.footer
        footer.autoLockLabel.setText(f"Auto-lock in {auto_lock_minutes} min")
        footer.clipboardStatusLabel.setText("Clipboard status: Ready")  # Will be updated by checkClipboardStatus
        footer.lastSyncedLabel.setText(f"Last synced: {last_sync}")
        footer.versionLabel.setText(f"v{settings.value('app/version', '1.0.0')}")
        
        # 
        self.settingsForm.lastBackupLabel.setText(f"Last Backup: {last_backup}")
        self.settingsForm.lastSyncLabel.setText(f"Last synced: {last_sync}")

        # Start checking clipboard status
        self.checkClipboardStatus()

    def checkClipboardStatus(self):
        """Check clipboard status and update the label accordingly"""
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        
        if text:
            # Check if text looks like a password (simple heuristic)
            is_password = (len(text) >= 8 and 
                        any(c.isupper() for c in text) and 
                        any(c.islower() for c in text) and
                        any(c.isdigit() for c in text))
            
            if is_password:
                # Get clipboard expiration time from settings
                expiration_min = int(self.settings.value(f"{self.userEmail}/clipboard/expirationTime", "1"))
                expiration_sec = expiration_min * 60
                
                # Calculate time remaining
                if hasattr(self, 'clipboard_timer'):
                    remaining = self.clipboard_timer.remainingTime() // 1000
                    status = f"Password expires in {remaining}s"
                else:
                    status = f"Password expires in {expiration_sec}s"
                
                self.footer.clipboardStatusLabel.setText(f"Clipboard status: {status}")
                
                # Start/restart timer if needed
                if not hasattr(self, 'clipboard_timer'):
                    self.clipboard_timer = QTimer()
                    self.clipboard_timer.timeout.connect(self.clearClipboard)
                    self.clipboard_timer.start(expiration_sec * 1000)
            else:
                self.footer.clipboardStatusLabel.setText("Clipboard status: Ready")
        else:
            self.footer.clipboardStatusLabel.setText("Clipboard status: Empty")

    def calculateDbSize(self):
        """Calculate database size in MB"""
        db_path = self.backendWorker.dbHandler.db_path
        try:
            if os.path.exists(db_path):
                size_bytes = os.path.getsize(db_path)
                return round(size_bytes / (1024 * 1024), 2)  # Convert to MB
        except Exception as e:
            print(f"Error calculating DB size: {e}")
        return 0

    def startActivityTracking(self):
        # Track mouse movements
        self.main.installEventFilter(self)
        # Start with current settings
        self.resetInactivityTimer()

    def eventFilter(self, obj, event):
        # Reset timer on any user activity
        if event.type() in [QEvent.MouseMove, QEvent.KeyPress, QEvent.WindowActivate]:
            self.resetInactivityTimer()
            self.ensureEncryptionMethod()
        return super().eventFilter(obj, event)

    def resetInactivityTimer(self):
        """Reset the inactivity timer with current settings"""
        try:
            lock_time = int(self.settings.value(f"{self.userEmail}/general/autoLockTimer", "30"))  # in minutes(30 min default)
            self.inactivity_timer.start(lock_time * 60 * 1000)  # convert to milliseconds
        except:
            # string found
            pass

    def handleInactivityTimeout(self):
        """Handle when inactivity period exceeds auto-lock timer"""
        if self.userEmail:  # Only lock if user is logged in
            self.logout()
            self.showMessageModal(
                "Auto-Locked", 
                "You've been logged out due to inactivity",
                duration=3000
            )
    
    def handleChangePasswordRequest(self):
        """Handle change master password button click"""
        self.showMessageModal(
            title="Reset Password!!",
            description=(
                "<b>⚠️ DESTRUCTIVE ACTION!</b><br><br>"
                "This will <b>permanently delete ALL</b> items in your vault:<br>"
                "- All passwords<br>"
                "- All secure notes<br>"
                "- All payment cards<br>"
                "- All contacts<br><br>"
                "<b>⚠️ Sync your items first to upload them before changing your local password!</b><br><br>"
                "This cannot be undone!"
            ),
            type="warning",
            okayText="Logout to Reset Password",
            cancelText="Cancel",
            okayBtnType="danger",
            cancelBtnType="default",
            okayAction=self.startChangePassword,
            duration=-1 
        )

    def startChangePassword(self):
        # Log out current user
        self.logout()
        
        # Show instruction message
        self.showMessageModal(
            "Password Change Required",
            "You've been logged out to recover your password.\n\n"
            "Please click Login then 'Forgot Password' to change your password.",
            okayText="Go to Login",
            duration=3000 
        )

    def exportEncryptedVault(self):
        """Export the user's vault as encrypted file using standard Qt dialogs"""
        if not self.userEmail:
            QMessageBox.warning(self.main, "Error", "No user logged in")
            return
        
        # 1. Get password from user using standard QInputDialog
        password, ok = QInputDialog.getText(
            self.main,
            "Vault Export",
            "Enter encryption password:",
            QLineEdit.Password
        )
        if not ok or not password:
            return
        
        try:
            # 2. Get all vault items
            dd_pass = self.backendWorker.getPassword()
            vault_items = self.backendWorker.dbHandler.getAllVaultItems(self.userEmail, dd_pass)
            if not vault_items:
                raise Exception("No vault items found")
            
            # 3. Prepare data for encryption
            export_data = {
                'version': 1,
                'email': self.userEmail,
                'items': vault_items,
                'exported_at': datetime.now().isoformat()
            }
            json_data = json.dumps(export_data).encode('utf-8')
            
            # 4. Encrypt with AES-256
            salt = get_random_bytes(16)
            key = scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1)
            cipher = AES.new(key, AES.MODE_GCM)
            ciphertext, tag = cipher.encrypt_and_digest(json_data)
            
            # 5. Package encrypted data
            encrypted_package = {
                'salt': base64.b64encode(salt).decode(),
                'nonce': base64.b64encode(cipher.nonce).decode(),
                'tag': base64.b64encode(tag).decode(),
                'ciphertext': base64.b64encode(ciphertext).decode()
            }
            
            # 6. Save to file using standard QFileDialog
            file_path, _ = QFileDialog.getSaveFileName(
                self.main,
                "Save Encrypted Vault",
                f"trusted_in_vault_export_{datetime.now().strftime('%Y%m%d')}.tivault",
                "TrustedIn Vault (*.tivault)"
            )
            
            if file_path:
                with open(file_path, 'w') as f:
                    json.dump(encrypted_package, f)
                
                # Update last backup time
                last_backup = datetime.now().strftime("%b %d, %Y %H:%M")
                self.settings.setValue(f"{self.userEmail}/backup/last_backup", last_backup)
                self.updateStatusDisplay()
                
                self.showMessageModal(
                    "Export Successful",
                    f"Vault exported successfully to:\n{file_path}",
                    type="success",
                    duration=2000
                )
        
        except Exception as e:
            QMessageBox.warning(
                self.main,
                "Export Failed",
                f"Could not export vault: {str(e)}"
            )

    def importEncryptedVault(self):
        """Import an encrypted vault file"""
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning")
            return
        
        # Get file path using standard QFileDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self.main,
            "Open Encrypted Vault",
            "",
            "TrustedIn Vault (*.tivault);;All Files (*)"
        )
        
        if not file_path:
            return  # User cancelled
        
        # Get password from user
        password, ok = QInputDialog.getText(
            self.main,
            "Vault Import",
            "Enter encryption password:",
            QLineEdit.Password
        )
        if not ok or not password:
            return
        
        # Show processing message
        self.showMessageModal(
            "Processing", 
            "Decrypting and importing vault data...",
            type="info",
            duration=2000
        )
        
        # Start the import worker
        self.backendWorker.importVaultWorker(self.userEmail, file_path, password)
    
    def handleImportResult(self, result):
        """Handle the result of the import operation"""
        if result.get('success'):
            self.showMessageModal(
                "Import Successful",
                result['message'],
                type="success",
                duration=5000
            )
            # Refresh the vault to show new items
            self.loadVaultItems()
        else:
            self.showMessageModal(
                "Import Failed",
                result['message'],
                type="warning",
                duration=5000
            )

    def confirmResetVault(self):
        """Show custom confirmation dialog before resetting vault"""
        if not self.userEmail:
            self.showMessageModal(
                "Error", 
                "No user logged in",
                type="warning",
                duration=3000
            )
            return

        # Use your custom modal for confirmation
        self.showMessageModal(
            title="Reset Vault Data",
            description=(
                "<b>⚠️ DESTRUCTIVE ACTION!</b><br><br>"
                "This will <b>permanently delete ALL</b> items in your vault:<br>"
                "- All passwords<br>"
                "- All secure notes<br>"
                "- All payment cards<br>"
                "- All contacts<br><br>"
                "This cannot be undone!"
            ),
            type="warning",
            okayText="Reset Vault",
            cancelText="Cancel",
            okayBtnType="danger",
            cancelBtnType="default",
            okayAction=self.resetVaultData,
            duration=0  # Persistent until user action
        )

    def resetVaultData(self):
        """Perform the vault reset after confirmation"""
        try:
            # Show processing notification
            self.showMessageModal(
                "Processing", 
                "Resetting vault data...",
                type="info",
                duration=2000
            )
            
            # Call backend to delete all vault items
            success = self.backendWorker.dbHandler.deleteAllVaultItems(self.userEmail)
            
            if success:
                # Refresh the vault display
                self.loadVaultItems()
                
                # Show success notification
                self.showMessageModal(
                    "Vault Reset", 
                    "All vault items have been permanently deleted.",
                    type="success",
                    duration=5000
                )

                # logut the user
                self.logout()
            else:
                raise Exception("Failed to reset vault data")
                
        except Exception as e:
            self.showMessageModal(
                "Reset Failed", 
                f"Could not reset vault: {str(e)}",
                type="warning",
                duration=5000
            )
    
    # Change in GuiFunctions.py
    def syncVaultItems(self):
        """Trigger two-way vault item sync"""
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning")
            return
        
        self.showMessageModal(
            "Syncing", 
            "Synchronizing vault items with server...",
            type="info",
            duration=2000
        )
        
        # Change this line to call the new sync method
        self.backendWorker.syncVaultItemsWorker(self.userEmail)

    def handleVaultSyncResult(self, result):
        """Handle sync completion"""
        if result.get('success'):
            last_sync = datetime.now().strftime("%b %d, %Y %H:%M")
            self.settings.setValue(f"{self.userEmail}/sync/last_sync", last_sync)
            self.updateStatusDisplay()
            
            self.showMessageModal(
                "Sync Complete", 
                f"Uploaded {result.get('uploaded', 0)} items to server",
                type="success",
                duration=3000
            )
        else:
            self.showMessageModal(
                "Sync Failed", 
                result.get('message', 'Unknown error'),
                type="warning",
                duration=5000
            )

    def generateSecurityReport(self):
        """Handle report generation button click"""
        if not self.userEmail:
            self.showMessageModal("Error", "No user logged in", type="warning")
            return
        
        # Get report data
        report_data = self.backendWorker.generateSecurityReport(self.userEmail)
        
        # Generate PDF
        report_generator = ReportGenerator()
        pdf_bytes = report_generator.generate_report(report_data)
        
        # Show save dialog
        file_path, _ = QFileDialog.getSaveFileName(
            self.main,
            "Save Security Report",
            f"trustedin_security_report_{datetime.now().strftime('%Y%m%d')}.pdf",
            "PDF Files (*.pdf)"
        )
        
        if file_path:
            with open(file_path, 'wb') as f:
                f.write(pdf_bytes)
            self.showMessageModal(
                "Report Generated",
                f"Security report saved to:\n{file_path}",
                type="success",
                duration=3000
            )
            
            # Optionally open the PDF
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def initAboutForm(self):
        try:
            # Initialize a custom dialog for the vault form
            self.aboutFormDialog = QCustomQDialog(
                parent=self.main,
                frameless = True,
                windowMovable = False,
                showForm = AboutForm(),
                setModal = True,
                showYesButton = False,
                showCancelButton = False,
            )

            form = self.aboutFormDialog.shownForm

            # Close dialog on cancel
            form.closeBtn.clicked.connect(self.aboutFormDialog.close)
        
        except Exception as e:
            print(e)

    def showAboutForm(self):
        try:
            self.aboutFormDialog.show()
        except Exception as e:
            print(e)
            self.initAboutForm()
            self.aboutFormDialog.show()
    