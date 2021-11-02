'''
Create a class called Employ have the data members empid, name
Defined the display()

Sub class the Employ – call it as EmpDetails – have data members email Id, mobile number

Define the method emp_details_display()

Again sub class EmpDetails – call it as EmpDeptDetails – have data members – dept name and designation

(example  it can be Sales, Sales executive)

 

Create objects of EmpDeptDetails and display the output as following

 

E1019  Ravi Kumar

ravi@gmail.com  9778845234

Sales , Sales executive

'''

class Employ:
    def __init__(self):
        self.empid='E1019'
        self.name='Ravi Kumar'
    def display(self):
        print("The Employee id is :",self.empid)
        print("The Employee Name is :",self.name)
class EmpDetails:
    def __init__(self):
        self.emp=Employ()
        self.email_id='ravi@gmail.com'
        self.mobile_number=9778845234
    def emp_details_display(self):
        #self.emp=Employ()
        self.emp.display()
        print("The Employee Email id is :",self.email_id)
        print("The Employee Mobile Number is :",self.mobile_number)
        
class EmpDeptDetails:
    def __init__(self):
        #self.emp=Employ()
        self.empd=EmpDetails()
        self.dept='sales'
        self.designation='Sales executive'
    def EmpDeptDetails_display(self):
        self.empd.emp_details_display()
        print("The Employee Dept  is :",self.dept)
        print("The Employee designation in dept is :",self.designation)
        
        
        
d=EmpDeptDetails()
d.EmpDeptDetails_display()