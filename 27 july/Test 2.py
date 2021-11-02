#Hierarchy.py

 

class Animal(object):

    def __init__(self):

        print ('i am in animal init method ')

        print ('i am just below the mother of all classes - object')

        print ('the supermost (TOP MOST) class is ALWAYS object ')

        self.life = 100 

        self.delicacy = ''

       

class Mamal(Animal):

    def __init__(self):

        Animal.__init__((self))

        self.heart = '4 chambers'

        print ('i am in mamal init method ')

 

class Feline(Mamal):

    def __init__(self):

        Mamal.__init__(self)

        print ('i am in feline init method ')

 

class Cat(Feline):

    def __init__(self):       

        Feline.__init__(self)

        print ('i am in cat init method ')

   

    def disp_heart_type(self):

        print (self.heart)

        self.life = 10

        print ('life of cat is ',self.life)

        self.delicacy = 'rat,mice'

        print ('cat delicacy is ',self.delicacy)

   

class Tiger(Feline):

    def __init__(self):       

        Feline.__init__(self)

        print ('i am in tiger init method ')

        self.protected_species='yes'

        self.stripped = 180

   

    def disp_heart_type(self):

        print (self.heart)

        self.life = 30

        print ('life of tiger ',self.life)

        print ('am i protected species ? ', self.protected_species)

        print ('how many stripes are there ? ',self.stripped)

        self.delicacy = 'deer, wild-goat'

        print ('tiger delicacy is ',self.delicacy)

       

 

print (' i am in main block')   

 

havana_brown = Cat()

havana_brown.disp_heart_type()

print ('---------')

royal_bengal = Tiger()

royal_bengal.protected_species='earlier I was, now I am not '

royal_bengal.disp_heart_type()

print ('---------')

white_tiger = Tiger()

white_tiger.stripped=65

white_tiger.disp_heart_type()

