import json
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

from Custom_Widgets.WidgetsWorker import Worker, WorkerResponse
from qtpy.QtCore import QCoreApplication, QSettings, QThreadPool

from src.Auth import Auth
from src.DatabaseHandler import DatabaseHandler
class BackendWorker:
    def __init__(self, GuiFunctions):
        self.guiFunc = GuiFunctions #for updating GUI

        self.app = QCoreApplication.instance()
        if self.app is None:
            self.app = QCoreApplication([])
        self.app.aboutToQuit.connect(self.backendWorkerStopper)

        # START THREAD
        self.backendWorkerThreadpool = QThreadPool()
        self.backendWorkerThreadpool.setMaxThreadCount(5)  # Limit concurrency

        self.dbHandler = DatabaseHandler() 

        # start threads
        self.start()
             
    def start(self):
        self.initDatabaseWorker()
        self.initAuthWorker()
    
    def initDatabaseWorker(self):
        """
        Initializes the database in a worker thread.
        """
        self.dbHandler.loginSuccessful.connect(self.guiFunc.handleLoginSuccessful)
        self.dbHandler.loginFailed.connect(self.guiFunc.handleLoginFailed)
        self.dbHandler.passwordUpdateSuccess.connect(self.guiFunc.handlePasswordUpdateSuccess)
        self.dbHandler.passwordUpdateFailed.connect(self.guiFunc.handlePasswordUpdateFailed)
        self.dbHandler.vaultItemSaved.connect(self.guiFunc.handleVaultItemSaved)
        self.dbHandler.vaultItemError.connect(self.guiFunc.handleVaultItemError)
        self.dbHandler.vaultItemsLoaded.connect(self.guiFunc.handleVaultItemsLoaded)
        self.dbHandler.vaultItemDeleted.connect(self.guiFunc.handleVaultItemDeleted)
    
    def getPassword(self):
        if self.password is None or self.password == "":
            raise ValueError("Encryption Password is not set or is empty.")
        return self.password

    def initAuthWorker(self):
        """
        Initialize the Auth instance and connect its signals to GUI handlers.
        """
        self.auth = Auth()

        # Connect Auth signals to GUI function handlers
        self.auth.resendVerificationEmailFinished.connect(self.guiFunc.handleResendVerificationEmailFinished)
        self.auth.verifyEmailFinished.connect(self.guiFunc.handleVerifyEmailFinished)
        self.auth.uploadUserFinished.connect(self.guiFunc.handleUserUploadFinished)
        
    def registerUserWorker(self, firstName, lastName, email, passwordHash):
        worker = Worker(
            lambda progress_callback: self.startRegisterUserWorker(
                progress_callback, firstName, lastName, email, passwordHash
            )
        )
        self.backendWorkerThreadpool.start(worker)

    def startRegisterUserWorker(self, progress_callback, firstName, lastName, email, passwordHash):
        self.dbHandler.initialize_user_db(email)
        self.dbHandler.registerUser(firstName, lastName, email, passwordHash)


    def loginUserWorker(self, email, passwordHash):
        worker = Worker(lambda progress_callback: self.startLoginUserWorker(progress_callback, email, passwordHash))
        self.backendWorkerThreadpool.start(worker)

    def startLoginUserWorker(self, progress_callback, email, passwordHash):
        self.password = passwordHash
        # Initialize user-specific DB before login
        self.dbHandler.initialize_user_db(email)
        self.dbHandler.loginUser(email, passwordHash)

    def isValidToken(self, token):
        return True
    
    def updatePasswordWorker(self, email, new_password_hash):
        worker = Worker(lambda progress_callback: 
            self.startUpdatePasswordWorker(progress_callback, email, new_password_hash))
        self.backendWorkerThreadpool.start(worker)

    def startUpdatePasswordWorker(self, progress_callback, email, new_password_hash):
        self.dbHandler.updatePassword(email, new_password_hash)
    
    def uploadUserDetailsWorker(self, email):
        """
        Worker method to fetch user details from local DB and upload to remote server.
        """
        worker = Worker(lambda progress_callback: self.startUploadUserDetailsWorker(progress_callback, email))
        self.backendWorkerThreadpool.start(worker)

    def startUploadUserDetailsWorker(self, progress_callback, email):
        # Get user details from DB
        user_data = self.dbHandler.getUserByEmail(email)
        if not user_data:
            print(f"[UploadUser] User {email} not found in local DB.")
            return
        
        first_name, last_name, email, password_hash = user_data

        # Call Auth.uploadUser to upload details to remote backend
        response = self.auth.uploadUser(first_name, last_name, email, password_hash)

        if response.get("success"):
            print(f"[UploadUser] User {email} uploaded successfully.")
        else:
            error_msg = response.get("upload_user_response") or response.get("error") or "Unknown error"
            print(f"[UploadUser] Upload failed: {error_msg}")
    
    def resendVerificationEmailWorker(self, email):
        """
        Worker method to resend the verification email.
        """
        worker = Worker(lambda progress_callback: self.startResendVerificationEmailWorker(progress_callback, email))
        self.backendWorkerThreadpool.start(worker)

    def startResendVerificationEmailWorker(self, progress_callback, email):
        """
        Worker function to call Auth.resendVerificationEmail and handle the result.
        """
        response = self.auth.resendVerificationEmail(email)
        print(response)
        if response.get("success"):
            print(f"[ResendVerificationEmail] Verification email resent successfully to {email}.")
        else:
            error_msg = response.get("resend_verification_email_response") or response.get("error") or "Unknown error"
            print(f"[ResendVerificationEmail] Failed to resend verification email to {email}: {error_msg}")


    def verifyEmailWorker(self, email, token):
        """
        Worker method to verify a user's email with token.
        """
        worker = Worker(lambda progress_callback: self.startVerifyEmailWorker(progress_callback, email, token))
        self.backendWorkerThreadpool.start(worker)

    def startVerifyEmailWorker(self, progress_callback, email, token):
        """
        Worker function to call Auth.verifyEmail and handle the result.
        """
        response = self.auth.verifyEmail(email, token)
        if response.get("success"):
            print(f"[VerifyEmail] Email {email} verified successfully.")
        else:
            error_msg = response.get("verify_email_response") or response.get("error") or "Unknown error"
            print(f"[VerifyEmail] Failed to verify email {email}: {error_msg}")

    def saveVaultItemWorker(self, user_email: str, item_data: dict):
        """Worker method to save vault item"""
        worker = Worker(
            lambda progress_callback: self.startSaveVaultItemWorker(
                progress_callback, user_email, item_data
            )
        )
        self.backendWorkerThreadpool.start(worker)

    def startSaveVaultItemWorker(self, progress_callback, user_email: str, item_data: dict):
        """Worker function that saves item."""
        self.dbHandler.saveVaultItem(user_email, item_data, self.getPassword())

    def loadVaultItemsWorker(self, user_email: str):
        """Worker method to load vault items"""
        worker = Worker(
            lambda progress_callback: self.startLoadVaultItemsWorker(
                progress_callback, user_email
            )
        )
        self.backendWorkerThreadpool.start(worker)

    def startLoadVaultItemsWorker(self, progress_callback, user_email: str):
        """Worker function to load vault items"""
        self.dbHandler.loadVaultItems(user_email, self.getPassword())

    def updateVaultItemWorker(self, item_id, user_email, item_data):
        """Worker method to update vault item"""
        worker = Worker(
            lambda progress_callback: self.startUpdateVaultItemWorker(
                progress_callback, item_id, user_email, item_data
            )
        )
        self.backendWorkerThreadpool.start(worker)

    def startUpdateVaultItemWorker(self, progress_callback, item_id, user_email, item_data):
        """Worker function to update vault item"""
        self.dbHandler.updateVaultItem(item_id, user_email, item_data, self.getPassword())
    
    def deleteVaultItemWorker(self, item_id, user_email):
        """Worker method to delete vault item both locally and online"""
        worker = Worker(
            lambda progress_callback: self.startDeleteVaultItemWorker(
                progress_callback, item_id, user_email
            )
        )
        self.backendWorkerThreadpool.start(worker)

    def startDeleteVaultItemWorker(self, progress_callback, item_id, user_email):
        """Worker function to delete vault item both locally and online"""
        try:
            # First get the item data
            item_data = self.dbHandler.getVaultItemById(user_email, item_id, self.getPassword())
            if not item_data:
                print(f"[DELETE ERROR] Item {item_id} not found")
                return False
                
            # First delete locally
            local_success = self.dbHandler.deleteVaultItem(item_id, user_email)
            
            if local_success:
                # Then delete from server using multiple identifying fields
                result = self.auth.deleteVaultItem(user_email, {
                    'type': item_data['type'],
                    'name': item_data['name'],
                    'data': item_data['data']
                })
                
                if not result.get('success'):
                    print(f"[DELETE ERROR] Failed to delete item from server: {result.get('message')}")
                    # You may want to handle the case where local delete succeeds but server delete fails
                    # For now, we'll just log it since the local delete already happened
            else:
                print(f"[DELETE ERROR] Failed to delete item {item_id} locally")
                
        except Exception as e:
            print(f"[DELETE ERROR] Error during deletion: {e}")

    def updateUsernameWorker(self, email, new_first_name, new_last_name):
        worker = Worker(
            lambda progress_callback: self.startUpdateUsernameWorker(
                progress_callback, email, new_first_name, new_last_name
            )
        )
        worker.signals.result.connect(lambda: print("Username updated successfully"))
        worker.signals.error.connect(lambda e: print(f"Error updating username: {e}"))
        self.backendWorkerThreadpool.start(worker)

    def startUpdateUsernameWorker(self, progress_callback, email, new_first_name, new_last_name):
        return self.dbHandler.updateUsername(email, new_first_name, new_last_name)

    def deleteAccountWorker(self, email):
        worker = Worker(
            lambda progress_callback: self.startDeleteAccountWorker(progress_callback, email)
        )
        worker.signals.result.connect(self.handleAccountDeleted)
        worker.signals.error.connect(lambda e: print(f"Error deleting account: {e}"))
        self.backendWorkerThreadpool.start(worker)

    def startDeleteAccountWorker(self, progress_callback, email):
        return self.dbHandler.deleteUserAccount(email)

    def handleAccountDeleted(self):
        # Emit signal to GUI to reset the application
        self.guiFunc.accountDeleted.emit()
    
    def scanVaultSecurityWorker(self, email):
        worker = Worker(lambda progress_callback: self.startScanVaultSecurityWorker(progress_callback, email))
        worker.signals.result.connect(self.guiFunc.handleVaultSecurityScanResult)
        self.backendWorkerThreadpool.start(worker)

    def startScanVaultSecurityWorker(self, progress_callback, email):
        return self.dbHandler.scanSecurity(email, self.getPassword())

    def loadVaultItemStatsWorker(self, email):
        worker = Worker(lambda progress_callback: self.startLoadVaultItemStatsWorker(progress_callback, email))
        worker.signals.result.connect(self.guiFunc.handleVaultItemStatsResult)
        self.backendWorkerThreadpool.start(worker)
    
    def startLoadVaultItemStatsWorker(self, progress_callback, email):
        return self.dbHandler.countItemTypes(email)

    def getPasswordStatsWorker(self, email):
        worker = Worker(lambda progress_callback: self.startGetPasswordStatsWorker(progress_callback, email))
        worker.signals.result.connect(self.guiFunc.handlePasswordStatsResult)
        self.backendWorkerThreadpool.start(worker)

    def startGetPasswordStatsWorker(self, progress_callback, email):
        return self.dbHandler.getPasswordStats(email)
    
    def syncVaultItemsWorker(self, email):
        """Worker method to perform two-way vault sync"""
        worker = Worker(
            lambda progress_callback: self.startSyncVaultItemsWorker(progress_callback, email))
        worker.signals.result.connect(self.guiFunc.handleVaultSyncResult)
        self.backendWorkerThreadpool.start(worker)

    def startSyncVaultItemsWorker(self, progress_callback, email):
        """Worker function for two-way item sync with proper encryption handling"""
        password = self.getPassword()
        upload_result = {}
        # First upload local items (decrypt before upload)
        try:
            local_items = self.dbHandler.getAllVaultItems(email, password)
            decrypted_items = []
            
            for item in local_items:
                try:
                    # Create a clean decrypted item for upload
                    decrypted_item = {
                        'id': item['id'],
                        'type': item['type'],
                        'name': item['name'],
                        'data': item['data'],  # This is already decrypted by getAllVaultItems
                        'created_at': item['created_at'],
                        'updated_at': item['updated_at']
                    }
                    decrypted_items.append(decrypted_item)
                except Exception as e:
                    print(f"[SYNC] Error preparing item {item.get('id')} for upload: {e}")
                    continue
            
            if decrypted_items:
                upload_result = self.auth.uploadVaultItems(email, decrypted_items)
                if upload_result.get('success'):
                    print(f"[SYNC] Uploaded {upload_result.get('uploaded', 0)} items")
                else:
                    print(f"[SYNC UPLOAD ERROR] {upload_result.get('message')}")
            else:
                print("[SYNC] No local items to upload")
                
        except Exception as e:
            print(f"[SYNC UPLOAD ERROR] Failed to prepare local items: {e}")
            upload_result = {'success': False, 'message': str(e)}
        
        server_items = []
        saved_count = 0
        # Then download server items (encrypt before local save)
        try:
            download_result = self.auth.downloadVaultItems(email)
            if download_result.get('success'):
                server_items = download_result.get('items', [])
                if server_items:
                    print(f"[SYNC] Retrieved {len(server_items)} items from server")
                    
                    saved_count = 0
                    for item in server_items:
                        try:
                            # Check if item exists locally
                            exists = self.dbHandler.vaultItemExists(email, item['id'])
                            if not exists:
                                # The item from server is decrypted - we need to encrypt it before local save
                                encrypted_data = {
                                    'type': item['type'],
                                    'name': item['name'],
                                    'data': item['data']  # This is the decrypted data from server
                                }
                                
                                # Save the item locally (will be encrypted in saveVaultItem)
                                self.dbHandler.saveVaultItem(
                                    email, 
                                    encrypted_data, 
                                    password,
                                    skip_emit=True
                                )
                                saved_count += 1
                        except Exception as e:
                            print(f"[SYNC ERROR] Failed to process item {item.get('id')}: {e}")
                    
                    print(f"[SYNC] Saved {saved_count} new items from server")
                else:
                    print("[SYNC] No items found on server")
            else:
                print(f"[SYNC DOWNLOAD ERROR] {download_result.get('message')}")
                
        except Exception as e:
            print(f"[SYNC DOWNLOAD ERROR] Failed to process server items: {e}")
            download_result = {'success': False, 'message': str(e)}
        
        # Return combined result
        return {
            'success': upload_result.get('success', False) and download_result.get('success', False),
            'uploaded': upload_result.get('uploaded', 0),
            'downloaded': len(server_items) if server_items else 0,
            'saved': saved_count,
            'message': (
                f"Sync complete. "
                f"Uploaded: {upload_result.get('uploaded', 0)}, "
                f"Downloaded: {len(server_items) if server_items else 0}, "
                f"Saved: {saved_count}"
            )
        }
    
    def generateSecurityReport(self, email: str):
        """Wrapper for report generation"""
        return self.dbHandler.generateSecurityReport(email, self.getPassword())
    
    def importVaultWorker(self, email, file_path, password):
        """Worker method to import vault data"""
        worker = Worker(
            lambda progress_callback: self.startImportVaultWorker(
                progress_callback, email, file_path, password
            )
        )
        worker.signals.result.connect(self.guiFunc.handleImportResult)
        worker.signals.error.connect(lambda e: print(f"Import error: {e}"))
        self.backendWorkerThreadpool.start(worker)

    def startImportVaultWorker(self, progress_callback, email, file_path, password):
        """Worker function to perform the import"""
        try:
            # 1. Read the encrypted file
            with open(file_path, 'r') as f:
                encrypted_package = json.load(f)
            
            # 2. Decode the base64 fields
            salt = base64.b64decode(encrypted_package['salt'])
            nonce = base64.b64decode(encrypted_package['nonce'])
            tag = base64.b64decode(encrypted_package['tag'])
            ciphertext = base64.b64decode(encrypted_package['ciphertext'])
            
            # 3. Derive the key
            key = scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1)
            
            # 4. Decrypt the data
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            json_data = cipher.decrypt_and_verify(ciphertext, tag)
            
            # 5. Parse the JSON
            import_data = json.loads(json_data.decode('utf-8'))
            
            # 6. Verify the email matches
            if import_data.get('email') != email:
                return {
                    'success': False,
                    'message': "Vault file is for a different user account"
                }
            
            # 7. Import each item
            imported_count = 0
            for item in import_data.get('items', []):
                try:
                    # Save the item (will be encrypted with current password)
                    self.dbHandler.saveVaultItem(
                        email,
                        {
                            'type': item['type'],
                            'name': item['name'],
                            'data': item['data']  # This is the decrypted data
                        },
                        self.getPassword(),
                        skip_emit=True
                    )
                    imported_count += 1
                except Exception as e:
                    print(f"[IMPORT] Failed to import item {item.get('id')}: {e}")
                    continue
            
            return {
                'success': True,
                'imported': imported_count,
                'total': len(import_data.get('items', [])),
                'message': f"Imported {imported_count} of {len(import_data.get('items', []))} items"
            }
            
        except json.JSONDecodeError:
            return {
                'success': False,
                'message': "Invalid vault file format"
            }
        except ValueError as e:
            return {
                'success': False,
                'message': f"Decryption failed - wrong password or corrupted file: {str(e)}"
            }
        except Exception as e:
            return {
                'success': False,
                'message': f"Import failed: {str(e)}"
            }

    # Try and stop background threads
    def backendWorkerStopper(self): 
        print("[BackendWorker] Cleaning up...")
        self.backendWorkerThreadpool.clear()
        self.backendWorkerThreadpool.waitForDone()