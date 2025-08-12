class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class SpecialMenuItem(MenuItem):
    def __init__(self, name: str, price: float, discount: float):
        super().__init__(name, price)
        self.discount = discount

    def final_price(self) -> float:
        return self.price * (1 - self.discount)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def total(self) -> float:
        return sum(item.price for item in self.items)

pizza = SpecialMenuItem("Pizza", 12.5, 0.1)  # 10% off
pasta = MenuItem("Pasta", 10.0)

order = Order()
order.add_item(pizza)
order.add_item(pasta)

print("Total:", order.total())  # 22.5 (no discount applied here)
print("Pizza final price:", pizza.final_price())  # 11.25
