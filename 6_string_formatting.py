# So far we have been adding strings together to print out to our terminals
name = "George"
number = 1
print("Hello " + name + " what's the weather with you?" + str(number))

# This is a bit slow to type out
# Instead we can format a string by placing the character f in front of the quotation marks
print(f"Hello")

# We can then add our variable name into the string using {}
print(f"Hello {name} what's the weather with you? {number}")

# This formatting will cast everything into a string type
# So even giving an integer, or boolean, will be converted to string

# print("hello " + number)
print(f"Hello {number}")