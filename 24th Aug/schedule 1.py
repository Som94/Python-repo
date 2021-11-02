import schedule
import time

def create_file():
    with open('schelude1.txt','w') as f:
        print("File created successfully...")

create_file()


schedule.every(0.30).minutes.do(create_file)
   
    
schedule.run_pending()
#time.sleep(1)