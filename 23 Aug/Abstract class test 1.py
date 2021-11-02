#abc_concept_demo1.py

 

 

from abc import *

class Study(ABC):

   

    @abstractmethod

    def how_to_study(self):

        pass

   

    @abstractmethod

    def when_to_study(self):           

        pass

 

class EnggEntrance(ABC):

        @abstractmethod

        def engg_prep(self):

            pass

       

        def engg_colleges(self):

            lst = ['Pune','Blore','Hyd','Chennai']

            for i in lst:

                print (i)

       

class BE(Study):

    def how_to_study(self):

        print ('in BE I read lecturer notes')

   

 

    def when_to_study(self):           

        print ('in BE I study from 7pm to 9 pm')

 

class MCA(Study):

    def how_to_study(self):

        print ('in MCA I read text books & lecturer notes')

   

 

    def when_to_study(self):           

        print ('in MCA  I study from 6am to 7:30am ')

       

    def some_greet(self):

        print ('MCA in some greet ')       

        

class BCA(Study):

    def how_to_study(self):

        print ('in BCA I watch video and go thru lecturer notes')

   

 

    def when_to_study(self):           

        print ('in BCA I study from 8pm to 10 pm ')

       

class XStd (Study):

    def how_to_study(self):

        print ('in X std I read TB and lecturer notes')

   

 

    def when_to_study(self):           

        print ('in X std I study from 8pm to 11 pm ')

       

class JEE (Study,EnggEntrance):

    def how_to_study(self):

        print ('Read text, practice, listen to lect audio, discuss')

   

    

    def when_to_study(self):           

        print ('1.. 5 am to 8 am')

        print ('2.. 7pm to 11 pm')

       

    def why_I_am_prep_for_JEE(self):       

        print ('To clear the IIT entrance ...First choice IIT Delhi, IIT Powai ')

       

    def engg_prep(self):

        print ('Studying with focus and determination for clearing the various Engg Entrances ')

       

stud_type = input ('which type of student ?  BE , MCA , BCA , XStd , JEE ')       

try:

    classname = globals()[stud_type]

    print ('watch class name is ',classname)

    obj  = classname()   # this is create object

 

    obj.how_to_study()

    obj.when_to_study()

   

    if (hasattr(obj, "some_greet")):

        obj.some_greet()

    elif (hasattr(obj, "why_I_am_prep_for_JEE")):            

             obj.why_I_am_prep_for_JEE()

             obj.engg_prep()

             print ('below are the cities having TOP Engg colleges ...')

             obj.engg_colleges()

            

except KeyError:

    print ('some issue ....pls check what you entered !! ')

 

print ('Progr over ')