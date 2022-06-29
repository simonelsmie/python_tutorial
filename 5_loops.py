# Iteration using for and while loops
# Counters

# While loops
# This type of loop will continue indefinitely while a condition is true

counter = 0

while (counter < 5):
    # print(counter)
    # counter = counter + 1
    counter += 1


# Guessing game
def guessing_number():
    condition = True
    while (condition):
        number = input("What is the number?: ")
        if number == "2":
            condition = False
        else:
            print("Guess again")
    print("You are right, the number was 2")


# guessing_number()

# Breaking out of while loops

def guessing_number_break():
    while (True):
        number = input("What is the number?: ")
        if number == "2":
            break
        else:
            print("Guess again")
    print("You are right, the number was 2")


# guessing_number_break()


# For loops only iterate for the length of the list
numbers  = [1, 2, 3, 4, 5]
def print_number():
    for number in numbers:
        print(number)
    

# print_number()

# How would we total all the numbers in numbers?
def square_number():
    for number in numbers:
        square = number * number
        print(square)


# square_number()

employees = [
    {"name": "Chuck", "age": 40, "service_years": 3},
    {"name": "Tom", "age": 60, "service_years": 15},
    {"name": "Sean", "age": 25, "service_years": 1},
    {"name": "Viola", "age": 36, "service_years": 5},
    {"name": "Serena", "age": 53, "service_years": 20},
]

def change_tom_service():
    for employee in employees:
        if employee["name"] == "Tom":
            employee["service_years"] = 14

# change_tom_service()

# print(employees)

# How can we find the total years of service for all employees?
def total_years():
    totals = 0
    for employee in employees:
        # totals = totals + employee["service_years"]
        totals += employee["service_years"]
    print(f"Total years is {totals}")
    # return totals

# total_years()
