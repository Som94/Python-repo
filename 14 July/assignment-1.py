'''
If input like Ravi Chandra Aswin output should be : RCA
if input like Ravi only output should be : Ravi
'''

String=input("Enter any String : ")

result=''

count_space=0
for i in String:
    
    if i==' ':
        count_space += 1
    
for j in String:
    if count_space>0:
        if j.isupper():
            result += j
    else:
        print(j,end='')
print()
        
print(result)

print("-------Other way----------")

str1=String.split()
str2=''
for j in str1:
    str2=str2+j[0]
print(str2)