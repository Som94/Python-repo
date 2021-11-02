'''
data2= (19,100,356,-19,789,45,500,525,89,-19,622,651,25,-19,50,650)

Sum only the 3 digits number

Note while adding the 3 digits number , ignore all the 3digit number in the range of 450 to 650

While processing when 2 times -19 is encountered then :: STOP, come out and display the

Sum
Avg
Highest number
Lowest number

'''

data2= (19,100,356,-19,789,45,500,525,89,-19,622,651,25,-19,50,650)
list1=[]
count=0
for i in data2:
    
    if i== -19:
        count +=1
    
    if i>99 and i<1000 and not(i>=450 and i<=650):
        list1.append(i)
    if count==2:
        break
list1.sort()
print("Sum of all positive  3 digit numbers : ",sum(list1))
print("Avarage : ",sum(list1)/len(list1))
print("The highest number is : ",list1[len(list1)-1])
print("The lowest number is : ",list1[0])        