d={1000: [1000, 'som', 50000, 9658744330, 'x@gmail.com', 'w'], 2000: [2000, 'pk', 60000, 866885221, 's@gmail.com', 'd']}

d1={}

print(len(d1))



'''
Transaction_list={'Ac_no': 3000, 'Ac_holder_name': 'Viswanath', 'Tran_mode': 'Withdraw', 'Amount': 40000, 'Mobile': 7845866998, 'Email_id': 'visanth@gmail.com'}

import datetime    
class Transaction:
    
    def __init__(self,account_no,name, tran_type, amt_transacted , Date_time):
        
        self.account_no=account_no
        self.name=name
        self.tran_type=tran_type
        self.amt_transacted=amt_transacted
        self.Date_time=Date_time
     
        self.account_no=Transaction_list['Ac_no']
        self.name=Transaction_list['Ac_holder_name']
        self.tran_type=Transaction_list['Tran_mode']
        self.amt_transacted=Transaction_list['Amount']
        self.Date_time=datetime.time()
        
    




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
        
    
tm=TransMobile(Transaction_list['Ac_no'],Transaction_list['Ac_holder_name'],Transaction_list['Tran_mode'],Transaction_list['Amount'],Transaction_list['Mobile'],datetime.datetime.now())
tm.display()

te=TranEmail(Transaction_list['Ac_no'],Transaction_list['Ac_holder_name'],Transaction_list['Tran_mode'],Transaction_list['Amount'],Transaction_list['Email_id'],datetime.datetime.now())
te.display()
 '''