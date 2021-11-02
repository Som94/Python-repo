'''
Given a lst1 = [23,78,45,23,66,23,12,23,50,23,23,23,99,23]
Find out how many 23 are there. And remove all the 23 except the one shown above in highlighted way

'''
lst1 = [23,78,45,23,66,23,12,23,50,23,23,23,99,23]

print('The Number of occurrences of 23 in lst1 is :',lst1.count(23))

lst2=lst1[:5:]

lst3=lst1[6::]

lst4=[lst1[5]]

lst5=[]

for i in lst2:
    if i !=23:
        lst5.append(i)

lst5=lst5+lst4

for j in lst3:
    if j !=23:
        lst5.append(j)

print('After removing all 23 except marked one :',lst5)