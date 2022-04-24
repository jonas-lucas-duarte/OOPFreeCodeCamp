import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instance_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item.get('name'),
                 price=float(item.get('price')),
                 quantity=int(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

# SUPER

class Phone(Item):
    #all = []

    '''
    def __init__(self,name:str,price:float,quantity=0, broken_phones=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} os not greater than or equal to zero!"

        self.name=name
        self.price=price
        self.quantity=quantity
        self.broken_phones=broken_phones

        Phone.all.append(self)

    '''

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        self.broken_phones = broken_phones

        #Phone.all.append(self)

# PARENT CLASS > CHILD CLASS

phone1 = Phone("jscPhonev10", 500, 5)
#phone1.broken_phones = 1
#print(phone1.calculate_total_price())
#phone2 = Phone("jscPhonev20", 700, 5)
#phone2.broken_phones = 1

print(Item.all)
print(Phone.all)

