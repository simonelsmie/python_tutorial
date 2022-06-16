# Create a function that takes in an argument of fruit, so that it will print "You're favourite fruit is " followed by the fruit provided.
# Make sure to call this function a few times with different parameters given so that we see the string printed with different fruit.
# >> Define function here
from audioop import add


def fruit_picker(fruit):
    print("Your favourite fruit is " + fruit)

fruit_picker("Apples")


# Create a function that can add two integer values together that are provided as arguments.
# Print this value so that we can see the total of the two integers added together.
# >> Define function here
def addition(num1, num2):
    print(num1 + num2)

addition(5, 2)
addition("5", "2") 
# Strings so concatinated


# Create a function that can take an argument of name and of time of day, so that the printed value could show "Good morning Dan" for example
# >> Define function here
def greeting(name, time):
    print("Good " + time + ", " + name)

greeting("Dan", "morning")



# Please feel free to create other functions, including other math operators.
# If you would like a challenge then you could use the in-build function of input() to get a bit more interaction as shown below:
def test_name():
    name = input("What is your name? \n")
    print("This is just a test, but hello " + name)

test_name()
# Give this a try and see how it displays in your terminal, as it will wait for some input there.
# You could add complexity to have conditional logic occuring if the input is equal (or not) to a set value.




