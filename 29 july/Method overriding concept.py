#Method overriding

 

 

class study:

    def __init__(self,s):

        self.study_method = s

 

    def how_you_study(self):

        print ('how i study is',self.study_method)

 

class my_approach(study):

     

    def __init__(self,study_hours=2):

        super().__init__('reading books')

        self.study_hours = study_hours

 

    def display(self):

        print ('i study for ', self.study_hours)

 

# the below is overridden

    def how_you_study(self):

         print ('I always like to browse the net and study tutorials and watch videos')      
         print('And get some knowledge through it..')
        

        

print ('inside main block')       

 

m1 = my_approach(16)

m1.how_you_study()

m1.display()

 

 