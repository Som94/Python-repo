
'''

when the issue will come.....

when the function tries to modifies the global variable after using/displaying it

when the keyword global was not used in the BEGINING OF THE FUNCTION (start of the funcion body)

VIOLATION

 

what type of error

UnboundLocalError: local variable 'this_year'

referenced before assignment

'''

# what is pass by value

greets = 'Have a wonderful day '

this_year = 2021

 

def pass_by_value_demo(a,b):

    #global this_year

    #this_year = 2025

   

    this_year = 2002

    print ('inside the function a is ',a,'b is ',b)

    print ('inside the function ....WATCH THIS .....id of a is  ',id(a),' id of b is ',id(b))

    a=99

    b='Kiran Kumar'

    print ('inside the function after altering ....WATCH THIS .....id of a is  ',id(a),' id of b is ',id(b))

    print ('inside the function AFTER ALTERING a is ',a,'b is ',b)   

    print (' brother about to exit out of the function ....')   

    print ('inside function LOCAL ' ,greets, '  ',this_year)

    this_year = 2025

    print ('inside function GLOBAL ' ,greets, '  ',this_year)

    print (' === ===  = === = = = == = == = =')

 

 

 

a=10

b='Shyam'

print ('before function call ',a, ' ',b)

print ('WATCH THIS .....id of a is  ',id(a),' id of b is ',id(b))

pass_by_value_demo(a,b)

print ('--------------------- I am back ----------')

print ('now the value of  ',a, ' ',b, ' values are UNCHANGED ')

print ('when i am back ...WATCH THIS .....id of a is  ',id(a),' id of b is ',id(b))

print ('in the main block  GLOBAL var ' ,greets, '  ',this_year)