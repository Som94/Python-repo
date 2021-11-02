import pandas as pd

df=pd.read_csv('E:\Aroha Tech\Python Session\game.csv')

#print(df)

class Game:
    def __init__(self,points,chances):
        self.points=points
        self.chances=4
        
    def level1(self):
        if self.points>=100 and self.chances>0:
            print("You clear Level 1")
            self.level2()
            return True
           
        if self.points<100:
            print("Input the point value again..You ar e not reach that point..")
            #self.chances -= 1
        if self.chances<=0:
            print("Game Over")
            return False
        
    def level2(self):
        if self.points>150 and self.chances>0:
            print("You clear Level 2:")
            
        
        if self.chances<=0:
            print("Game Over")
        
        
    def level3(self):
        if self.points>200 and self.chances>0:
            print("You clear Level 3:")
        if self.chances<=0:
            print("Game Over")
    
        
    def level4(self):
        if self.points>300 and self.chances>0:
            print("You clear all levels:")
            print("Congradulations You are the winner")
        if self.chances<=0:
            print("Game Over")
     
    
flag=True      

   

chances=4 
while chances>0:
    point=int(input("Enter your point value :"))
    Game(point,chances).level()

    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            