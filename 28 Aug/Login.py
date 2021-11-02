
import boto3
import pandas as pd
s3_client=boto3.client('s3')
file=s3_client.get_object(Bucket='som-aws-bucket-1',Key='Admin_userid_password.csv')
file_df=pd.read_csv(file['Body'])
user_id=file_df.iloc[0,0]
password=file_df.iloc[0,1]


from Admin_class import Admin as a

import user_validation 
import Valid_user_login # First_time_login,Other_login
from datetime import datetime
date_and_time=datetime.now()

time=int(date_and_time.strftime('%H'))
print(time)


#user_id='somnath'
#password='somnath123'


def login():
       
    if time>0 and time < 12 :
        print("Good Morning")
            
    if time >= 12 and time < 17:
        print("Good Afternoon")
    if time >= 17 and time < 21:
        print("Good Evening")
     
    print("Wellcome, Please Login ..")
    
    while True:
        type_of_login=int(input("Enter What's Your Login type :\n 1. Admin login \n 2. User Login \n 3 Quit\nEnter your choice :"))
        
        
        if type_of_login==1:
            print("Admin Login")
            count=3
            while count>0:
                
                admin_user_id=input("Enter admin user id :")
                admin_password=input("Enter password :")
                if admin_user_id==user_id:
                    if admin_password==password:
                        print("You Successfully Login..")
                                            
                                            
                        while True:
                            #print("You successfully login..")
                            
                            choice=int(input("""
                                           1. Create a New User\n
                                           2. Retrive the user details\n
                                           3. Delete\n
                                           4. To Active\n
                                           5. To Deactive\n
                                           Enter ypur choice which operation you want to perform :"""))
                                           
                            if choice==1:
                                a.create_new_user()
                            if choice==2:
                                a.user_view() 
                            if choice==3:
                                a.delete_user()
                            if choice==4:
                                a.Active()         
                            if choice==5:
                                a.Deactive()
                                
                            
                            wish=input("Do you want perform any operation again y/n :")
                            
                            if wish=='n':
                                break
    
                        
                        break
                    else:
                        print("Password doesnot match..")
                        count=count-1
                else:
                    print("Admin User id doesn't match")
                    count=count-1
                print("Try Again..")
                print("Remember you have only {} remaining chances..".format(count))
                if count==0:
                    print("You cross the login limits")
                    
                    
        if type_of_login==2:
            
            print("User Login")
            count1=3
            while count1>0:
                if user_validation.valid_user():
                    #print(user_validation.d)
                    #print(user_validation.pd.read_sql_query("select * from User_Details where user_id={};".format(user_validation.valid_user.uid), user_validation.engine)
                    
                    
                    
                    if user_validation.d<3:
                        
                        if user_validation.pw_len<= 6:
                            Valid_user_login.First_time_login.change_password()
                            
                            
                    else:
                        while True:
                            choice1=int(input("1. All details \n 2. Short Details\n 3.Logout \n Enter Your choice :"))
                            if choice1==1:
                                Valid_user_login.Other_login.User_all_details()
                                
                            if choice1==2:
                                Valid_user_login.Other_login.User_short_details()
                            if choice1==3:
                                print("Logout Successfully..")
                                break
                            wish=input("Do you want perform any operation again y/n :")
                            
                            if wish=='n':
                                break    
                    break        
                else:
                    print("It's not a valid user id ")
                    count1 -= 1
                    print("Remember you have only {} remaining chances..".format(count))
                    
            print("You cross the login limit")        
        if type_of_login==3:
            print("You Quit")
            print("Thanks for visiting..")
            break
        else:
            print("Please Enter a valid input only..")
login()
    
