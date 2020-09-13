from cryptography.fernet import Fernet

def decrypt(filename, key):
    encryptionChecker=b'DeltaRelease.0.1'
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        encrypted_data=encrypted_data[len(encryptionChecker):]
    return f.decrypt(encrypted_data)