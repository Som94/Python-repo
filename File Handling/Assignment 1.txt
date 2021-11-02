'''
Create a file and write into 10 lines,
And append these 10 lines into a list
'''


file=open("demo.txt",'w')
file.write('''1.Today is Friday
2.Tommoro is Saturday
3.Then Sunday
4.Then Monday
5.Then Tuesday
6.Then Wednusday
7.Then Thursday
8.Reapet Friday
9.This Cycle 
10. Going to be always''')
file.close()

f=open('demo.txt','r')
read=f.readlines()
lst1=[]
for line in read:
    lst1.append(line)
    #print(line)
f.close
print('After appending all lines from demo.txt file into the list :',lst1)