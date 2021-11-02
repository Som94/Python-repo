'''

1) check whether source exists - if it exists goto step 3 otherwise goto step 2

2) display a msg source does not exists . STOP

3) check whether the target file exists - if it exists goto 4 step otherwise goto step 5 

4) display a msg warning the user - that the file will be OVERWRITTEN with new contets.

   if user say YES then goto STEP 5 otherwise STEP 6

5) read the source file , write it into the target file. display the msg once done

   'Copying of the file is successful'

6) [4] ....copying cannot be done as the user has not given the consent to overwrite the

   existing file

'''

import os,sys

my_current_working_path='E:\\Aroha Tech\\3rd Aug\\File handling\\'

source = input('enter the source file name ')   

source = my_current_working_path+source

print (source)

if os.path.isfile(source):

    target = input('enter the target file name ')  

    target = my_current_working_path+target

    print ('target file details ',target)

    if not os.path.isfile(target):

        s = open(source,'r')

        t = open(target,'w')

        src = s.read()

        print ('src is ', src)

        t.write(src)

        print ('file copied successfully ')

        s.close()

        t.close()

   

 