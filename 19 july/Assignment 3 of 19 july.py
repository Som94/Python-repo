'''

 given a tuple tp3 =  (199,345,299,199,445,441,778,299,299,350,450,299,199)

     Do what it takes to make the contents of the tuple elements as keys for dictionary.

     And the value should be updated to the next key value.

     If key is 199 then value must be 200

     If key is 445 then value must be 446

 '''
 
tp3 = (199,345,299,199,445,441,778,299,299,350,450,299,199)
#print(tp3)
my_tuple=set(tp3)
#print(my_tuple)
my_tuple=tuple(my_tuple)
#print(my_tuple)
my_dict={}

for i in my_tuple:
    my_dict[i]=i+1
    
print(my_dict)