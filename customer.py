class Customer:
    def __init__(self, name):

        self.name = name
        self._orders = []
    
    def orders(self):
        
        return self._orders
    
    def coffees(self):
       
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        
        from order import Order
        return Order(self, coffee, price)