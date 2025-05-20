from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        
        self._customer = customer
        self._coffee = coffee
        
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._price = price
        
       
        customer._orders.append(self)
        coffee._orders.append(self)
    
    @property
    def customer(self):
       
        return self._customer
    
    @property
    def coffee(self):
        
        return self._coffee
    
    @property
    def price(self):
    
        return self._price