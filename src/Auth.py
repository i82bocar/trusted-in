# src/Auth.py
from qtpy.QtCore import QObject, Signal
import hashlib
import re
import requests
import json

class Auth(QObject):
    # Signals for GUI interaction
    resendVerificationEmailFinished = Signal(dict)
    verifyEmailFinished = Signal(dict)
    uploadUserFinished = Signal(dict)

    uploadVaultItemFinished = Signal(dict)
    uploadVaultItemsFinished = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        # Optional future state (e.g. session data, OTP tokens)
        pass

    def hashPassword(self, password: str) -> str:
        """
        Returns SHA-256 hash of the password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def verifyPassword(self, inputPassword: str, storedHash: str) -> bool:
        """
        Compares a plaintext password to a stored hashed password.
        """
        return self.hashPassword(inputPassword) == storedHash

    def isValidEmail(self, email: str) -> bool:
        """
        Validates the format of an email string.
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def resendVerificationEmail(self, email: str) -> dict:
        """
        Requests a new verification token to be sent to the user's email.

        Args:
            email (str): The user's email address.

        Returns:
            dict: JSON response from the server with status and message.
        """
        url = "https://spinncode.com/updaters/sd_account_verification.php"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "resend_verification_email": "true",
            "email": email,
            "ignore_verified": True
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "resend_verification_email_response": "A network error occurred while requesting the verification email.",
                "error": str(err)
            }
        
        self.resendVerificationEmailFinished.emit(result)
        return result
        
    def verifyEmail(self, email: str, token: str) -> dict:
        """
        Verifies a user's email by sending the token and email to the backend.

        Args:
            email (str): The user's email address.
            token (str): The verification token to be validated.

        Returns:
            dict: JSON response from the server with success status and message.
        """
        url = "https://spinncode.com/updaters/sd_account_verification.php"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "verify_email": "true",
            "email": email,
            "token": token
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "verify_email_response": "A network error occurred while verifying the token.",
                "error": str(err)
            }

        self.verifyEmailFinished.emit(result)
        return result
    
    def uploadUser(self, first_name: str, last_name: str, email: str, password_hash: str) -> dict:
        """
        Uploads a new user's information to the PHP backend for server-side registration.

        Args:
            first_name (str): First name of the user.
            last_name (str): Last name of the user.
            email (str): Email of the user.
            password_hash (str): Hashed password (SHA-256).

        Returns:
            dict: JSON response from the server indicating success or failure.
        """
        url = "https://project.spinncode.com/account_register.php"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "register_user": "true",
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password_hash": password_hash
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "upload_user_response": "Failed to register user on remote server.",
                "error": str(err)
            }

        self.uploadUserFinished.emit(result)
        return result

    def uploadVaultItem(self, user_email: str, item_data: dict) -> dict:
        """
        Uploads a single vault item to the server
        """
        url = "https://project.spinncode.com/vault_upload.php"
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "upload_item": "true",
            "user_email": user_email,
            "item_data": json.dumps(item_data)
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "upload_response": "Failed to upload vault item",
                "error": str(err)
            }

        self.uploadVaultItemFinished.emit(result)
        return result

    def uploadVaultItems(self, user_email: str, items: list) -> dict:
        """
        Uploads multiple vault items using form-encoded POST data.
        Expects items to be decrypted before passing to this method.
        """
        url = "https://project.spinncode.com/vault_upload.php"
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "upload_items": "true",
            "user_email": user_email,
            "items": json.dumps(items)  # Items should already be decrypted
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "upload_response": "Failed to upload vault items",
                "error": str(err)
            }

        self.uploadVaultItemsFinished.emit(result)
        return result

    def downloadVaultItems(self, user_email: str) -> dict:
        """
        Downloads all vault items for a user from the server
        """
        url = "https://project.spinncode.com/vault_download.php"
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "download_items": "true",
            "user_email": user_email
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "download_response": "Failed to download vault items",
                "error": str(err)
            }

        return result
    
    def deleteVaultItem(self, user_email: str, item_data: dict) -> dict:
        """
        Deletes a vault item from the server using multiple identifying fields.
        
        Args:
            user_email (str): The user's email
            item_data (dict): Dictionary containing item identifying information
                Should include: type, name, and the encrypted data
                
        Returns:
            dict: JSON response from the server
        """
        url = "https://project.spinncode.com/vault_delete.php"
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "delete_item": "true",
            "user_email": user_email,
            "item_type": item_data.get('type', ''),
            "item_name": item_data.get('name', ''),
            "item_data": json.dumps(item_data.get('data', {}))
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as err:
            result = {
                "success": False,
                "delete_response": "Failed to delete vault item",
                "error": str(err)
            }

        return result


# Resend token
# auth = Auth()
# result1 = auth.resendVerificationEmail("kibetkhamisi@gmail.com")
# print(result1.get("resend_verification_email_response"))

# Verify token
# result2 = auth.verifyEmail("kibetkhamisi@gmail.com", "mxBM")
# print(result2.get("verify_email_response"))
