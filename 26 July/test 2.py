def author():

    first_name = 'Somnath'

    second_name = 'Ojha'

    print ('------Author details are as below ')

    print ('author name is ',first_name, '  ',second_name)

    print ('----------------------------------')

    print ()

   

    

class Rectangle:

 

    def __init__(self,length=0,breadth=0)    :

        self.length = length

        self.breadth = breadth

        self.area =0

        self.perimeter = 0
        
        self.diagonal = 0   

        print ('in init constructor method body ....')

 

    def input_details(self):

        self.length=int(input('enter the length ... '))

        self.breadth=int(input('enter the breadth ... '))

       

    def calc_area(self):

        self.area = self.length * self.breadth

   

    def calc_perimeter(self):

        self.perimeter = 2 * (self.length+self.breadth)
        
    def calc_diagonal(self):
        self.diagonal = math.sqrt(self.length+self.breadth)
        
         

       

    def display(self):

        self.calc_area()

        self.calc_perimeter()

        print ('Area is ',self.area)

        print ('Perimeter is ',self.perimeter)

        author()  # is a normal method hence it is

        # not prefixed with self as it is NOT THE PART

        # OF rectangle class

 

    def get_results(self):

        # do the computation

        self.calc_area()

        self.calc_perimeter()

        return self.area,self.perimeter

   

# either you can pass the data in the constructor

# how Rectangle(25,15)

# either you can input the data from keyboard

# how.....input_details()

# either you can input the data via the OBJECT HANDLE

# how  r5.length = xxx     r5.breadth = yyy

 

print ('i am in MAIN BLOCK ')   

r1 = Rectangle(25,15)

r1.display()

print ('----------')

r2 = Rectangle(20,10)

r2.display()

print ('----------')

r3 = Rectangle()

r3.input_details()

r3.display()

print ('----------')

r4 = Rectangle()

r4.input_details()

a,p = r4.get_results()

print ('WATCH object is r4 ...hello area is ',a,' perimeter is ',p)

print ('----------')

r5 = Rectangle()

r5.length = 30

r5.breadth =20

r5.display()