
def computation(distance , mileage , vehi_type, petrol=105,diesel=95):

    total_fuel_consumed = distance/mileage

    total_fuel_cost = 0

    if (vehi_type == 'P'):

        total_fuel_cost = petrol * total_fuel_consumed

    elif (vehi_type == 'D'):       

        total_fuel_cost = diesel * total_fuel_consumed

    return total_fuel_cost       

 

def display(tot_fuel_cost):

    print ('Total fuel cost is ',tot_fuel_cost,' INR')   

    

    

print ('i am in the main BLOCK')

total_fuel_cost  = computation(100,10,'P')

display(total_fuel_cost)

total_fuel_cost  = computation(100,10,'D',diesel=100)

display(total_fuel_cost)

 

 

#Gold_silver.py

 

def billing(qty_gold,qty_silver,gold=44900,silver=666):

    gold_bill = qty_gold * gold

    silver_bill = qty_silver * silver

    total_bill = gold_bill + silver_bill

    return gold_bill,silver_bill,total_bill

 

 

print ('i am in main BLOCK') 

isAllOk = True

try: 

    g,s =input ('Do you wish to buy Gold and Silver both in blocks of 10gms ? ').split(',')

    print (g)

    print (s)

    gold_qty = 0

    silver_qty = 0

except ValueError:

    print ('your inputted data is not right !! ')

    isAllOk = False

   

if isAllOk:

    try:

        gold_qty = int(g[g.index('=')+1:])

    except ValueError:

        gold_qty=0

       

    try:    

        silver_qty =int(s[s.index('=')+1:])   

    except:

        silver_qty=0

   

    print (gold_qty)

    print (silver_qty)

   

    bills = billing(gold_qty,silver_qty,silver=700)

    for i in bills:

        print ('i is ',i)

 

print ('thank you ')