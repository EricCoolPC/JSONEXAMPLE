import json
from cryptography.fernet import Fernet

def Encyrpt_Json(fileName):
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)
    with open(fileName, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(fileName, 'wb') as f:
        f.write(encrypted)

def Decyrpt_Json(fer, enc):
    decrypted_var = fer.decrypt(enc)
    back2Json = decrypted_var.decode('utf-8')

    return back2Json

def ReadKey(k):
    with open(k, 'rb') as f:
        key = f.read()
    return key

def GetEncryption(e):
    with open(e, 'rb') as f:
        enc = f.read()
    return enc