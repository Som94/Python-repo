class Customer:
    def __init__(self,ac_no,name,balance,mobile,email,ac_type):
        self.ac_no=ac_no
        self.name = name
        self.balance=balance
        self.mobile=mobile
        self.email=email
        self.ac_type=ac_type
    
        
global Customer_details
Customer_details={}

while True:
    
    ac_no=int(input("Enter Account Number :"))
    name=input("Enter Customre name :")
    balance=int(input("Enter Account Balance :" ))
    mobile=int(input("Enter Mobile NUmber :"))
    email=input("Enter Email Address :")
    ac_type=input("Enter Account Type :")
    c1=Customer(ac_no,name,balance,mobile,email,ac_type)

    Customer_details.update({c1.ac_no:[c1.ac_no,c1.name,c1.balance,c1.mobile,c1.email,c1.ac_type]})

    
    flag=input("Do You want add customer y/n :")
    if flag=='n':
          
        break
     
print(Customer_details)