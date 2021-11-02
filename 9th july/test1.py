sum=0
count=0
for x in range(0,2):
    
    while True:
        num=int(input("Enter any number :"))
        
        if num>999 and num<10000:
            print(num)
            sum=sum+num
            break
        else:
            count=count+1
print("Sum of 4 digit numbers is :",sum)
print("The number of attemption of 4 digit number is :",count)