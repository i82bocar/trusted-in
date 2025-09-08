from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from qtpy.QtCore import QSettings
import os
import base64
import json
import secrets
from typing import Union


class CryptoHelper:
    @staticmethod
    def deriveKey(password: str, salt: bytes, length: int = 32) -> bytes:
        """
        Derives a secure encryption key from a password using PBKDF2-HMAC-SHA256.

        Args:
            password (str): The user's password.
            salt (bytes): A cryptographic salt.
            length (int): Length of the key in bytes.

        Returns:
            bytes: The derived key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=salt,
            iterations=100_000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    @staticmethod
    def getEncryptionMethod(userEmail: str) -> str:
        """
        Gets the active encryption method based on QSettings.

        Returns:
            str: The active encryption method
        """
        settings = QSettings()
        return settings.value(f"{userEmail}/security/encryption", "AES-256 Active")

    @staticmethod
    def isChaCha20Active(userEmail: str) -> bool:
        """
        Determines whether ChaCha20 is the active encryption method.

        Returns:
            bool: True if ChaCha20 is selected, False otherwise.
        """
        method = CryptoHelper.getEncryptionMethod(userEmail)
        return method == "ChaCha20 Active"

    @staticmethod
    def isXORActive(userEmail: str) -> bool:
        """
        Determines whether XOR is the active encryption method.

        Returns:
            bool: True if XOR is selected, False otherwise.
        """
        method = CryptoHelper.getEncryptionMethod(userEmail)
        return method == "XOR Active"

    @staticmethod
    def isPBKActive(userEmail: str) -> bool:
        """
        Determines whether PBK (Password-Based Key) is the active encryption method.

        Returns:
            bool: True if PBK is selected, False otherwise.
        """
        method = CryptoHelper.getEncryptionMethod(userEmail)
        return method == "PBK Active"

    @staticmethod
    def xorEncryptDecrypt(data: bytes, key: bytes) -> bytes:
        """
        XOR encryption/decryption (NOT SECURE for production use).
        
        WARNING: This is a simple XOR cipher and is not cryptographically secure.
        Use only for educational purposes or combined with other encryption methods.
        
        Args:
            data (bytes): Data to encrypt/decrypt
            key (bytes): Encryption key
            
        Returns:
            bytes: XORed data
        """
        return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

    @staticmethod
    def pbkEncrypt(data: dict, password: str, salt: bytes) -> str:
        """
        Simple Password-Based Key encryption using derived key for XOR.
        
        Args:
            data (dict): Data to encrypt
            password (str): User password
            salt (bytes): Cryptographic salt
            
        Returns:
            str: JSON string with encrypted data
        """
        # Derive key from password
        key = CryptoHelper.deriveKey(password, salt, length=32)
        
        # Serialize data
        serialized = json.dumps(data).encode()
        
        # Encrypt using XOR with derived key
        ciphertext = CryptoHelper.xorEncryptDecrypt(serialized, key)
        
        encrypted = {
            "s": base64.b64encode(salt).decode(),
            "ct": base64.b64encode(ciphertext).decode()
        }
        return json.dumps(encrypted)

    @staticmethod
    def pbkDecrypt(encryptedStr: str, password: str) -> Union[dict, None]:
        """
        Decrypt PBK-encrypted data.
        
        Args:
            encryptedStr (str): Encrypted JSON string
            password (str): User password
            
        Returns:
            dict | None: Decrypted data or None if failed
        """
        try:
            encrypted = json.loads(encryptedStr)
            salt = base64.b64decode(encrypted["s"])
            ciphertext = base64.b64decode(encrypted["ct"])
            
            # Derive the same key
            key = CryptoHelper.deriveKey(password, salt, length=32)
            
            # Decrypt using XOR
            plaintext = CryptoHelper.xorEncryptDecrypt(ciphertext, key)
            
            return json.loads(plaintext.decode())
        except Exception as e:
            print(f"[PBK DECRYPT ERROR] {e}")
            return None

    @staticmethod
    def encryptData(data: dict, password: str, userEmail: str) -> str:
        """
        Encrypts a dictionary using the active encryption method.

        Args:
            data (dict): The data to encrypt.
            password (str): The password to derive the encryption key.

        Returns:
            str: A JSON string containing encrypted data.
        """
        salt = os.urandom(16)
        
        if CryptoHelper.isXORActive(userEmail):
            # XOR encryption (WARNING: Not secure for production)
            serialized = json.dumps(data).encode()
            key = CryptoHelper.deriveKey(password, salt, length=32)
            ciphertext = CryptoHelper.xorEncryptDecrypt(serialized, key)
            
            encrypted = {
                "s": base64.b64encode(salt).decode(),
                "ct": base64.b64encode(ciphertext).decode(),
                "method": "XOR"
            }
            
        elif CryptoHelper.isPBKActive(userEmail):
            # PBK encryption (uses XOR with derived key)
            return CryptoHelper.pbkEncrypt(data, password, salt)
            
        else:
            # Standard encryption (AES or ChaCha20)
            key = CryptoHelper.deriveKey(password, salt)
            nonce = os.urandom(12)
            serialized = json.dumps(data).encode()

            useChaCha = CryptoHelper.isChaCha20Active(userEmail)
            cipher = ChaCha20Poly1305(key) if useChaCha else AESGCM(key)

            ciphertext = cipher.encrypt(nonce, serialized, None)

            encrypted = {
                "s": base64.b64encode(salt).decode(),
                "n": base64.b64encode(nonce).decode(),
                "ct": base64.b64encode(ciphertext).decode(),
                "method": "ChaCha20" if useChaCha else "AES-256"
            }
            
        return json.dumps(encrypted)

    @staticmethod
    def decryptData(encryptedStr: str, password: str, userEmail: str) -> Union[dict, None]:
        """
        Safely decrypts an encrypted JSON string using the appropriate method.

        Args:
            encryptedStr (str): JSON string with encrypted data.
            password (str): The password to derive the decryption key.

        Returns:
            dict | None: The decrypted data, or None if decryption fails.
        """
        try:
            encrypted = json.loads(encryptedStr)
            
            # Check which encryption method was used
            method = encrypted.get("method", "")
            
            if method == "XOR" or CryptoHelper.isXORActive(userEmail):
                # XOR decryption
                salt = base64.b64decode(encrypted["s"])
                ciphertext = base64.b64decode(encrypted["ct"])
                key = CryptoHelper.deriveKey(password, salt, length=32)
                plaintext = CryptoHelper.xorEncryptDecrypt(ciphertext, key)
                return json.loads(plaintext.decode())
                
            elif "n" not in encrypted or CryptoHelper.isPBKActive(userEmail):
                # PBK decryption (no nonce field)
                return CryptoHelper.pbkDecrypt(encryptedStr, password)
                
            else:
                # Standard decryption (AES or ChaCha20)
                salt = base64.b64decode(encrypted["s"])
                nonce = base64.b64decode(encrypted["n"])
                ciphertext = base64.b64decode(encrypted["ct"])
                key = CryptoHelper.deriveKey(password, salt)

                useChaCha = CryptoHelper.isChaCha20Active(userEmail)
                cipher = ChaCha20Poly1305(key) if useChaCha else AESGCM(key)

                plaintext = cipher.decrypt(nonce, ciphertext, None)
                return json.loads(plaintext.decode())

        except (json.JSONDecodeError, KeyError, ValueError, Exception) as e:
            print(f"[DECRYPT ERROR] Failed to decrypt: {str(e)}")
            return None

    @staticmethod
    def getAvailableEncryptionMethods() -> list:
        """
        Returns list of available encryption methods.
        
        Returns:
            list: Available encryption methods
        """
        return [
            "AES-256 Active",
            "ChaCha20 Active", 
            "XOR Active",
            "PBK Active"
        ]

    @staticmethod
    def setEncryptionMethod(userEmail: str, method: str) -> bool:
        """
        Set the encryption method for a user.
        
        Args:
            userEmail (str): User email
            method (str): Encryption method
            
        Returns:
            bool: True if successful
        """
        if method not in CryptoHelper.getAvailableEncryptionMethods():
            return False
            
        settings = QSettings()
        settings.setValue(f"{userEmail}/security/encryption", method)
        return True