class ShoppingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
i1 = ShoppingItem('milk', 5.50, 3)
print (i1.total_price())
