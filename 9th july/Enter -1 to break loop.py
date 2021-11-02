

sum=0
count=0
highest=0
lowest=99999999
last_num=0
sec_last=0
while True:
    
    num=int(input("Enter any number :"))
    if (not(num ==-1)):
        if num<0:
            num=num*(-1)
        sum=sum+num
        count=count+1 
        sec_last=last_num
        last_num=num
        
    else:
        break
    if count==2:
        s_input=num
    if num>highest:
        highest=num
    if num<lowest:
        lowest=num
   
print("Sum of inputed Numbers is :",sum,"And avarage of all numbers :",sum/count)
print("Highest Number is :",highest,',',"Lowest Number is :",lowest)
print("Second Input number is :",s_input)
print("Second Last Input number is :",sec_last)