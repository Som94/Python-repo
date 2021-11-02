'''
Input a name of the file. If it exists, then read only half of the contents of the file.
Use error handling if the file does not exists and display the appropriate message.

Find out the following:-

 

How many vowels are there in the read data?
How many words are there ?
Given (say) a set with bad words
Assume bad_word_set = { ‘word1’, ‘word2’,’word3’ ………………….}

Find out from the read data of the file how many matched the bad word set

Copy the second half of the file into the target file
If the source file was called  story_1.txt then the target file should be automatically names

The source file + the ‘_target’   so story_1_traget.txt

Find out how many lines are there in the source files
Display the last 2 lines of the source file and store each word of those in the dictionary like shown below
Suppose the total lines in the files are  20 then the dictionary looks like this

KEY                   VALUE

“line_19”  :  [….list of words ………….]

“line_20”  : [….list of words ………….]

 

 

Find out if the source file which you gave is hidden – then what happens ?

 
'''
#import os,sys 

vowels_list=['a','e','i','o','u']

vowels_count=0

word_count=0
list_word=[]

count_lines=0

count_bad_word=0

bad_word_set = { 'word1', 'word2','word3','word4','word5','word6','word7'}

try:
    
    dir_name=input("Enter your Directory name :") #   E:\Aroha Tech\3rd Aug\File handling\
    file=input("Enter a file name :")             #     test1.txt
      
    #if os.path.isfile(file):      
           
    with open(dir_name+file ,'r', encoding="utf-8") as f:
        read_file=f.read()
        len_read_file=len(read_file)//2
        print('Total Length of the file :',len_read_file)
        
        with open(dir_name+file ,'r', encoding="utf-8") as f1:
            read_file1=f1.read(len_read_file)
            print(read_file1)
            
#--------------------Count vowels ------------------------------ 
            
            for vowel in read_file1:
                if vowel.lower() in vowels_list:
                    vowels_count += 1
            print("The number of vowels are :",vowels_count) 
            
#-------------------- Word Count ---------------------------------
            read_file_list=read_file1.split()
            #for word in read_file_list:
             #   if word.isalnum():
             #       word_count += 1
             #       list_word.append(word)
            print("The Number of Words are :",len(read_file_list))
            #print("The List Of words is :",read_file_list)
            
#--------------------- Bad Word------------------------------
            for word in read_file_list:
                if word in bad_word_set:
                    count_bad_word += 1
            print("The Nu,ber of Bad words are :",count_bad_word)
            
#----------------- Copy The 2nd half data of sourse file i to target file-----------------
            
            split_file=file.split('.')
            
            target_file=dir_name+split_file[0]+'_target.'+split_file[1]
            
            with open(target_file ,'w', encoding="utf-8") as f3:
                for i in range(len_read_file,len(read_file)):
                    f3.write(read_file[i])
                    
#-------------------- Count How many Lines --------------------------------
                    
            read_file_lines=read_file.split('\n')
            
            print('The number of lines are :',len(read_file_lines))

#----------------- Display last 2 lines of sourse file----------------------
            print("The Last 2 lines are :\n",read_file_lines[-2],'\n',read_file_lines[-1])
            
#-----------And Showing last 2 line with list of words as dictionary ---------------------
            
            dict_data={'line_'+str(len(read_file_lines)-i):read_file_lines[-1-i].split() for i in range(2)}
            
            print('The Last 2 lines as Dictionary :',dict_data)
                
            

except FileNotFoundError:
    print('Entered file doesnot exists in directory , Plz.. Try another one')


