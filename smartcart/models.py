class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, price, quantity)

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def update_quantity(self, name, quantity):
        if name in self.items:
            self.items[name].quantity = quantity
            if quantity <= 0:
                self.remove_item(name)

    def clear(self):
        self.items.clear()

    def get_total(self):
        return sum(item.price * item.quantity for item in self.items.values())