from datetime import *
import pandas as pd

current_date=datetime.today()
str_current_date=current_date.strftime('%Y-%m-%d')

def EMICALCULATOR(loan_amount,interest_rate,no_tenure,repayment_start_date):
    interest_rate=interest_rate/(12*100)
    #no_tenure=no_tenure*12
    emi=loan_amount*interest_rate*((1+interest_rate)**no_tenure)/((1+interest_rate)**no_tenure-1)
    emi=round(emi)
    #print("Your monthly EMI is :",emi)
    count=0
    while count<no_tenure:
        
        if repayment_start_date <= str_current_date:
            print("Your repayment start date should be in future..")
            break
        else:
            print("Your EMI Amount is :",emi)
            
            payment_date=datetime.strptime(repayment_start_date,'%Y-%m-%d') + pd.DateOffset(months=count)
            print("And {} EMI Payment date is {}".format(count+1,payment_date.date()))
        
        count += 1
    
loan_amount=float(input("Enter your loan amount :"))
interest_rate=float(input("Enter your  interest rate :"))
no_tenure=int(input("Enter your no. of tenure (Month wise) :"))
repayment_start_date=input(" Repayment start date (yyyy-mm-dd) :")

EMICALCULATOR(loan_amount,interest_rate,no_tenure,repayment_start_date)

