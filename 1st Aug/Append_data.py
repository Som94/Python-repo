#Append_data.py

 

 

print ('enter the file name ')

fname = input()

f = open(fname,'a+')

print ('enter some text .....or type QUIT to STOP ')

while True:

    txt = input()

    if (txt == 'QUIT'):

        break

    f.write(txt)

    f.write('\n')

f.close()

f = open(fname,'r+') 

f1 = open('temp1.py','w') 

for i in range(0,10):

    line_numb = f.readline()   

    print (i,' ',line_numb,end='')

    f1.write(line_numb)

 

   

for i in range(10,11):

    line_numb = f.readline() 

    

    new_str = 'prod1 = int(p1)*int(p2)'   

    f1.write(new_str)

    f1.write('\n')

   

for i in range(11,15):

    line_numb = f.readline()   

    print (i,' ',line_numb,end='')   

    f1.write(line_numb)

 

 

 

#new_str = 'prod1 = int(p1)*int(p2)'

#f.write(new_str)  

f.close()

f1.close()