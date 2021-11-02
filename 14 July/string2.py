'''

Part C

Start processing the string from reverse (from last char).
Count how many 5 and 6 digits are there.
Once the count reaches 8 stop, come out of the loop
 

'''

st1 = "hello 123 test 456789 22 89 all is 235 and go59066558875599022ing 89765 we7856112ll 1A2#$$#@$@350000000000"
sum_of_digit=0
count=0

print("processing the string from reverse",st1[::-1])

list1=st1.split()
for i in st1:
    if i=='5' or i=='6':
        count += 1
        if count>=8:
            break
    
print("Count how many 5 and 6 digits are there ",count)


