'''
If input like Ravi Chandra Aswin output should be : RC Aswin
if input like Ravi only output should be : Ravi
'''


str1=input("Enter any string : ")

str2=str1.split()
str3=''
for i in range(len(str2)-1):
    #print(str2[i])
    str3=str3+str2[i][0]
print(str3+' '+str2[len(str2)-1])
    