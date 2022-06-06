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


# Updating values


# Adding a new key-value pair


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

# print(list(meal_plan))

# Print tuesday's dictionary


# Print wednesday's dinner value


# Add thursday's meal plan with something for breakfast, lunch and dinner


friday = {
    "breakfast": "eggs",
    "lunch": "salad",
    "dinner": ["sausages", "hamburger", "potatoes", "icecream"]
}

# Add this dictionary onto the meal plan. Notice that the dinner is a list of strings
# How would you print the value icecream based on it's location in the dictionary?

