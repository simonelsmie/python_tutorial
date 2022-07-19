from person import Person

charlie = {
    "name": "Charlie",
    "age": 40,
    "wallet": 0,
    "salary": 1000,
    "items": []
}

# print(charlie["age"])

charlie["wallet"] += 20
# print(charlie["wallet"])

# print(charlie["items"])
charlie["items"].append("phone")
# print(charlie["items"])


# These are very seperated, what if we could closely link dictionaries and methods?
# Classes

# Let's create a Person class, with properties for name, age, wallet, salary and items
claire = Person("Claire", 35, 0, 1100)

# Let's print each property to ensure it is working
# print(claire.name)
# print(claire.age)
# print(claire.wallet)
# print(claire.salary)
# print(claire.items)

# Let's create a class method to add the salary into the person's wallet. Let's "get_paid"
def pay_charlie():
    charlie["wallet"] += charlie["salary"]
    print(charlie["wallet"])

# pay_charlie()

claire.payday()

# def payroll(list_of_employees):
#     for employee in employees:
#         employee.payday()

# Let's create a class method to increment the age by 1, to indicate a birthday
# print(claire.age)
claire.birthday()
# print(claire.age)

# Let's create a class method to add different items to the items list on the person object
claire.add_item("birthday card")
claire.add_item("cake")
claire.add_item("party hat")
print(claire.items)
