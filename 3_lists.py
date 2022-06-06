# List / Arrays
# Denoted using  square brackets
# Ordered
# Should only contain single type inputs, e.g. only strings or integers etc.
# List of names, or lotter numbers

# Accessing lists
fruit = ["apple", "banana", "kiwi", "pear", "grape"]

# Print the list


# Indexes - what are they and where do they start from


# Print off pear by the index of fruit


# Indexing from the end of the list


# Update an entry in the list
# Change Banana to Mango


# Create an empty list
new_list = []
# or new_list = list()

# List functions
# Adding to a list - using append
# print(new_list)
new_list.append("keyboard")
# print(new_list)

# Removing from the end of a list - using pop
# print(new_list)

# print(new_list)

## You can remove items by their value - using remove
fruit.remove("grape")
# print(fruit)


# Adding lists
combined_list = fruit + new_list
# print(combined_list)

# Extending Lists
fruit2 = ["peach", "orange", "dragonfruit"]
fruit.extend(fruit2)
# print(fruit)


nested_list = [1,2,3,4,[5,6,7]]
# print(nested_list)