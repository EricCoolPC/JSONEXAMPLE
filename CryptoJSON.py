import json
from cryptography.fernet import Fernet

def Encyrpt_Json(fileName):
    key = Fernet.generate_key()
    with open(fileName, 'rb') as f:
        data = f.read()

    CreateKey(key, data)

def Decyrpt_Json(fileName):
    with open(fileName, 'rb') as f:
        data = f.read()
        jsonContent = data.decode('utf-8')
    print(jsonContent)
    return jsonContent

def CreateKey(filename, k, d):
    fernet = Fernet(k)
    encrypted = fernet.encrypt(d)

    with open('key.key', 'wb') as f:
        f.write(k)
    with open(filename, 'rb') as f:
        

def ReadKey(k):
    with open(k, 'rb') as f:
        key = f.read()
    return key