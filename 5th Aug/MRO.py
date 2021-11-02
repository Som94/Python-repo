class Alpha(object):

    def __init__(self,x):

        self.x = x

    def disp(self):

        print ('in alpha x is ', self.x) 

 

class Beta(Alpha):

    def __init__(self,y):

        self.y = y

        super().__init__(y+1)

    def disp1(self):

        print ('in Beta y is ', self.y)         

        self.disp()

 

class Delta(Alpha):

    def __init__(self,z):

        self.z = z

        super().__init__(z+1)

    def disp1(self):

        print ('in Delta  z is ', self.z)          

        self.disp()

class Theta(Beta,Delta):

#class Theta(Delta,Beta):   

    def __init__(self,m,n):

        self.m = m

        self.n  = n

        super().__init__(m+n)

    def disp_theata_memb(self):

        print ('m is ',self.m,' n is ',self.n)    

    def disp1(self):

        print ('i have overridden the disp1() in Theta class')

        super().disp1() # what happens

 

print ('---in main block ---')       

a = Alpha(10)

a.disp()

print ('------')

b = Beta(15)

b.disp1()

print ('------')

c = Delta(25)

c.disp1()

print ('------')

t = Theta(78,80)

t.disp_theata_memb()

print ('===============')

t.disp1()

print(Theta.mro())