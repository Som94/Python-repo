"""
Figure out whether customer get discount or not.
"""
flag=True

total_price=0

gross_price=0

while flag:
    
    month=int(input("Enter which month you purchase : "))
    week_day=int(input("Enter the which day you purchase : "))
    time_of_day=int(input("Enter the time at which time you purchase : "))
    loyal_customer=input("The customer is loyal or not  (y/n) : ")
    payment_mode=input("Are you using card1 or card2 for payment or not  (y/n) : ")
    item_1=int(input("Enter the quanity of item 1 : "))
    item_2=int(input("Enter the quanity of item 2 : "))
    item_3=int(input("Enter the quanity of item 3 : "))
    item_4=int(input("Enter the quanity of item 4 : "))
    item_5=int(input("Enter the quanity of item 5 : "))
    
    total_1=(100*item_1)+(75*item_2)+(65*item_3)+(25*item_5)
    
    total_2=40*item_4
    
    
    
    if month==5 or  month==6 or month==7:
        if week_day==6 or week_day==7:
            if time_of_day>=18 and time_of_day<=21:
                total_price=total_1+total_2
                     
            else:
                
                if total_1>=1000 and total_1<=2000:
                    total_1=total_1-total_1*(4/100)
                    
                elif total_1>=2001 and total_1<=5000:
                    total_1=total_1-total_1*(6.5/100)
                    
                elif total_1>5000:
                    total_1=total_1-total_1*(8/100)
                    
                    
                if loyal_customer=='y':
                    total_1=total_1-total_1*(1/100)
                    
                if payment_mode=='y':
                    total_1=total_1-total_1*(0.5/100)
                   
                    
                total_price=total_1+total_2
                
        
        else:
                
                if total_1>=1000 and total_1<=2000:
                    total_1=total_1-total_1*(4/100)
                    
                elif total_1>=2001 and total_1<=5000:
                    total_1=total_1-total_1*(6.5/100)
                    
                elif total_1>5000:
                    total_1=total_1-total_1*(8/100)
                    
                    
                if loyal_customer==True:
                    total_1=total_1-total_1*(1/100)
                    
                if payment_mode=='y':
                    total_1=total_1-total_1*(0.5/100)
                    
                    
                total_price=total_1+total_2
                        
                        
    else:
        total_price=total_1+total_2
        
    stop=input("Do you want purchase more..  (y/n) : ")
    if stop=='n':
        flag=False
    gross_price += total_price
    
print("The total price of the product after all discount is : ",gross_price)