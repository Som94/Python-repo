#Read_files.py

 

 

f = open('Assignment 1.py', 'r')

data_str = f.read()

how = len(data_str)

print ('the file size is ',how)

print (data_str)

# after all the operation close the file

print ('----------------------')

try:

    f1 = open('Assignment 1.py', 'r')

    part_file = f1.read(20000)

    print ('part file is REVERSED ')

    print (part_file[::-1])

    f1.close()

except FileNotFoundError:

    print ('file does not exists. Pls check again')

 

f.close()

