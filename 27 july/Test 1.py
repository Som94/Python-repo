'''
Has a relation ship
Aggregation.py
'''
 

class automobile(object):

    pass

 

class engine(automobile):

    def __init__(self):

        print ('i am in engine class')

        self.eng_type = ''

 

class power_trans(automobile):

    def __init__(self):

        print ('i am in power trans class')

        self.power_tran_type = ''

       

class car1:

    def __init__(self):

        self.e1 = engine()

        self.e1.eng_type = 'Petrol operated'

        self.pt1 = power_trans()

        self.pt1.power_tran_type='abc type ...'

        print ('i am in car 1 init method ')

        print ('Engine type is ',self.e1.eng_type)

        print ('Power transmission mechanism ',self.pt1.power_tran_type)

 

class car2:

    def __init__(self):

        self.e1 = engine()

        self.e1.eng_type = 'Diesel operated'

        self.pt1 = power_trans()

        self.pt1.power_tran_type='xyz type ...'

        print ('i am in car 2 init method ')

        print ('Engine type is ',self.e1.eng_type)

        print ('Power transmission mechanism ',self.pt1.power_tran_type)   

 

print ('i am in main block')      

print ('------- I am car1 ------------------')

c1_ram = car1()

c1_shyam = car1()

c1_mohan = car1()

print (id(c1_ram),id(c1_shyam),id(c1_mohan))

print()

print ('------- I am car2 ------------------')

c2 = car2()

c2_vivian = car2()

c2_shekar = car2()

 

print (id(c2_vivian),id(c2_shekar))

print ('----------d o n e---------------')

 