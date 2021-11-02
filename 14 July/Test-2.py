lst = [12,56,9,10]      #-- List

tp1  = 10,45,67,8,19    #-- tuple

tp2  = (10,45,67,8,19)  #-- tuple

st1  = {45,12,55,66,65} #-- set 

fz   = frozenset(st1)   #-- now fz is FROZEN SET (read only)

dc1  = { 190:166661, 191:45522, 899:1816161}  #-- dictionary

 

 

print (type(lst))

print (lst)

print (' -----------------------')

print (type(tp1))

print (tp1)

print (' -----------------------')

print (type(tp2))

print (tp2)

print (' -----------------------')

print (type(st1))

print (st1)

print (' -----------------------')

print (type(fz))

print (fz)

print (' -----------------------')

print (type(dc1))

print (dc1)

print (' -----------------------')

 

emp = {100:'Ravi', 200:'Shyam', 300:'Uday', 100:'Kishore'}

empdata = {400 : ('Ganesh','Vinay','Arun','Hari'), 500: ['Manoj','Alex','Samson',78500,True,False]}

 

print ('emp is ',emp)

print ('emp data is ',empdata)

 

hello_list=[56,78,[44,55,21,22,[1,2,3]]]

print ('hello list has ',hello_list)

 

print('the element is ',tp2[2])

# TypeError: 'tuple' object does not support item assignment

# tp2[2] = 199

 

# TypeError: 'set' object is not subscriptable

# print (st1[3])

# TypeError: 'frozenset' object is not subscriptable

# print (fz[0])

# KeyError: 898 , because 898 is NOT THERE IN THE DICTIONARY

print (dc1[190])

print (empdata[500])

 

for x in empdata[400]:

    print (x)