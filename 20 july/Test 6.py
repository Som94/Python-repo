
PIEE = 3.14

def calc_details(radius):

    print ('inside the function ...doing calc ')

    a = PIEE * radius * radius

    c = 2 * PIEE * radius

    return a , c

 

def capture_input():

    a= int(input ('enter 2 numbers one by one '))

    b= int(input ('enter another numbers '))

    return a,b

 

def computation(n1,n2):

    total = n1 + n2

    diff = n1 - n2

    prod = n1 * n2

    quot = n1 // n2

    return total,diff,prod,quot

 

def display(rst):

    print ('displaying .........')

    for i in rst:

        print (i)

 

print ('I am in main block ')

radius = float(input ("enter the radius of the circle .... "))

 

area , cirf = calc_details(radius)

print ('I AM BACK area of circle is ',area,' circumference is ',cirf)

print ('------------------- *********  -------------------')

n1, n2 = capture_input()

result  = computation(n1,n2)

display(result)

display(computation(n1,n2))

print ('------------------- *********  -------------------')   

 