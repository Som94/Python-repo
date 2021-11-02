#Method overloading concept

 

# class

class Compute:

# area method

    def area(self, x = None, y = None):

        if x != None and y != None:

            return x * y

        elif x != None:

            return x * x

        else:

            return 0

    def my_display(self, n1=None,n2=None,n3=None):

        if (n1!= None and n2!= None and n3!= None):

            print ('3 arg ',n1,' ',n2,' ',n3,end=' ')

        elif (n1!= None and n2!= None and n3== None):

            print ('2 arg ',n1,' ',n2,end=' ')

        elif (n1!= None and n2== None and n3== None):           

            print ('1 arg ',n1)

        else:

            print ('YOU DID NOT PASS any paramters')

        print()

 

# object

obj = Compute()

# zero argument

print("Area Value:", obj.area())     # EXPEECTED output is 0

# one argument

print("Area Value:", obj.area(4))    # as only one input value is provied 16

# two argument

print("Area Value:", obj.area(3, (5,6,7)))  # as both are provied then 3x5 = 15

print ('------------------')

try:

    obj.my_display('Ajay','Godron','Hari')  # 3

    obj.my_display('James','Anderson')      # 2

    obj.my_display('Ian Botham')            # 1

    obj.my_display()                        # 0  

    obj.my_display('Ajay','Godron','Hari','Kiran')  # 4

except TypeError :

    print ('somewhere you passed more arguments ...check it ')   

 