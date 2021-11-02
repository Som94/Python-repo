'''

input ten 2 digits numbers, and store them into a tuple.
display 1 by 1 and at same time remove the element.
find the total of first 8 numbers only.
'''
list_num=[]
count=0
sum_of_8=0

flag=True
while flag:
    
    number=int(input("Enter two digit Number :"))
   
    if number>9 and number<100:
        list_num.append(number)
    else:
        print("Enter Two digit number only..")
    
    
    #print(list_num)
    #print(len(list_num))
    if len(list_num)>=10:
        flag=False
 
list_num1=list_num.copy()

len_list_num=0
while len(list_num)>len_list_num:
    print('The Element is :',list_num[len_list_num])
           
    print("Remove :",list_num1.pop(len_list_num-len(list_num)))
    
    len_list_num=len_list_num+1
     
print("Sum off first 8 numbers is :",sum(list_num[:8]))
print('Ten 2 digit numbers of tuple :',tuple(list_num))

    

