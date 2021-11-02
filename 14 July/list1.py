'''
given a list
data1 = [67,-2,23,10,34,-43,-20,-19,29,-99,89,22,-45,90,12,13,12,15, 25]

find the sum of all the positives numbers only
find the avg
find the highest, sec highest (ignore the negative number as mentioned above )
find the lowest  , sec lowest  (ignore the negative number as mentioned above )
 

Part B

Process ONLY the negative numbers

 

find the sum of all the negative numbers only
find the avg
find the highest, sec highest
find the lowest  , sec lowest
 

'''

data1 = [67,-2,23,10,34,-43,-20,-19,29,-99,89,22,-45,90,12,13,12,15, 25]
list1=[]
for i in data1:
    if i>=0:
        list1.append(i)
        
print('sum of all the positives numbers : ',sum(list1),'and avarage : ',sum(list1)/len(list1))        
list2=sorted(list1)
print(list2)
print("the highest, sec highest :", list2[len(list2)-1],list2[len(list2)-2])
print("the lowest  , sec lowest : ",list2[0],list2[1])


print("------for negative numbers--------")

list3=[]
for j in data1:
    if j<0:
        list3.append(j)
print('sum of all the positives numbers : ',sum(list3),'and avarage : ',sum(list3)/len(list3))        
list4=sorted(list3)
print(list4)
print("the highest, sec highest :", list4[len(list4)-1],list4[len(list4)-2])
print("the lowest  , sec lowest : ",list4[0],list4[1])
