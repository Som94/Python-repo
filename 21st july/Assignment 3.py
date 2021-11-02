'''
Given a data1 = [10,20,151,30,55,23,199,-23,-33,221,44,55,19,-13]

 

Write the following function to process the list (use data1 )
display()

delete() – to remove all the negative numbers

total()   - which adds all the 2 digits number (while ignoring 44,55)

findAvg() – finding the avg of last 5 numbers from the end of the list (negative numbers excluded out)

findHigh() – finding the highest from start of the list till the middle element of the list

'''

data1 = [10,20,151,30,55,23,199,-23,-33,221,44,55,19,-13]


def display(data1):
    
    for i in data1:
        print(i)
    print(data1)   
display(data1)

 
def delete(data1):
    for i in data1:
        
        for j in range(len(data1)-1):
            if data1[j]<0:
                del data1[j]
                
    print("After deleting all -ve numbers :",data1)
    
delete(data1)


def total(data1):
    total1=0
    for i in data1:
        if i>9 and i<100 and i != 44 and i != 55:
            total1 += i
    print("Addition of all 2 digit number except 44 and 55 is :", total1)
total(data1)   

  
  
def findAvg(data1):
    sum1=0
    for i in data1[-1:-6:-1]:
        #print(i)
        sum1 += i
    print("Average of last 5 numbers is :", sum1/5)

findAvg(data1)

def findHigh(data1):
    data2=data1[:len(data1)//2]
    #print(data2)
    print('the highest from start of the list till the middle element of the list :',max(data2))
    
findHigh(data1)
    

    