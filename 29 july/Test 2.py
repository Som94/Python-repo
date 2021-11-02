#Super_sub_class_name.py

 

class A:

    def __init__(self, name):

        self.__name = name

        print ('i am inside A\'s init method watch name is ',self.__name)

 

    def print_name(self):

        print (self.__name)

 

 

class B(A):

    def __init__(self, name):

        A.__init__(self, name)  # calling the super class init method

        self.__name = name + "::yes"

        print ('i am inside B\'s init method watch name is ',self.__name )

 

    def print_name(self):

        print ('watch B\'s name is ',self.__name)

 

    def print_super_name(self):

        print ('watch A\'s name is ',self._A__name) #class name mangled into attri

       

print ('i am in main block ')       

 

b = B('hello')

b._A__name = 'A:::hello1 something'

b._B__name = 'B:::Good Day ....something else'

 

b.print_name()

b.print_super_name()

 