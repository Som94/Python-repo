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
    def __init__(self,empid,name):
        self.empid=empid
        self.name=name
    def display(self):
        print("The Employee id is :",self.empid)
        print("The Employee Name is :",self.name)
class EmpDetails(Employ):
    def __init__(self,empid,name,email_id,mobile_number):
        super().__init__(empid,name)
        self.email_id=email_id
        self.mobile_number=mobile_number
    def emp_details_display(self):
        self.display()
        print("The Employee Email id is :",self.email_id)
        print("The Employee Mobile Number is :",self.mobile_number)
        
class EmpDeptDetails(EmpDetails):
    def __init__(self,empid,name,email_id,mobile_number,dept,designation):
        super().__init__(empid,name,email_id,mobile_number)
                
        self.dept=dept
        self.designation=designation
    def EmpDeptDetails_display(self):
        
        self.emp_details_display()
        print("The Employee Dept  is :",self.dept)
        print("The Employee designation in dept is :",self.designation)
        
        
#e=EmpDetails('E1019','Ravi Kumar','ravi@gmail.com',9778845234)
#e.emp_details_display()   
        
        
#d=EmpDeptDetails('E1019','Ravi Kumar','ravi@gmail.com',9778845234,'Sales' , 'Sales executive')
#d.EmpDeptDetails_display()

'''
Once above program is working , create another class Salary having the data members as
Number of days worked,  Net Salary

This Salary class should be aggregated to EmpDeptDetails    (HAS A – relationship)

 
The output should come as
 

E1229  Sundar Kumar

sundar@gmail.com  9770045294

Purchase , Purchase Manager

28 ,  INR 56500

'''

class Salary:
    def __init__(self,Number_of_days_worked,Net_Salary,empdd):
        self.Number_of_days_worked=Number_of_days_worked
        self.Net_Salary=Net_Salary
        self.empdd=empdd
        #self.edd=EmpDeptDetails('E1019','Ravi Kumar','ravi@gmail.com',9778845234,'Sales' , 'Sales executive')        

    def Display(self):
        #self.edd=EmpDeptDetails('E1019','Ravi Kumar','ravi@gmail.com',9778845234,'Sales' , 'Sales executive')
        self.empdd.EmpDeptDetails_display()
        print('The number of days working by employee is :',self.Number_of_days_worked)
        print("The Net Salary of the employee is :",self.Net_Salary)
 
d=EmpDeptDetails('E1019','Ravi Kumar','ravi@gmail.com',9778845234,'Sales' , 'Sales executive')
       
sal=Salary(28,'INR 56500',d)
#sal.Display()


'''
3.   Create 4-5 objects and store it in list called emp_list[]
     Display all the stored objects from the list
'''

d1=EmpDeptDetails('A2019','Rohit Sharma','rohit@gmail.com',9337788452,'Cricket' , 'Batsman')
       
rsal=Salary(20,'INR 506500',d1)   
    
   
d2=EmpDeptDetails('D9019','Ms Dhoni','ms@gmail.com',8488245234,'Sports' , 'Captain')
       
dsal=Salary(28,'INR 560500',d2) 

d3=EmpDeptDetails('K9119','Virat','v@gmail.com',6685445234,'Hockey' , 'Goal Keeper')
       
ksal=Salary(28,'INR 56500',d3)

d4=EmpDeptDetails('H1019','Hardik','h@gmail.com',8824045234,'Crickt' , 'All rounder')
       
hsal=Salary(28,'INR 406500',d4)
    

emp_list=[sal,rsal,dsal,ksal,hsal]

for i in emp_list:
     i.Display() 
     print('*'*100)

    
    
    