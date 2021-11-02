def proverb1():

    print ('from func proverb1 --- God\'s mill grinds slow but sure ')

 

def proverb2():

    print ('from func proverb2 --- All THAT GLITTERS IS NOT GOLD ')

   

def greet():

    print ('welcome ...good day')

    print ('happy to note that all is well ')

 

def add(a,b):

    if ((a > 9 and a < 100) and (b > 9 and b < 100)):

        total = a + b

        print ('total is ',total,' of a value ',a,' b value is ',b)

    else:

        print ('either ',a,' or ' , b , ' is not 2 digit number !!')          

 

def adding_numbers(a,b):

    if ((a > 9 and a < 100) and (b > 9 and b < 100)):

        total = a + b       

        return total

    else:

        msg = 'either '+str(a)+' or ' +str(b)+ ' is not 2 digit number !!'                  

        return msg

   

 

print ('i am here ')   

print ('i am about to invoke greet funtion ')

greet()

proverb2()

proverb1()

print ('hey i am back to the next line after completing the  function greet')

add(12,38)

print (' -------------------------- ')

add(2,38)

print (' -------------------------- ')

add(12,13)

print (' -------------------------- ')

print ( '***  total is ' , adding_numbers(19,81), ' ****')

print ( adding_numbers(29,81))

adding_numbers(14,15)

 

# function could be assigned to a variable

temp=adding_numbers(14,15)

print (temp)

