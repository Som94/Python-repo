'''
Create the Product cost where in you pass the selling price and cost price
Display the appropriate message

 

Selling price – cost price is Profit , display the profit and profit percentage

 

Cost Price – Selling Price is Loss, display the loss percentage
'''


class Product:
    
    def __init__(self,selliing_price, cost_price):
        self.selliing_price=selliing_price
        self.cost_price=cost_price
    
    def calculation(self):
        
        if self.selliing_price>self.cost_price:
            
            print("Profit on selling is :",self.selliing_price-self.cost_price)
            print("Profit percentage on selling is :",100*((self.selliing_price-self.cost_price)/self.cost_price))

        else:
            print("Loss on selling is :",self.cost_price-self.selliing_price)
            print("Loss percentage on selling is :",100*((self.cost_price-self.selliing_price)/self.cost_price))
    
calc=Product(122,130)
calc.calculation()

            