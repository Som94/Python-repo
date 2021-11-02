'''
input a number and add all of its digits,find avg , highest and lowest among the digits
'''

number=int(input("Enter any digit Number :"))

sum_of_digit=0
count=0
list_digit=[]
for i in str(number):
    list_digit.append(int(i))
    sum_of_digit=sum_of_digit+int(i)
    count=count+1
list_digit.sort()
print("Sum of all digit of gib=ven number is :",sum_of_digit)
print('Average of all digit is :',sum_of_digit/count)
print('highest among the digit is :',list_digit[-1])
print('Lowest among the digit is :',list_digit[0])



