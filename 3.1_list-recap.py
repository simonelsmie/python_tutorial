# 1. Make an empty list
names = []
# name = list()

# 2. Add 5 strings to the list
names.append("Matt")
names.append("Mike")
names.append("Adela")
names.append("Graeme")
names.append("Antony")

# print(names)


# 3. Print off index 2 and index 4 of the list
# print(names[2])
# print(names[4])


# 4. Remove the item at index 3 and the print the list
# names.pop(3)
# names.remove("Graeme")
# print(names)


# 5. Combine your list and this one ["one", "two", "three"]
list_2 = ["one", "two", "three"]
bigger_list = names + list_2
# print(bigger_list)

names.extend(list_2)
print(names)
