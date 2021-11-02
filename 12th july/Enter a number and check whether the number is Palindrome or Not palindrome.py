'''
3.

Enter a number and check whether the number is Palindrome or Not palindrome
Example,    1001  is a palindrome (same reading from left to right or right to left)

2005  is not palindrome

 

Once 3 is working, build a for loop accept 5 numbers and repeat the process

'''

for i in range(5):
    number=int(input("Enter any number : "))
    rev_number=0
    num=number
    while number>0:
        digit=number%10
        rev_number=(rev_number*10)+digit
        number=number//10
    if rev_number==num:
        print(num,"is a palindrome")
    else:
        print(num," is not a palindrome")
        