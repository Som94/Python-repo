'''
Part B

While processing the above string when the count of digit exceed 12 then stop , come out of loop
Display the sum and avg. Again use for and while loop to solve it
 
'''



st1 = "hello 123 test 456789 22 89 all is 235 and go59066558875599022ing 89765 we7856112ll 1A2#$$#@$@350000000000"
sum_of_digit=0
count=0

for i in st1:
    if i.isdigit():
       if count<12:
           sum_of_digit=sum_of_digit+int(i)
       else:
           break
       count += 1
       
print("Sum of upto 12 digit present in the given string is : ",sum_of_digit)
print("And Avarage is :",sum_of_digit/count)
print(count)

print("_____Using while Loop____")

sum_of_digit1=0
str1=''
count1=0

while len(st1)>count1:
    
    if st1[count1].isdigit():
        
        if len(str1)<12:
            str1=str1+st1[count1]
            sum_of_digit1 = sum_of_digit1 + int(st1[count1])
        else:
            break
    count1 += 1
    

print("Sum of all digit present in the given string is : ",sum_of_digit1)
print("And Avarage is :",sum_of_digit1/int(len(str1)))
print(len(str1))