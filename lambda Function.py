
# lambda <multiple arguments> : <expressions>

s=lambda a,b: a+b

print(s(10,20))

mult= lambda d,i,o: d*i+o

print(mult(10,15,20))


sub= lambda  r,b: r-b

re=sub(40,10)

print(re)


# filter ()

#syntax:
    
#filter( function name, sequence)

# In filter function we can't modify the given sequence of data 
# But we can only filter out or travercing on the given sequence of data like list and tuple


list1=[12,34,33,65,32,65]

tup=(2,3,34,23,22,53)



even=list(filter(lambda  a : a%2==0  , tup))

print(even)

odd=tuple(filter( lambda a : a %2 !=0 , list1))

print(odd)

st={12,3,45,76,85,34} # We can't use set as sequence in lambda function.

st1=[12,3,45,76,85,34]
st2=[2,3,34,23,22,53]

add5=list(filter( lambda a : a+5 , st1))

print(add5)


str1='mahendraSomanath'

data=list(filter( lambda w : w=='m', str1))

print(data)


data1=list(filter( lambda a: a, (st2+st1)))

print(data1)


data3=list(filter(lambda a : a%2==0 , data1))

print(data3)

# map() 

#suntax:
    
#    map( function , sequence)

#Arithmatic operator over map()

lst2=[10,29,91,39,26]

rstl=list( map(lambda a : a+5 , lst2) )

print(rstl)

#Relational operator over map()

lst3=[10,29,91,39,26]

rstl1=list( map(lambda a : a>55 , lst2) )  # it returns list of boolean values

print(rstl1)

lst4=[10,29,91,39,26]

rslt2=list(map(lambda a : a+a ,lst4))

print(rslt2)



st1=[12,3,45,76,85,34]
st2=[2,3,34,23,22,53]

rslt3= list(map(lambda a ,b : a+b , st1,st2))

print(rslt3)  #if length of 2 list are equal then we get same length of result set of asdditiion operation


st1=[12,3,45,76,85]
st2=[2,3,34,23,22,53,122]

rslt4=list(map(lambda  a,b : a+b , st2,st1))

print(rslt4)  # It will return result  accordoing to set of data  which having min length of sequence of given data set.


#Reduce () , It is use for, to make n elements present in a sequence in a single value.
#syntax:
#     reduce(function, sequence)


print(sum(st1)) 

# we must import reduce function from functool

from functools import reduce

st1=[12,3,45,76,85]

#a=0 ,12, 3 , 45, 76 , 85 
#b=0, 12, 15, 60, 136, 221

#rslt =0, 221

rslt5=reduce( lambda a ,b: a+b , st1 )

print(rslt5)


rslt6=reduce( lambda a ,b: a*b , st1 )

print(rslt6)
