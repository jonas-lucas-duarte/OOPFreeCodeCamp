'''

item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1)) # str
print(type(item1_price)) # int
print(type(item1_quantity)) # int
print(type(item1_price_total)) # int

'''

class Item:
    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

'''

print(type(item1)) # __main__.Item
print(type(item1.name)) # str 
print(type(item1.price)) # int
print(type(item1.quantity)) # int

'''
