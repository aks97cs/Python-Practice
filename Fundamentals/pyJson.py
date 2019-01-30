'''
    @created By: Anuj Kumar Singh
    @ Working with Jason in python

'''
import json 
#writing json string 
x = '{"Name":"Anuj","Age":21}'
#loading Json
y = json.loads(x)
print(y['Name'])

'''
    Converting python object into json using json.dumps()
'''
data = {
    "Name":"Anuj",
    "Roll_no":1507710017,
    "Course":"B.tech"
}
# data = [1,2,3]
y = json.dumps(data)
print(y)


# Examples 
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#formating result

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
