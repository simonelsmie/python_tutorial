# Dictionaries / Objects
# Denoted by curly brackets 
# Key value pairs, seperated by commas
# {key: value}

# new_dict = {}
# new_dict = dict()

meals = {
    "breakfast": "scrambled eggs",
    "lunch": "BLT sandwich",
    "dinner": "fish and chips"
}

# print(meals)

# Print the value of breakfast
# print(meals["breakfast"])
# print(meals["dinner"])

# Updating values
# print(meals["lunch"])
meals["lunch"] = "tomato soup"
# print(meals["lunch"])

# Adding a new key-value pair
meals["desert"] = "chocolate cake"
# print(meals)


# Getting all keys in a dictionary
# print(list(meals))
# or 
# print(meals.keys())

# Getting all values
# print(meals.values())

# Nested dictionaries
meal_plan = {
    "monday": {
        "breakfast": "cereal",
        "lunch": "soup",
        "dinner": "pizza"
    },
    "tuesday": {
        "breakfast": "pancakes",
        "lunch": "humus",
        "dinner": "pasta"
    },
    "wednesday": {
        "breakfast": "fruit",
        "lunch": "sandwich",
        "dinner": "steak"
    }
}

# print(meal_plan)

# Print tuesday's dictionary
# print(meal_plan["tuesday"])


# Print wednesday's dinner value
# print(meal_plan["wednesday"]["dinner"])


# Add thursday's meal plan with something for breakfast, lunch and dinner
meal_plan["thursday"] = {}
# meal_plan["thursday"]["breakfast"] = "eggs"
meal_plan["thursday"] =  {
    "breakfast": "eggs",
    "lunch": "salad",
    "dinner": "sausages"
}

# print(meal_plan)


friday = {
    "breakfast": "eggs",
    "lunch": "salad",
    "dinner": ["sausages", "hamburger", "potatoes", "icecream"]
}

# Add this dictionary onto the meal plan. Notice that the dinner is a list of strings
# How would you print the value icecream based on it's location in the dictionary?
meal_plan["friday"] = friday
# print(meal_plan)

# print(meal_plan["friday"]["dinner"][3])


number1 = 123
number2 = "456"
number3 = "something"


# print(type(str(number1)))
print(float(number2))


# str(number1)
# number1 = 123 >>>>> "123"