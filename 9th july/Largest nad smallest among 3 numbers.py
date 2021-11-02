''' Input 3 numbers from user and find out highest and lowest number among them '''
fist_number=int(input("Enter first number : "))
second_number=int(input("Enter second number : "))
third_number=int(input("Enter third number : "))

if fist_number>second_number and second_number>third_number:
    print("highest number is : ",fist_number,"Lowest number is : ",third_number)
    
if second_number>third_number and third_number>fist_number:
    fist_number,third_number=third_number,fist_number
    fist_number,second_number=second_number,fist_number
    
    print("highest number is : ",fist_number,"Lowest number is : ",third_number)
    
if third_number>fist_number and fist_number>second_number:
    
    third_number,fist_number=fist_number,third_number
    third_number,second_number=second_number,third_number
    
    
    print("highest number is : ",fist_number,"Lowest number is : ",third_number)