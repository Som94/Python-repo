'''
1) union         a union b
'''
a = {12,55,66,77}
b = {10,12,25,55}

#    12,55,66,77,10,25    (12,55 are common HENCE APPEARS once)   

 

print('union',a.union(b))

 
'''
2) intersection  a intersection b

   a = {12,55,66,77}

   b = {10,12,25,55}

   o/p  12,55           (which are common in a and b)
'''
 

print('intersection  ',a.intersection()) 

 
'''
3) symmetric difference

   meaning ....

   method returns a set that contains all items from both set, but not the items that are present in    both sets.

 

   a = {12,55,66,77}     66,77

   b = {10,12,25,55}     10,25

 

   common 12,55

   sym diff   is  66,77,10,25
'''
 

print('symmetric_difference : ',a.symmetric_difference(b))

 
'''
4) difference

   a = {12,55,66,77}

   b = {10,12,25,55}

 

  a-b  elements present is a BUT NOT IN b

     intersection result is  12,55


    66,77

 

b-a    o/p         10,25
'''
 

print("Difference : ",a.difference(b))