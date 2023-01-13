import json
from cryptography.fernet import Fernet
import CryptoJSON as cj

fileName = "Example.json"

key = cj.ReadKey('key.key')
encryption = cj.GetEncryption(fileName)

jsonData = cj.Decyrpt_Json(Fernet(key), encryption)

with open("Example3.json", 'w') as f:
    f.write(jsonData)
    f.close()

Obj = json.loads(jsonData)

t = type(Obj)
print(t)

for key, e in Obj.items():
    print(key)
    print(e)
    print(type(e))
    if(type(e) == dict):
            print("dictionary within a dictionary")
            for keyy, ee in e.items():
                print(keyy)
                print(ee)