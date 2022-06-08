# What are conditionals?
# 
# Based on true or false / yes or no answers
# We provide a statement that must be evalutated as a true of false
# True or false are representative of binary 1 and 0

#Equality
# = assignment
# == equality
# !=  not equal


def two_plus_two_four():
    if (2 + 2 == 4):
        print(True)

# two_plus_two_four()

def equals_five():
    if (2 + 2 == 5):
        print(True)
    else:
        print(False)

# equals_five()

# Greater/Less Thans
def greater_than_100(number):
    if 100 < number:
        print(True)
    elif 100 == number:
        print("Equal")
    else:
        print(False)


# greater_than_100(500)
# greater_than_100(5)
# greater_than_100(100)

# print(1,type(1))
# print(True, type(True))
# print("True", type("True"))












def do_these_equal_four():
    if 4 == 2 + 2:
        print(True)

# do_these_equal_four()


def do_these_equal_four_v2():
    if 4 == 2 + 3:
        print(True)


# do_these_equal_four_v2()

# Greater/Less Thans
def greater_than_100(number):
    if 100 < number:
        print(True)
    else:
        print(False)


# greater_than_100(101)
# greater_than_100(5)

#Greater/Less Than or Equals
def is_greater_or_less_or_equal(number1, number2):
    if number1 > number2:
        return "Number 1 is larger", True
    else:
        return "Number 2 is larger", False


# print(is_greater_or_less_or_equal(45, 60))
# is_greater_or_less_or_equal(73, 20)
# is_greater_or_less_or_equal(35, 35)

# Comparing strings
def do_these_match(string1, string2):
    if string1 == string2:
        print(True)
    else:
        print(False)


do_these_match("dog", "dog")
do_these_match("cat", "dog")
do_these_match("1", "1")
do_these_match("Dog", "dog")
do_these_match("1", 1)
