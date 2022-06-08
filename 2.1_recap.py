# Recap
# Things of type String are anything encapsulated by quotation marks "Like this" - can be either single or double quotes, but they must be the same
# Integers are numerical values, whole numbers only, such as 1234
# Floats are also numerical values, however these are to the decimal point, such as 33.3
# Booleans are True or False
# Assignment is done from right to left using a singe equals sign =
# Equivalence is done using a double equals
# No equal is an exclamation mark and equals !=
# Normal operators can also be <, > or <=, >= etc
#
# When we want to use conditional logic we can do so using if else statements 
# (including elif - "else if" - which are the same as the if part of the statement)
# 
# In a statement if we wanted to have 3 possible outcomes we could use something like this: -
# if colour == "Red":
#   print("Red is a cool colour")
# elif colour == "Pink":
#   print("Pink is a great colour")
# else:
#   print("Pick a better colour...")
#
# As you recall the colon character : is required at the end of the line after a statement, and also after defining a function
#
# Functions are defined using def before the function name
# The function is follow by brackets () in which you can place an argument/parameter that would be used during the function
# These argument/parameters can be named anything and can be as many as required
# They should always be seperated by a comma as below: 
def hello(name, day):
    print("Hello " + name + ", today is " + day)

hello("Simon", "Wednesday")
# This will print "Hello Simon, today is Wednesday"


# Mathmatical operators
# We didn't touch on this, however we can apply normal math operators as follows
# Addition is done using a plus +
# Subtraction by a dash -
# Multiplication is done using a star *
# Division by a forward slash /
