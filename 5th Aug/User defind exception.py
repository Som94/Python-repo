#User_defined_exception.py

 

class MyMarksRange(Exception):

    def __init__(self,mrk,sub):

        self.marks = mrk

        self.subject=sub

       

    def marks_rule(self):

#        if (self.marks < 0 or self.marks > 100):

        if (self.subject =='P' or self.subject=='M'):

            return 'Brother you entered '+str(self.marks)+' but marks range is not ok. it must be 0 to 100 only'

        elif self.subject =='C':

            return 'Brother you entered '+str(self.marks)+' but marks range is not ok. it must be 0 to 125 only'

       

print ('---i am in main block ---- ')       

try:

    maths = int(input('enter the maths marks (0-100) '))

    if (maths < 0 or maths > 100):        

        raise MyMarksRange(maths,'M')

    print ('score in maths is ',maths) 

    phy = int(input('enter the phy marks (0-100) '))

    if (phy < 0 or phy > 100):        

        raise MyMarksRange(phy,'P')      

    print ('score in physics is ',phy)         

    chem = int(input('enter the chemistry(major) marks (0-125) '))

    if (chem < 0 or chem > 125):        

        raise MyMarksRange(chem,'C')      

    print ('score in chemistry (major) is ',chem)         

    print ('prog is over ')

except  MyMarksRange as x:

        temp_msg = x.marks_rule()       

        print (temp_msg)

 