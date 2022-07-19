class Person:
    def __init__(self, name, age, wallet, salary):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.salary = salary
        self.items = []

    def payday(self):
        self.wallet += self.salary

    def birthday(self):
        self.age += 1

    def add_item(self, item):
        self.items.append(item)
        