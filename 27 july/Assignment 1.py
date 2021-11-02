'''
Create the class and defined methods , create objects to solve the following
 

Create a Circle class and pass the radius to the constructor (__init__ method

 

Compute the area and perimeter , area is PIE x radius squared,  perimeter is 2 x PIE x radius

'''
import math

class Circle:
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        self.area_circle=math.pi*math.pow(self.radius,2)
        
        print("Area of the circle is :",self.area_circle)
    def perimeter(self):
        self.perimeter_of_circle=2*math.pi*self.radius
        
        print("Perimeter of the circle is :",self.perimeter_of_circle)
  

num = int(input("Enter radius of circle: "))      
circ=Circle(num)
circ.area()
circ.perimeter()