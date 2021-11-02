import pandas as pd

df=pd.read_csv('E:\Aroha Tech\Python Session\game.csv')

#print(df.iloc[:,0][1])


#print(df.iloc[:,1][1])



def level1(chances = df.iloc[:,1][0] ):
    print("Welcoom to Level 1 \n")
    print("You have only",df.iloc[:,1][0]," chances")
    while chances>0:
        points=int(input("Enter point :"))
        if points>=df.iloc[:,0][0] and chances>0:
            print("Congratulations \n")
            print("You clear Level 1 \n")
            print("Your going to enter level 2 \n")
            level2()
            return True
              
        if points<df.iloc[:,0][0]:
            print("Input the point value again..You ar e not reach that point..\n")
            chances =chances - 1 
            
            print("Remaining chances is :",chances)
    if chances<=0:
        print("Game Over")
        return False
            
def level2(chances = df.iloc[:,1][1] ):
    print("Welcoom to Level 2 \n")
    print("You have only ",df.iloc[:,1][1]," chances")
    while chances>0:
        points=int(input("Enter point :"))
        if points>=df.iloc[:,0][1] and chances>0:
            print("Congratulations \n")
            print("You clear Level 2 \n")
            print("Your going to enter level 3 \n")
            level3()
            return True
              
        if points<df.iloc[:,0][1]:
            print("Input the point value again..You are not reach that point..\n")
            chances =chances - 1 
            
            print("Remaining chances is :",chances)
    if chances<=0:
        print("Game Over")
        return False
        
def level3(chances = df.iloc[:,1][2] ):
    print("Welcoom to Level 3 \n")
    print("You have only ",df.iloc[:,1][2]," chances")
    while chances>0:
        points=int(input("Enter point :"))
        if points>=df.iloc[:,0][2] and chances>0:
            print("Congratulations \n")
            print("You clear Level 3 \n")
            print("Your going to enter level 4 \n")
            level4()
            return True
              
        if points<df.iloc[:,0][2]:
            print("Input the point value again..You ar e not reach that point..\n")
            chances =chances - 1 
            
            print("Remaining chances is :",chances)
    if chances<=0:
        print("Game Over")
        return False
        
def level4(chances = df.iloc[:,1][3]):
    print("Welcoom to Level 4 \n")
    print("This is the Final level and You have ",df.iloc[:,1][3]," chances in this level..So Play carefully")
    points=int(input("Enter point :"))
    if points>=df.iloc[:,0][3]:
        print("Congratulations \n")
        print("You clear all the Levels \n")
        print("Thanks for playing... \n")
                    
    else:
        print("Game Over")
        print("Better luck next time..")
        


level1()
