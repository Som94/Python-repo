# -*- coding: utf-8 -*-
"""
Given a dict1 = {1000: (10,20,30,40) , 2000 : (12,500,67), 3000 : (91,190,291,6,5,33)
dict2 =  {1000: True, 2000: False, 3000: True}

Write functions to do the following

 

display()  - on passing of the key it should display the values,
 if the key does not exists – it should display ‘no such key’

 

displayAll()  - display all the values from dict1 if the status of
 the key is True only (in dict2)
"""


dict1 = {1000: (10,20,30,40) , 2000 : (12,500,67), 3000 : (91,190,291,6,5,33)}
dict2 =  {1000: True, 2000: False, 3000: True}

def display(key):
    
    try:
    #if key in dict1.keys():
        print(dict1[key])
    except KeyError:
    #else:
        print("no such key")
    
key=int(input("Enter the key value :"))

display(key)

def displayAll(key):
    try:
    #if key in dict1.keys():
        if dict2[key]==True:
            
            print(dict1[key])
        else:
            print("dict2 key value is False..")
    except KeyError:
    #else:
        print("no such key")
    
key=int(input("Enter the key value :"))

displayAll(key)