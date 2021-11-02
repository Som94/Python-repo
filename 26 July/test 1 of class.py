class Employ:

    '''

    def __init__(self):

        print ('i am in the init with 0 args [CONSTRUCTOR] ')       

    ''' 

    # the above is WRONG you cannot have multiple init

    #def __init__(self,name,empid,salary):           

    #                 <---attributes --------->       

    def __init__(self,name='',empid=0,salary=0):

        print ('i am in the init with 3 args [CONSTRUCTOR] ')

        self.name = name

        self.empid = empid

        self.salary = salary

       

    def disp_details(self):

        upname = self.name.upper()

        print ('name is ',upname)

        print ('ID is ',self.empid)

        print ('salary is INR ',self.salary)

 

 

print ('this is my MAIN BLOCK')

e1 = Employ('Shankar',1614142,56500) # this is the process of OBJECT CREATION

print ('object created ',type(e1), id(e1))

e1.disp_details()

print ('-----------------------')

e2 = Employ('Harish',3474645,35600)

print ('object created ',type(e2), id(e2))

e2.disp_details()

print ('-----------------------')

e3 = Employ()

e3.upname = 'Vijay'   # this is ignored

e3.name= 'Som'

e3.empid = 101

e3.salary = 50000

e3.junk = 100   # this is ignored

e3.disp_details()