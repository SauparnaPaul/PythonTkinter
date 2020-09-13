from cryptography.fernet import Fernet
import os
def encrypt(filename, key):
    encryptionChecker=b'DeltaRelease.0.1'
    f = Fernet(key)
    with open(filename, "rb") as file:
       file_data = file.read()
       if file_data[:len(encryptionChecker)] != encryptionChecker:
            #raise ValueError('Not an encrypted file')
            
            encrypted_data = f.encrypt(file_data)
            # write the encrypted file
            
            #testing different format
            #with open(filename, "wb") as file:
            with open(os.path.splitext(filename)[0]+".delta", "wb") as file:
                file.write(encryptionChecker)  # write the identifier.
                file.write(encrypted_data)
       else:
           print("Already encrypted")
           pass     
    