
from datetime import datetime  

#----------------------User Defined Exception---------------

class InsufficientBalException(Exception):
    def __int__(self,message):
        self.message=message
        
    def display(self):
        
        print(self.message)
        
class AmountDipositException(Exception):
    def __int__(self,message):
        self.message=message
        
class AmountWithdralException(Exception):
    def __int__(self,message):
        self.message=message
        


#----------------------- Coustomer-------------------------

class Customer:
    def __init__(self,ac_no,name,balance,mobile,email,ac_status):
        self.ac_no=ac_no
        self.name = name
        self.balance=balance
        self.mobile=mobile
        self.email=email
        self.ac_status=ac_status
    
        
#global Customer_details
Customer_details={}

while True:
    
    ac_no=int(input("Enter Account Number :"))
    name=input("Enter Customre name :")
    balance=int(input("Enter Account Balance :" ))
    mobile=int(input("Enter Mobile Number :"))
    email=input("Enter Email Address :")
    ac_status=input("Enter Account Status Avtive Or Suspended :")
    c1=Customer(ac_no,name,balance,mobile,email,ac_status)

    Customer_details.update({c1.ac_no:[c1.ac_no,c1.name,c1.balance,c1.mobile,c1.email,c1.ac_status.lower()]})

    
    flag=input("Do You want add customer y/n :")
    if flag=='n':
          
        break
     
print(Customer_details)


#---------------------------- Bank---------------------------------


Transaction_list={}

success_trans_list=[]

failure_trans_list=[]

class Bank:
        
    def __init__(self,acno):
        self.acno=acno
        
        
        
    def deposit(self,amount):
        
        success_trans_list1=[]
        
        failure_trans_list1=[]
        
        if amount not in range(100,1000000):
            failure_trans_list1.append(self.acno)
            failure_trans_list1.append(Customer_details[self.acno][1])
            failure_trans_list1.append('Deposit')
            failure_trans_list1.append(amount)
            
            if amount<100:
                failure_trans_list1.append('amount cannot be less than 100')
              
            else:
                failure_trans_list1.append('amount cannot be greater than 1000000')
                
                
            failure_trans_list1.append(str(datetime.now()))
           
            raise AmountDipositException('Deposite Amount Should be in range 100 to 1000000').display()
                
                
                
        else:
            success_trans_list1.append(self.acno)
            success_trans_list1.append(Customer_details[self.acno][1])
            success_trans_list1.append('Deposit')
            success_trans_list1.append(amount)
            success_trans_list1.append('amount successfully deposited')
            success_trans_list1.append(str(datetime.now()))
            
            Customer_details[self.acno][2] += amount
        print('After deposit ac bal is :', Customer_details[self.acno][2])   
        
        success_trans_list.append(success_trans_list1)
        failure_trans_list.append(failure_trans_list1)
        
                                             
        
    def withdraw(self,amount):
        
        success_trans_list2=[]
        
        failure_trans_list2=[]
        
        if amount in range(100,500000):
            Customer_ac_Bal = Customer_details[self.acno][2]
            
            Customer_ac_Bal -= amount
            if Customer_ac_Bal < 1000:
                failure_trans_list2.append(self.acno)
                failure_trans_list2.append(Customer_details[self.acno][1])
                failure_trans_list2.append('Withdraw')
                failure_trans_list2.append(amount)
                failure_trans_list2.append('min balance is not met')
                failure_trans_list2.append(str(datetime.now()))
                
                raise AmountWithdralException('Please maintain minimum account balance 1000')
            else:
                
                success_trans_list2.append(self.acno)
                success_trans_list2.append(Customer_details[self.acno][1])
                success_trans_list2.append('Withdraw')
                success_trans_list2.append(amount)
                success_trans_list2.append('amount successfully withdraw')
                success_trans_list2.append(str(datetime.now()))
                
                Customer_details[self.acno][2] = Customer_ac_Bal
        else:
            failure_trans_list2.append(self.acno)
            failure_trans_list2.append(Customer_details[self.acno][1])
            failure_trans_list2.append('Withdraw')
            failure_trans_list2.append(amount)
            
            if amount<100:
                failure_trans_list2.append('amount cannot be less than 100')
                
                       
            else:
                failure_trans_list2.append('amount cannot be greater than 500000')
                  
            failure_trans_list2.append(str(datetime.now()))
                    
            raise AmountWithdralException('Withdrawal amount should be in the range 100 to 500000')
                    
        success_trans_list.append(success_trans_list2)
        failure_trans_list.append(failure_trans_list2)           
            
        print('After withdraw ac bal is :', Customer_details[self.acno][2])   

    def balance_check(self):
        print("Your Available Account Balance is :", Customer_details[self.acno][2])
        
     
#-------------------------- Customer Transaction ------------------------



while True:
    accno=int(input("Enter account number :"))
    
    if accno in Customer_details.keys():
        if Customer_details[accno][5] =='active':
            Transaction_list['Ac_no']=accno
            Transaction_list['Ac_holder_name']=Customer_details[accno][1]
            b=Bank(accno)
            oparetion=input('Enter what you want to perform :\n w : Withdraw\n d : Deposit\n b: Balance enquiry\n')
                
            if oparetion.lower()=='w':
                amt=int(input("Enter Withdraw Amount :"))
                b.withdraw(amt)
                Transaction_list['Tran_mode']='Withdraw'
                Transaction_list['Amount']=amt
                
            if oparetion.lower()=='d':
                amt=int(input("Enter Deposit Amount :"))
                b.deposit(amt)
                Transaction_list['Tran_mode']='Deposit'
                Transaction_list['Amount']=amt
                
                            
            if oparetion.lower()=='b':
                b.balance_check()
                
            Transaction_list["Mobile"]=Customer_details[accno][3]
            Transaction_list["Email_id"]=Customer_details[accno][4]
        else:
            print("Your Account Suspended, Please Visit Nearest Branch to Active..")
            break
                
    else:
        print('Account Number not exists')
        
    
    
     
    n=input("Do You wish perform any transaction again y/n :")
    if n.lower() != 'y':
        break

#print("Transaction List :",Transaction_list)

 
#--------------------- Transaction Details ----------------------------      
   
  
class Transaction:
    
    def __init__(self,account_no,name, tran_type, amt_transacted , Date_time):
        
        self.account_no=account_no
        self.name=name
        self.tran_type=tran_type
        self.amt_transacted=amt_transacted
        self.Date_time=Date_time


class TransMobile(Transaction):
    
    
    def __init__(self,account_no,name,tran_type, amt_transacted,mobile , Date_time):
        super().__init__(account_no,name, tran_type, amt_transacted , Date_time)
        self.mobile=mobile
        
    def display(self):
        print("Account No :",self.account_no)
        print("Account Holder Name :",self.name)
        print("Transaction Type",self.tran_type)
        print("Transactioin amount :",self.amt_transacted)
        print('Mobile Number :',self.mobile)
        print("Transaction Time :",self.Date_time)
        
    
    
class TranEmail(Transaction):
    def __init__(self,account_no,name,tran_type, amt_transacted,email , Date_time):
        super().__init__(account_no,name, tran_type, amt_transacted , Date_time)
        self.email=email #Transaction_list['Email_id']
    
    def display(self):
        print("Account No :",self.account_no)
        print("Account Holder Name :",self.name)
        print("Transaction Type",self.tran_type)
        print("Transactioin amount :",self.amt_transacted)
        print('Email ID  :',self.email)
        print("Transaction Time :",self.Date_time)
        

trans_mob_list=[]

trans_email_list=[]

if len(Transaction_list)>0:
    tm=TransMobile(Transaction_list['Ac_no'],Transaction_list['Ac_holder_name'],Transaction_list['Tran_mode'],Transaction_list['Amount'],Transaction_list['Mobile'],datetime.now())
    tm.display()
    date_time=datetime.now()
    trans_mob_list.extend([Transaction_list['Ac_no'],Transaction_list['Ac_holder_name'],Transaction_list['Tran_mode'],Transaction_list['Amount'],Transaction_list['Mobile'],str(date_time)])
   
    print('\n',50*'*')
    
    te=TranEmail(Transaction_list['Ac_no'],Transaction_list['Ac_holder_name'],Transaction_list['Tran_mode'],Transaction_list['Amount'],Transaction_list['Email_id'],datetime.now())
    te.display()
    trans_email_list.extend([Transaction_list['Ac_no'],Transaction_list['Ac_holder_name'],Transaction_list['Tran_mode'],Transaction_list['Amount'],Transaction_list['Email_id'],str(date_time)])
    
    
print('\n',50*'*')    
    
print('Through Mobile :',trans_mob_list)

print('\n',50*'*')
    
print('Through Email ID :',trans_email_list)

print('\n',50*'*')

print('Success transaction List :',success_trans_list)

print('\n',50*'*')

print("Fsilure Transactioin List :",failure_trans_list)



f1=open('success_trans.txt','a+')
for i in success_trans_list:
    if len(i)>0:
        for k in i:
            f1.write(str(k)+' ')
f1.write('\n')
f1.close()
    
f2=open('failure_trans.txt','a+')
for j in failure_trans_list:
    if len(j)>0:
        for l in j:
            f1.write(str(l)+' ')
f2.write('\n')
f2.close()
    