import math

from functools import reduce

#import reduce

 

lst1 = [17,2,100,25]

 

double_it = lambda x : x * 2

 

print (  list(map(double_it,lst1)))

 

#  rule is applied on EVERY ELEMENT OF THE mentioned sequence

lst2 = [4,36,100,441,625,1]

 

find_sq_root = lambda x : int(math.sqrt(x))

print ()

print ('original list is ',lst2)

print ( 'square roots ', list(map(find_sq_root,lst2)))

 

names =  ['shyam','ravi','ganesh','robert','suresh']

 

 

print (names)

print (list(map( lambda x: x.title() , names)))

 

adding = lambda a,b : a+b

total = reduce(adding,lst2)

print ('total is ',total)