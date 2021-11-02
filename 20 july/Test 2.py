 

# these are global variables

greets = 'Have a wonderful day '

this_year = 2021

 

def pass_by_value_demo(a,b):
    
    global this_year
    
    this_year=2222
    
    
    print ('inside the function a is ',a,'b is ',b)

    print ('inside the function ....WATCH THIS .....id of a is  ',id(a),' id of b is ',id(b))

    a=99

    b='Kiran Kumar'

    print ('inside the function after altering ....WATCH THIS .....id of a is  ',id(a),' id of b is ',id(b))

    print ('inside the function AFTER ALTERING a is ',a,'b is ',b)   

    print (' brother about to exit out of the function ....')

    print ('inside function GLOBAL ' ,greets, '  ',this_year)

    #this_year = 2025
    print(this_year)

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

 

 

