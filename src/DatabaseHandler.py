import sqlite3
import json
from typing import Dict
from datetime import datetime, timedelta
from appdirs import user_data_dir
from qtpy.QtCore import QSettings, QObject, Signal
import os
from hashlib import sha256
from pathlib import Path

from src.CryptoHelper import CryptoHelper

class DatabaseHandler(QObject):
    """Handles database operations for the application including connection management,
    table creation, and user-related CRUD operations.
    
    Attributes:
        db_initialized (Signal): Qt signal emitted when database initialization succeeds or fails.
    """
    
    dbInitialized = Signal(bool)
    loginSuccessful = Signal(str)
    loginFailed = Signal(str)
    passwordUpdateSuccess = Signal(str)
    passwordUpdateFailed = Signal(str)

    vaultItemSaved = Signal(dict)
    vaultItemError = Signal(str) 
    vaultItemsLoaded = Signal(list)
    vaultItemDeleted = Signal(int)

    def __init__(self, app_name="TrustedIn", parent=None):
        """Initialize the database handler with application name and parent.
        
        Args:
            app_name (str): Name of the application. Defaults to "TrustedIn".
            parent (QObject): Parent object for Qt hierarchy. Defaults to None.
        """
        super().__init__(parent)
        self.app_name = app_name
        self.app_author = "Spinn"
        self.settings = QSettings()
        
        # Initialize without connecting to a specific DB yet
        self.data_dir = user_data_dir(self.app_name, self.app_author)
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Will be set when user logs in/registers
        self.db_path = None  
        self.conn = None
        self.cursor = None
        
        self.crypto = CryptoHelper()

    def initialize_user_db(self, email):
        """Initialize or connect to a user-specific database"""
        # Create a safe filename from email
        db_name = self._email_to_dbname(email)
        self.db_path = os.path.join(self.data_dir, db_name)
        
        self._connect()
        self._createTables()
    
    def _email_to_dbname(self, email):
        """Convert email to a safe db filename"""
        # Hash the email to get consistent length and avoid special chars
        email_hash = sha256(email.encode()).hexdigest()
        return f"trustedin_{email_hash}.db"
    
    def _connect(self):
        """Establish connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"[DB ERROR] Could not connect: {e}")
            self.dbInitialized.emit(False)
        else:
            self.dbInitialized.emit(True)

    def _createTables(self):
        """Create necessary database tables if they don't exist."""
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            # Add vault items table
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vault_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_email TEXT NOT NULL,
                item_type TEXT NOT NULL,
                item_name TEXT NOT NULL,
                item_data TEXT NOT NULL, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_email) REFERENCES users(email) ON DELETE CASCADE
            )
            """)

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"[DB ERROR] Could not create tables: {e}")


    # --- Public CRUD Methods ---

    def registerUser(self, first_name, last_name, email, password_hash):
        """Register a new user in the database.

        Args:
            first_name (str): User's first name.
            last_name (str): User's last name.
            email (str): User's email address.
            password_hash (str): Hashed password for the user.

        Returns:
            bool: True if registration succeeded, False if user already exists.
        """
        if self.userExists(email):
            self.loginFailed.emit("User already exists")
            return False

        try:
            self.cursor.execute("""
                INSERT INTO users (first_name, last_name, email, password_hash)
                VALUES (?, ?, ?, ?)
            """, (first_name, last_name, email, password_hash))
            self.conn.commit()
            self.loginSuccessful.emit("You have registered successfully!")
            return True
        except sqlite3.IntegrityError:
            self.loginFailed.emit("Error registering user!")
            return False


    def getUserHash(self, email):
        """Retrieve password hash for a given user email.
        
        Args:
            email (str): Email address of the user.
            
        Returns:
            str: Password hash if user exists, None otherwise.
        """
        self.cursor.execute("""
            SELECT password_hash FROM users WHERE email = ?
        """, (email,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def userExists(self, email):
        """Check if a user with given email exists in the database.
        
        Args:
            email (str): Email address to check.
            
        Returns:
            bool: True if user exists, False otherwise.
        """
        self.cursor.execute("""
            SELECT 1 FROM users WHERE email = ?
        """, (email,))
        return self.cursor.fetchone() is not None
    
    def loginUser(self, email, password_hash):
        """Attempt to log in a user with provided credentials.
        
        Args:
            email (str): User's email address.
            password_hash (str): Hashed password to verify.
            
        Returns:
            bool: True if login succeeded, False otherwise.
        """
        if not self.userExists(email):
            self.loginFailed.emit("User does not exist")
            return False
        
        stored_hash = self.getUserHash(email)
        if stored_hash != password_hash:
            self.loginFailed.emit("Incorrect password")
            return False
        
        self.loginSuccessful.emit("Successfully logged in.")
        return True

    def getUserByEmail(self, email):
        """
        Fetch user details by email.

        Returns:
            tuple: (first_name, last_name, email, password_hash) or None if not found
        """
        self.cursor.execute("""
            SELECT first_name, last_name, email, password_hash FROM users WHERE email = ?
        """, (email,))
        return self.cursor.fetchone()

    def updatePassword(self, email, new_password_hash):
        """Update the password for an existing user.
        
        Args:
            email (str): User's email address
            new_password_hash (str): New hashed password
            
        Returns:
            bool: True if update succeeded, False otherwise
        """
        if not self.userExists(email):
            self.passwordUpdateFailed.emit("User does not exist")
            return False
        
        try:
            self.cursor.execute("""
                UPDATE users 
                SET password_hash = ?
                WHERE email = ?
            """, (new_password_hash, email))
            self.conn.commit()
            self.passwordUpdateSuccess.emit("Password updated successfully")
            return True
        except sqlite3.Error as e:
            error_msg = f"Failed to update password: {e}"
            print(f"[DB ERROR] {error_msg}")
            self.passwordUpdateFailed.emit(error_msg)
            return False

    def saveVaultItem(self, user_email: str, item_data: dict, password: str, skip_emit: bool = False) -> bool:
        """Save a vault item to the database"""
        try:
            # Encrypt the item data before saving
            item_json = self.crypto.encryptData(item_data, password, user_email) 
            
            self.cursor.execute("""
                INSERT INTO vault_items 
                (user_email, item_type, item_name, item_data)
                VALUES (?, ?, ?, ?)
            """, (
                user_email,
                item_data['type'],
                item_data['name'],
                item_json
            ))
            self.conn.commit()
            
            # Get the inserted ID
            item_id = self.cursor.lastrowid
            result = {
                'success': True,
                'item_id': item_id,
                'item_data': item_data
            }
            
            if not skip_emit:
                self.vaultItemSaved.emit(result)
            return True
            
        except sqlite3.Error as e:
            error_msg = f"Database error saving vault item: {e}"
            print(f"[DB ERROR] {error_msg}")
            if not skip_emit:
                self.vaultItemError.emit(error_msg)
            return False
    
    def loadVaultItems(self, user_email: str, password: str):
        """Load all vault items for a user"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT id, item_type, item_name, item_data, created_at, updated_at
                FROM vault_items
                WHERE user_email = ?
                ORDER BY updated_at DESC
            """, (user_email,))
            
            items = []
            for row in cursor.fetchall():
                try:
                    # Decrypt the item data
                    item_data = self.crypto.decryptData(row[3], password, user_email)  # Changed to use decrypted data

                    items.append({
                        'id': row[0],
                        'type': row[1],
                        'name': row[2],
                        'data': item_data,
                        'created_at': row[4],
                        'updated_at': row[5]
                    })
                except json.JSONDecodeError as e:
                    print(f"[DB WARNING] Corrupted item data for ID {row[0]}: {e}")
                    continue
                    
            self.vaultItemsLoaded.emit(items)
            return True
            
        except sqlite3.Error as e:
            error_msg = f"Database error loading vault items: {e}"
            print(f"[DB ERROR] {error_msg}")
            self.vaultItemError.emit(error_msg)
            return False
    
    def updateVaultItem(self, item_id: int, user_email: str, item_data: dict, password: str) -> bool:
        """Update an existing vault item in the database.
        
        Args:
            item_id: ID of the item to update
            user_email: Email of the user who owns the item
            item_data: Dictionary containing the updated item data
            password: User password for encryption
        """
        try:
            # Encrypt the item data before saving
            item_json = self.crypto.encryptData(item_data, password, user_email)  # Changed to use encrypted data
            
            self.cursor.execute("""
                UPDATE vault_items 
                SET item_type = ?,
                    item_name = ?,
                    item_data = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = ? AND user_email = ?
            """, (
                item_data['type'],
                item_data['name'],
                item_json,
                item_id,
                user_email
            ))
            
            if self.cursor.rowcount == 0:
                self.vaultItemError.emit("Item not found or not owned by user")
                return False
                
            self.conn.commit()
            
            # Return the updated item (decrypted)
            updated_item = {
                'id': item_id,
                'type': item_data['type'],
                'name': item_data['name'],
                'data': item_data,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            self.vaultItemSaved.emit(updated_item)
            return True
            
        except sqlite3.Error as e:
            error_msg = f"Database error updating vault item: {e}"
            print(f"[DB ERROR] {error_msg}")
            self.vaultItemError.emit(error_msg)
            return False
    
    def deleteVaultItem(self, item_id: int, user_email: str) -> bool:
        """Delete a vault item from the database.
        
        Args:
            item_id: ID of the item to delete
            user_email: Email of the user who owns the item
            
        Returns:
            bool: True if deletion succeeded, False otherwise
        """
        try:
            self.cursor.execute("""
                DELETE FROM vault_items
                WHERE id = ? AND user_email = ?
            """, (item_id, user_email))
            
            if self.cursor.rowcount == 0:
                # No rows were deleted (item not found or not owned by user)
                self.vaultItemError.emit("Item not found or not owned by user")
                return False
                
            self.conn.commit()
            self.vaultItemDeleted.emit(item_id)
            return True
            
        except sqlite3.Error as e:
            error_msg = f"Database error deleting vault item: {e}"
            print(f"[DB ERROR] {error_msg}")
            self.vaultItemError.emit(error_msg)
            return False
    
    def updateUsername(self, email: str, new_first_name: str, new_last_name: str) -> bool:
        """Update user's first and last name"""
        try:
            self.cursor.execute("""
                UPDATE users 
                SET first_name = ?, last_name = ?
                WHERE email = ?
            """, (new_first_name, new_last_name, email))
            
            if self.cursor.rowcount == 0:
                return False
                
            self.conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to update username: {e}")
            return False

    def deleteUserAccount(self, email: str) -> bool:
        """Delete user account and all associated data"""
        try:
            # Delete all user's vault items first (due to foreign key constraint)
            self.cursor.execute("DELETE FROM vault_items WHERE user_email = ?", (email,))
            
            # Then delete the user
            self.cursor.execute("DELETE FROM users WHERE email = ?", (email,))
            
            self.conn.commit()
            
            # Reset the entire database
            self.deleteDatabase(email)
            self._createTables()
            
            return True
            
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to delete account: {e}")
            return False

    def scanSecurity(self, user_email: str, password: str) -> dict:  # Added password parameter
        """
        Scan the vault for security issues.
        """
        weak = 0
        reused = 0
        old = 0
        breaches = 0

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT item_data, created_at FROM vault_items
                WHERE user_email = ? AND item_type = 'Passwords'
            """, (user_email,))
        
            seen_passwords = {}
            six_months_ago = datetime.now() - timedelta(days=180)

            for row in cursor.fetchall():
                try:
                    # Decrypt the item data first
                    decrypted_data = self.crypto.decryptData(row[0], password, user_email)
                    password_text = decrypted_data.get('password', '')
                    created_at = datetime.fromisoformat(row[1]) if 'T' in row[1] else datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')

                    # Weak password
                    if len(password_text) < 8:
                        weak += 1

                    # Reused passwords
                    if password_text in seen_passwords:
                        reused += 1
                    else:
                        seen_passwords[password_text] = 1

                    # Old passwords
                    if created_at < six_months_ago:
                        old += 1

                except Exception as e:
                    print(f"[SCAN ERROR] Skipping item: {e}")
            
            return {
                "weak_passwords": weak,
                "reused_passwords": reused,
                "old_passwords": old,
                "breach_count": breaches,
                "vault_score": self._calculateVaultScore(weak, reused, old)
            }
        except sqlite3.Error as e:
            print(f"[DB ERROR] Security scan failed: {e}")
            return {
                "weak_passwords": 0,
                "reused_passwords": 0,
                "old_passwords": 0,
                "breach_count": 0,
                "vault_score": 0
            }

    def _calculateVaultScore(self, weak, reused, old):
        """Simple scoring logic"""
        penalties = (weak * 2 + reused * 2 + old)
        score = max(0, 100 - penalties)
        return min(score, 100)

    def countItemTypes(self, user_email: str) -> Dict[str, int]:
        """Count the number of items of each type in the user's vault.
        
        Args:
            user_email: Email of the user whose items should be counted
            
        Returns:
            A dictionary with item types as keys and counts as values.
            Always includes all known item types (defaulting to 0 if none exist).
        """
        # Initialize with all known types set to 0
        default_counts = {
            "Passwords": 0,
            "Contacts": 0,
            "Notes": 0,
            "Payment Cards": 0
        }

        try:
            # Use a fresh cursor for thread safety
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("""
                    SELECT item_type, COUNT(*) FROM vault_items
                    WHERE user_email = ?
                    GROUP BY item_type
                """, (user_email,))
                
                # Update counts from the database results
                for item_type, count in cursor.fetchall():
                    if item_type in default_counts:
                        default_counts[item_type] = count
                
                print(f"[DEBUG] Vault Item Counts: {default_counts}")
                return default_counts
                
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to count item types: {e}")
            return default_counts
        
    def getPasswordStats(self, user_email: str) -> dict:
        """Get password statistics for a user"""
        stats = {
            'weak_passwords': [],
            'reused_passwords': [],
            'old_passwords': []
        }
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT id, item_data, created_at FROM vault_items
                WHERE user_email = ? AND item_type = 'Passwords'
            """, (user_email,))
            
            password_counts = {}
            six_months_ago = datetime.now() - timedelta(days=180)
            
            for row in cursor.fetchall():
                try:
                    item = json.loads(row[1])
                    password = item.get('password', '')
                    item_id = row[0]
                    created_at = datetime.fromisoformat(row[2]) if 'T' in row[2] else datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                    
                    # Check for weak password
                    if len(password) < 8:
                        stats['weak_passwords'].append(item_id)
                    
                    # Track password reuse
                    if password in password_counts:
                        password_counts[password].append(item_id)
                    else:
                        password_counts[password] = [item_id]
                    
                    # Check for old password
                    if created_at < six_months_ago:
                        stats['old_passwords'].append(item_id)
                        
                except Exception as e:
                    print(f"[PasswordStats] Error processing item {row[0]}: {e}")
            
            # Identify reused passwords (used more than once)
            for password, ids in password_counts.items():
                if len(ids) > 1:
                    stats['reused_passwords'].extend(ids)
                    
            return stats
            
        except sqlite3.Error as e:
            print(f"[DB ERROR] Password stats failed: {e}")
            return stats

    def getAllVaultItems(self, user_email: str, password: str):
        """Get all vault items for export - returns decrypted data"""
        try:
            self.cursor.execute("""
                SELECT id, item_type, item_name, item_data, created_at, updated_at
                FROM vault_items
                WHERE user_email = ?
                ORDER BY updated_at DESC
            """, (user_email,))
            
            items = []
            for row in self.cursor.fetchall():
                try:
                    # Decrypt the item data
                    item_data = self.crypto.decryptData(row[3], password, user_email)
                    items.append({
                        'id': row[0],
                        'type': row[1],
                        'name': row[2],
                        'data': item_data,  # Decrypted data
                        'created_at': row[4],
                        'updated_at': row[5]
                    })
                except Exception as e:
                    print(f"[DB WARNING] Failed to decrypt item ID {row[0]}: {e}")
                    continue
            return items
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to get vault items: {e}")
            raise Exception("Database error retrieving vault items")
        
    def deleteAllVaultItems(self, user_email):
        """Delete all vault items for a user"""
        try:
            settings = QSettings()
            method = settings.setValue(f"{user_email}/security/encryption", "")
            with self.conn:
                self.cursor.execute("""
                    DELETE FROM vault_items 
                    WHERE user_email = ?
                """, (user_email,))
                
                if self.cursor.rowcount > 0:
                    print(f"[VAULT RESET] Deleted {self.cursor.rowcount} items for {user_email}")
                else:
                    print(f"[VAULT RESET] No items found for {user_email}")
                    
                return True
                
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to reset vault: {e}")
            return False
    
    def vaultItemExists(self, user_email: str, item_id: int) -> bool:
        """Check if a vault item exists for the user"""
        try:
            self.cursor.execute("""
                SELECT 1 FROM vault_items 
                WHERE id = ? AND user_email = ?
            """, (item_id, user_email))
            return self.cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to check item existence: {e}")
            return False
    
    def getVaultItemById(self, user_email: str, item_id: int, password) -> dict:
        """Get a vault item by ID for the specified user"""
        try:
            self.cursor.execute("""
                SELECT id, item_type, item_name, item_data 
                FROM vault_items 
                WHERE id = ? AND user_email = ?
            """, (item_id, user_email))
            
            row = self.cursor.fetchone()
            if row:
                item_data = self.crypto.decryptData(row[3], password, user_email)
                return {
                    'id': row[0],
                    'type': row[1],
                    'name': row[2],
                    'data': item_data  
                }
            return None
            
        except sqlite3.Error as e:
            print(f"[DB ERROR] Failed to get vault item: {e}")
            return None
    
    def generateSecurityReport(self, user_email: str, password: str) -> dict:
        """Generate comprehensive security audit report"""
        result = self.scanSecurity(user_email, password)
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'user': user_email,
            'scan_results': result,
            'item_stats': self.countItemTypes(user_email),
            'password_stats': self.getPasswordStats(user_email),
            'vault_score': result['vault_score']
        }
        return report_data

    def close(self):
        """Close the database connection if it exists."""
        if self.conn:
            self.conn.close()
    
    def deleteDatabase(self, user_email):
        """Delete the SQLite database file and close the connection."""
        try:
            settings = QSettings()
            method = settings.setValue(f"{user_email}/security/encryption", "")
            if self.conn:
                self.conn.close()
                self.conn = None
                self.cursor = None

            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                print("[DB INFO] Database deleted successfully.")
                return True
            else:
                print("[DB INFO] No database file found to delete.")
                return False
            
        except Exception as e:
            print(f"[DB ERROR] Failed to delete database: {e}")
            return False