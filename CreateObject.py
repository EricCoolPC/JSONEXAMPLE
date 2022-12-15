import json
import CryptoJSON as cj

fileName = "Example.json"

jsonData = cj.Decyrpt_Json(fileName)

key = cj.ReadKey('key.key')

jsonData = cj.Decyrpt_Json()

Obj = json.load(jsonData)

#print(Obj)
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