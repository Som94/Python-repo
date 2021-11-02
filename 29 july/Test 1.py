#Super_sub_class_demo.py

 

class parallelogram:  # this is super class

    def __init__(self):

        self.concept = 'xyz'

        print ('i am inisde parallelogram class ')

#        print ('this is MEANINGLESS .... ',self.length)

#        print ('this is MEANINGLESS .... ',rectangle.length)

    def get_details(self):

        return self.concept

 

# IS a realtionship         rectangle is sub class/derived class

class rectangle(parallelogram):

    #this is class variable

    maths_teacher = 'Dr Kumar' # visible anywhere in the program

    @classmethod

    def disp_maths_teacher_name(cls):

        print ('the math teacher name is ', cls.maths_teacher)

       

    def  __init__(self,length=0,breadth=0):

        super().__init__()  # this is INVOKING THE super class init method()

        self.length = length

        self.breadth = breadth

        self.concept = 'time and tide wait for none '

        print ('location in RAM is ',id(self))

        print ('SUB CLASS concept (data member) of rectangle class  ',self.concept)

        print ('SUPER CLASS concept of pllgm is ', super().get_details())

# AttributeError: type object 'super' has no attribute 'concept'       

#        print ('ERROR SUPER CLASS DIRECT var concept of pllgm is ', super.concept)

#        super().__init__()

 

    def change_teacher(self,nm):

        rectangle.maths_teacher=nm

           

                

print ('before change ')

rectangle.disp_maths_teacher_name()

r1 = rectangle(10,15)    # r1 ------> own copy of length,breadth,area,peri          2389289318990

r2 = rectangle(20,25)    # r2 -------> its own copy of length,breadth,area,peri     2389289318555

r2.change_teacher('Dr Neeraj Sharma')

rectangle.maths_teacher='Prof Manoj Mehta'

print ('AFTER .....who was teaching maths to all the students ?? ')

rectangle.disp_maths_teacher_name()

r3 = rectangle()

r4 = rectangle(35)

 

 