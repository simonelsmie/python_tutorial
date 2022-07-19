charlie = {
    "name": "Charlie",
    "age": 40,
    "wallet": 0,
    "salary": 1000,
    "items": []
}

print(charlie["age"])

charlie["wallet"] += 20
# print(charlie["wallet"])

print(charlie["items"])
charlie["items"].append("phone")
print(charlie["items"])


# These are very seperated, what if we could closely link dictionaries and methods?
# Classes

# Let's create a Person class, with properties for name, age, wallet, salary and items

# Let's print each property to ensure it is working

# Let's create a class method to add the salary into the person's wallet. Let's "get_paid"

# Let's create a class method to increment the age by 1, to indicate a birthday

# Let's create a class method to add different items to the items list on the person object