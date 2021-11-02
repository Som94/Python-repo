#Coffeeshop.py

 

'''

Coffee - 1tbps sugar , 30% dicoction, 70% milk

        (default)

 

100's

     def  make_coffee(self)

 

 

A :::   0.5 tbps sugar, 45% dicoction, 55% milk

 

B::      0 tbps sugar ,  50% dicoction, 50% milk

 

C::     add cream to it

'''

class revenue:

    def __init__(self):

        self.revenue = '50 Lakhs INR'

   

    def print_revenue(self):

        print ('Revenue of the shop is ',self.revenue)

       

    @classmethod

    def revenue_office(cls):

        print ('The revenue office is M.G Raod , Bangalore 560001 ')

       

def greetings():

    print (' hello good day !! ')

 

#class beverage(object):

class beverage():

    pass

 

class coffee(beverage):

    def __init__(self):

        self.sugar = 1

        self.dicoction=30

        self.milk=70

       

    def make_coffee(self):

        print ('coffee ready ')

        print ('details ',self.sugar,' tbps ', ' dicoction% ',self.dicoction)

        print ('milk % ',self.milk)

 

class my_coffee(coffee):

   

    def make_coffee(self):

        self.sugar = 0.5

        self.dicoction=45

        self.milk=55

        print ('coffee ready ')

        print ('details ',self.sugar,' tbps ', ' dicoction% ',self.dicoction)

        print ('milk % ',self.milk)

   

class another_coffee(coffee):

    def make_coffee(self):

        self.sugar = 0

        self.dicoction=50

        self.milk=50

        print ('coffee ready ')

        if (self.sugar == 0):

            print ('details Sugarless ',' dicoction% ',self.dicoction)

            print ('milk % ',self.milk)

           

class coffee_cream(another_coffee):

   

    @staticmethod

    def myshop_name():

        print ('Coffee shop :: Uphar Darshini Coffee Center')

       

    def __init__(self,cr):

        super().__init__()

        self.cream = cr

       

    def make_coffee(self):   

        super().make_coffee()

        print ('addition is cream ....',self.cream)

        print ()

        greetings()

        r = revenue() # creating the object of another class

        r.print_revenue() # object to object communication

        print ('----Info of the office details ----')

        revenue.revenue_office()

           

    

print ('----- main BLOCK --------')       

print (' ----- Chikamangaluru Coffee Shop ')

c1 = coffee()

c1.make_coffee()

print ('------')

c2 = my_coffee()

c2.make_coffee()

print ('------')

c3 = another_coffee()

c3.make_coffee()

print ('------')

c4 = coffee_cream('cream type thin ')

c4.make_coffee()

print ('--------')

coffee_cream.myshop_name()

c5 = coffee_cream('thick 5gms cream')

c5.make_coffee()

print ('--------')

#print (dir(c5))

print ('hash code ',c5.__hash__())

print ('size of  ',c5.__sizeof__())   # 32 bytes

print ('------')

obj1 = object()

print ('hash code of object created is ',obj1.__hash__())

print ('size of object created is  ',obj1.__sizeof__())   # 16 bytes  