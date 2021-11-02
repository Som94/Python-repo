'''
Given to you dictionary
{10:100 , 12 : 35,  89: ‘1234’ , 99 : ‘56’ ,  110 : ‘A60’,  200: -45 , 350 : ‘75AB’ }

Display all the keys and values

Add all the values . convert the number to string and where the string starts with Alphabet fetch
the rest of string that you convert into integer for example in key 110  ‘A60’   ……’60’ …..convert it into
60  , 350 key the value does not start with alphabet – ignore it

 

Find the highest value

Find the lowest value

Find the average value

Find how many two digits number are there

Find how many THREE digits number are there
'''

from functools import *

dict1={10:100 , 12 : 35,  89: '1234' , 99 : '56' ,  110 : 'A60',  200: -45 , 350 : '75AB' }

#for key,value in dict1.items():
#    print(key,'=',value)
    
def dictionary():
    global key_list
    key_list=[]
    global value_list
    value_list=[]
    for key,value in dict1.items():
        key_list.append(key)
        value_list.append(value)
    print('Keys of dictinary are :',key_list)
    print('Values of dictinary are',value_list)
    
def total_of_values():
    global int_value_list
    int_value_list=[]
    st1=''
    for i in value_list:
        if type(i)==int:
            int_value_list.append(i)
        elif type(i)==str:
            for j in i:
                if j.isdigit():
                    st1=st1+j
            int_value_list.append(int(st1))      
        st1=''
    print('The eleminate alphabats from  dictionary values and make it list of integers :',int_value_list)
    
    add_values=reduce(lambda x,y: x+y,int_value_list )
    print("Addition of all values is :",add_values)
    
def Highest_value():
    highest=0
    for i in int_value_list:
        if i> highest:
            highest=i
    print("The Highest Value is :",highest)
    
def lowest_value():
    lowest=999999999
    for i in int_value_list:
        if i<lowest:
            lowest=i
    print("The Lowest Value is :",lowest)
  
def average_value():
    count=0
    sum1=0
    for i in int_value_list:
        sum1 += i
        count += 1
    print("The Average Value is :",sum1/count)
    
def two_digits():
    count=0
    for i in int_value_list:
        if i>9 and i<100:
            count += 1
    print("The two digit numbers are :",count)
   
def THREE_digits():
    count=0
    for i in int_value_list:
        if i>99 and i<1000:
            count += 1
    print("The Three digit numbers are :",count)
   

 
dictionary()
total_of_values()
Highest_value()
lowest_value()
average_value()
two_digits()
THREE_digits()