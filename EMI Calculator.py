def EMICALCULATOR(loan_amount,interest_rate,no_tenure):
	interest_rate=interest_rate/(12*100)
	#no_tenure=no_tenure*12
    
    
	emi=loan_amount*interest_rate*((1+interest_rate)**no_tenure)/((1+interest_rate)**no_tenure-1)
	emi=round(emi)
	print("Your monthly EMI is :",emi)
loan_amount=float(input("Enter your loan amount :"))
interest_rate=float(input("Enter your  interest rate :"))
no_tenure=int(input("Enter your no. of tenure (Month wise) :"))

EMICALCULATOR(loan_amount,interest_rate,no_tenure)


