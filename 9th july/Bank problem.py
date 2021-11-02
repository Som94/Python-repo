
customer_status=int(input("Check whether Customer Account is Active (100) or Not Active(25) : "))
if customer_status==100 or customer_status==25:
    if customer_status==100:
        
        avialable_ac_bal=int(input("Enter Your Account Balance : "))
        minimum_bal=5000

        while True:
            
            oparetion=int(input("Enter which oparetion you want to perform, 1 for withdraw,2 for deposite and 0 for balance inquary : "))
            if oparetion>=0 and oparetion<3:
                if oparetion==1:
                    withdraw_amt=int(input("Enter your Withdraw Amount : "))
                    if withdraw_amt<avialable_ac_bal:
                        avialable_ac_bal = avialable_ac_bal - withdraw_amt
                        if avialable_ac_bal>minimum_bal:
                            print("A successfull transactioin ")
                            print("Your Avialable Balance is : ",avialable_ac_bal)
                        else:
                            print("Unsuccessful transaction, You must mentain your minimum account balance as 5000")
                    else:
                        print("Unsuccessful transaction, Due to Insufficient Fund")
                if oparetion==2:
                    deposite_amt= int(input("Enter your Deposite Amount : "))
                    avialable_ac_bal = avialable_ac_bal + deposite_amt
                    print("A successfull transactioin ")
                    print("Your Avialable Balance is : ",avialable_ac_bal)
                if oparetion==0:
                    print("Your Avialable Balance is : ",avialable_ac_bal)
            else:
                print("Please Enter the value either 0 or 1 or 2 , except these three nothing else..")
            stop=input("Do you want to perform any other oparetion : y/n : ")
            if stop=='n':
                break;
                
                
    if customer_status==25:
        print("Sorry.. Your Account Deactive, for this please contact in your nearest branch. Thank you")
else:
    print("Please.. Enter either 100 or 25 for doing the bank oparetions")