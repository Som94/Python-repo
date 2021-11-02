import user_validation 
import Admin_class
import pandas as pd

class First_time_login:
    
    def change_password():
        
        while True:
            
            pw_change=input("Enter a password of length 8 for updation:")
            
            if len(pw_change)>=8:
                
                Admin_class.mycursor.execute("update User_Details set Password=%s  where User_id=%s",(pw_change,user_validation.uid))
                Admin_class.conn.commit()
                
              # Admin_class.mycursor.execute("update User_Details set Password='{}' where user_id='{}';".format(pw_change,user_validation.uid), user_validation.engine)
                print("Password Updated sucessfully..")
                break
            else:
                print("Password length doesn't match.. Try Again ")
               
class Other_login:
    
    
    
    def User_all_details():
        
        
        all_details=pd.read_csv(r'E:\Aroha Tech\user_view_details.csv')
        print(all_details[['mobile','email ID','name','alternate\nmobile number','address','qualification','hobbies']])
    
        
        
        
    def User_short_details():
        all_details=pd.read_csv(r'E:\Aroha Tech\user_view_details.csv')
        print(all_details[['alternate\nmobile number','address']])
    
    
