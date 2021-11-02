'''
2.

Input any 7 seven numbers
Check whether the last digit and the second last digit (if any) is either 5 or 8

Display the last (unit place)  and second last digit (tenth place)

Example

1234

4 3    -neither is 5 or 8

158

5 and 8  - yes it is either 5 or 8

Like this 7 times input the number
'''



for i in range(2):
    number=int(input("Enter any number : "))
    if number>9:
        count=0
        while number > 0:
            digi=number%10
            second_last_digit=digi
            count += 1
            if count==2:
                break
            number=number//10
            last_digit=second_last_digit
    else:
        print("Please Enter greater than 9 numbers only..")
        break
    if second_last_digit==5 and last_digit==8:
        print(second_last_digit,' ',last_digit,' - yes it is either 5 or 8')
    else:
        print(second_last_digit,' ',last_digit,' - neither is 5 or 8')
