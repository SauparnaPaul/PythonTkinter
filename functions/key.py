'''
Created on 12-Jul-2020

@author: Cabin
'''

from cryptography.fernet import Fernet
import os

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return "i1UcmtqmIOxgEcN_m-f0dBZoFruHxUAS4Z4aD80P9zY="
    #return open("D:/DigitalWorkHome/python_projects/EncryptorDecryptor/key.key", "rb").read()

