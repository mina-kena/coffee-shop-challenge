class Coffee:
    def __init__(self, name):

        self.name = name
        self._orders = []
    
    def orders(self):
        
        return self._orders
    
    def customers(self):
        
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
       
        return len(self._orders)
    
    def average_price(self):
        
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
    