#Same concept try applying in JSON

 

#Str_to_dict.py

 

s1 = "Ganesh=78,84,99#Hairsh=83,67,12#Kiran=72,60,50"

print (s1)

print ('convert the string into dictionary, use split ')

mylst=[]

for x in s1.split('#'):

    y=x.split('=')

    mylst.append(y)

print (mylst) 

mydict=dict(mylst) 

print ('mydict is ',mydict)

for k,v in mydict.items():

    print (k,' ',v)

dct={}

for k,v in mydict.items():

    dct[k]=v

 

print (dct['Ganesh'])   

print (dct['Kiran'])  