# List / Arrays
# Denoted using  square brackets
# Ordered
# Should only contain single type inputs, e.g. only strings or integers etc.
# List of names, or lotter numbers

# Accessing lists
fruit = ["apple", "banana", "kiwi", "pear", "grape"]

# Print the list
# print(fruit)

# Indexes - what are they and where do they start from


# Print off pear by the index of fruit
# print(fruit[3])
# print(fruit[0])
# print(fruit[1])

# Indexing from the end of the list
# print(fruit[-1])

# Length of a list
# print(len(fruit))

# Update an entry in the list
# Change Banana to Mango
fruit[1] = "mango"
# print(fruit)


# Create an empty list
new_list = []
new_list2 = list()

# List functions
# Adding to a list - using append
# print(new_list)
new_list.append("Adela")
new_list.append("Matt")
new_list.append("Mike")
# print(new_list)


# Removing from the end of a list - using pop
# new_list.pop()
# print(new_list)

# new_list.pop(1)
# Giving arguement replaces default of last place to that index value

## You can remove items by their value - using remove
fruit.remove("kiwi")
print(fruit)

# Adding/combining lists
combined_list = fruit + new_list
print(combined_list)

# Extending Lists
print(new_list)
new_list.extend(fruit)
print(new_list)


# Nested lists
nested = [1, 3, 4, [5, 6, 7]]