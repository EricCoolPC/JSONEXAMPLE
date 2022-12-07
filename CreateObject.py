import json

f = open("Example.json", "r")

Obj = json.load(f)

f.close()

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