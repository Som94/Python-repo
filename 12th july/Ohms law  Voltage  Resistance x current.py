'''
5.

Ohms law :  Voltage = Resistance x current
Let say current is  30 amps vary the resistance from  10 ohms by steps of 5 for next 8 readings display the voltage

 

 '''
 
 
current=30
resistance=10
readings=8
while readings>0:
    
    Voltage=resistance*current
    resistance += 5
    print(Voltage) 
    readings -= 1


 
