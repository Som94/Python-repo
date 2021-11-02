# -*- coding: utf-8 -*-
"""
Rework the date validation problem with displaying the Day of the week writing
 the needed function
 
Like 

inputDate()

validateDate()

checkLeap()

displayDOW()

etc…..
"""

def inputDate(d,m,y):
    
    global date
    date='/'.join([d,m,y])
    return date
    
d=input("Enter any Date :")
m=input("Enter any Month :")
y=input("Enter any Year :")

inputDate(d,m,y)

def validateDate():
    inputDate(d,m,y)
    date1=date.split('/')
    #print(date1)
    dd,mm,yyyy=int(date1[0]),int(date1[1]),int(date1[2])
    
    if (yyyy%400==0 or (yyyy%100 !=0 and yyyy%4==0) ):
    
        if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            if (dd>0 and dd<=31):
                print('Valid Date')
            else:
                 print('Invalid Date')
        elif (mm==4 or mm==6 or mm==9 or mm==11):
            if (dd>0 and dd<=30):
                print('Valid Date')
            else:
                 print('Invalid Date')
        elif (mm==2):
            if dd>0 and dd<=29:
                print("Valid date")
            else:
                 print('Invalid Date')
        else:
            print('Invalid Month')
            
    else:
        
        if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            if (dd>0 and dd<=31):
                print('Valid Date')
            else:
                 print('Invalid Date')
        elif (mm==4 or mm==6 or mm==9 or mm==11):
            if (dd>0 and dd<=30):
                print('Valid Date')
            else:
                 print('Invalid Date')
        elif (mm==2):
            if dd>0 and dd<=28:
                print("Valid date")
            else:
                 print('Invalid Date')
        else:
            print('Invalid Month')
            
    return date
validateDate()

def checkLeap():
    
    date1=date.split('/')
    
    yyyy=int(date1[2])
    
    if (yyyy%400==0 or (yyyy%100 !=0 and yyyy%4==0) ):
        return ("Leap Year..")
    else:
        return ("Not Leap Year")

checkLeap()

def display():
    
    inputDate(d,m,y)
    checkLeap()
    validateDate()
    
print(display())