traveller = [
    {
        "name": "Rick",
        "items": [],
        "packed": False,
        "cash": 200
    },
    {
        "name": "Bob",
        "items": [],
        "packed": False,
        "cash": 150
    },
    {
        "name": "Ang",
        "items": [],
        "packed": False,
        "cash": 300
    },
]

wardrobe = [
    {
        "description": "shirt",
        "colour": "white"
    },
    {
        "description": "jeans",
        "colour": "blue"
    },
    {
        "description": "chinos",
        "colour": "brown"
    },
    {
        "description": "t-shirt",
        "colour": "black"
    },
    {
        "description": "t-shirt",
        "colour": "cyan"
    },
    {
        "description": "socks",
        "colour": "red"
    },
    {
        "description": "socks",
        "colour": "white"
    },
    {
        "description": "belt",
        "colour": "tan"
    },
    {
        "description": "shoes",
        "colour": "black"
    },
    {
        "description": "shoes",
        "colour": "white"
    }
]

# Write functions for each of the following, that will print to the screen. 
# Remember to call the function so that it will work when you run the file

# Three friends are about to go on one night trip aaway together. No one has packed. Let's get started!

# 1. Create a function to show the dictionary of traveller named Bob


# 2. Create a function that will show if Ang has packed


# 3. Rick decides he want's to take his white shirt, red socks, blue jeans and wear his white shoes.
# Add these too Rick's items. REMEMBER you will need to add each item one at a time


# 4. Now that you have added the clothes to Rick's item list, change the boolean value of packed to True


# 5. Select clothes for Ang and Bob and add them to their items lists, then change their packed status to True


# 6. Now that all three have packed, they decide to make sure they have enough money for their big night.
# Using a counter total the amount of cash they have.


# 7. With enough cash for their hotel and expenses they are ready to go. 
# WAIT.... Who is driving?
# Add to Ang a new key value pair of driver with the value of True


# 8. With Ang confirmed as the driver, add a new key value pair to Ang for car_keys set to False


# 9. Now that we know Ang is the driver, we want to confirm we are all ready now
# Iterate through the list to confirm that each traveller has items in their list
# using the in build len() function you can confirm whether their list of items is greater than 0


# 10. If all have items in their bags, let's change car_keys to True for Ang



# Extension

# 11. Let's do a final check and confirm we are all packed and have car keys. 
# After iterating through the travellers to confirm everyone has packed, let's also confirm we have car keys.
# To do this you will need to iterate through the travellers looking for the key "car_keys" in their dictionary objects
# e.g. if "car_keys" in traveller:
#           do_something...
# 
# If all are packed, and we have car keys, print to the screen "Let's GO!"


