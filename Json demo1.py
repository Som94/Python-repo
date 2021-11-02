#Json_demo.py

 

import json

x =  '{ "name":"Kiran Kumar", "age":30,     "city":"New Delhi"}'

y = json.loads(x)

print (y["age"])

print ('---Dictionary to JSON ---')

 

x = {

  "name": "Shankar",

  "age": 23,

  "city": "Blore"

}

 

# convert into JSON:

y = json.dumps(x)

 

# the result is a JSON string:

print('watch ',y)

 

print ('---other data structures and objects to JSON ---')

print(json.dumps({"name": "Divakar", "age": 23}))

print(json.dumps(["pineapple", "grapes"]))

print(json.dumps(("mango", "cherries")))

print(json.dumps("hello"))

print(json.dumps(42))

print(json.dumps(31.76))

print(json.dumps(True))

print(json.dumps(False))

print(json.dumps(None))

print ('-------------WATCH complex data set -----------------')

 

class address:

    def __init__(self,city,pin):

        self.city = city

        self.pin = pin

    def disp(self):

        print ('City is ',self.city,' PIN CODE is ',self.pin)

 

 

ad = address ('Pune', 452000)       

 

citizen = {

  "name": "Anand",

  "age": 30,

  "married": True,

  "divorced": False,

  "children": ("Mohan","Radha"),

  "pets": None,

  "cars": [

    {"model": "Honda City", "mpg": 27.5},

    {"model": "Ford Edge", "mpg": 24.1}

  ],

#  "residence" : ad

}

 

try:

    print('BLUNT output ', json.dumps(citizen))

    print ('------')

    print('PLEASANT output \n', json.dumps(citizen, indent=4,separators=(". ", " = "),sort_keys=True))

#TypeError: Object of type address is not JSON serializable   

except TypeError:

    print ('object cannont be part for dump activity ') 

    