import json

class Example():
    def __init__(self, name, string1, string2, num1, num2, num3, bool, tup, lis, dict) -> None:
        self.name = name
        self.string1 = string1
        self.string2 = string2

        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.bool = bool

        self.tup = tup
        self.lis = lis

        self.dict = dict
    
example1 = Example("Name", "words", "Yeah", 1, 100, 50, False, ("tuple1", 2, False), ["list1", 3, True], {"Key1": "dict1", "Key2": 1,"Key3": True})

jsonStr = json.dumps(example1.__dict__, indent=3)

print(jsonStr)

f = open("Example.json", "w")
f.write(jsonStr)
f.close()