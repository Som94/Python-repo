'''
if it is tuple then replace it with (99,100)
if it is list then replac it with  [199,200,201]
if it is set then replace it with  {499,500,501,502}
dict1 = {10: (56,77,88,90), 20 :[34,78,55,19] , 30 : {12,2,5} }   
'''
tuple1=(99,100)
list1=[199,200,201]
set1={499,500,501,502}

dict1 = {10: (56,77,88,90), 20 :[34,78,55,19] , 30 : {12,2,5} }   

num=int(input("Enter Any Number :"))
if num in dict1.keys():
    if num==10:
        dict1[num]=tuple1
    
    elif num == 20:
        dict1[num]=list1
    elif num== 30:
        dict1[num]=set1
else:
    print("No Such key in dict1..")
    
print(dict1)

