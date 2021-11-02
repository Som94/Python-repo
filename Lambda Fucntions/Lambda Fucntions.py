# To check smallest number
s=lambda a,b:a if a<b else b
print(s(10,2))

# To check even or odd number
s1=lambda a: 'EVEN' if a%2==0 else 'Odd'
print(s1(10))

#To check number of digits in a number 

s3=lambda a:len(str(a))
print(s3(282),"digits number")
print(len(str(23)),"digit number")

# To check whether the number is 2 digit or not

s4=lambda a: 'Yes 2 digit number ' if a>9 and a<100 else "Not a 2 digit number"

print(s4(34))

l=[2,4,65,7,8,9]

def is_even(x):
    if x%2==0:
        return True
    else:
        return False
l2=list(filter(is_even,l))
print(l2)

# with Lambda function

l3=list(filter(lambda x:  x%2==0 ,l))   # find even number only
print(l3)

l4=list(filter(lambda x : x%2 != 0,l))  #find Odd number only
print(l4)

l5=list(filter(lambda x : x*2,l))   # filter() is only use for filter out records,
                                    # but don't modify the records present in sequence 
                                    #like list,tuple,string,
                                    # So , for modification we go for map() function
print(l5)

l6=list(map(lambda x: x**2,l))   # it will return list of square element of l list
print(l6)

from functools import  reduce
l7=reduce(lambda x,y:x+y,l)
print(l7)