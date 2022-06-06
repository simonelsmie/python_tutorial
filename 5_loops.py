# Iteration using for and while loops
# Counters

# While loops
# This type of loop will continue indefinitely while a condition is true

counter = 0

while (counter < 5):
    # print(counter)
    counter = counter + 1


# def guessing_game():
#     my_number = 5
#     value = int(input("What number am I thinking of? "))

#     while (value != my_number):
#         value = int(input("Try again... : "))
#     print("Yes")

# guessing_game()

# Breaking out of while loops
# def break_out_of_loop():
#     while (True):
#         line = str(input("Type anything: "))
#         if line.lower() == "q":
#             break
#         print("you typed " + line)

# break_out_of_loop()


# For loops only iterate for the length of the list
numbers  = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * number)
    

# How would we total all the numbers in numbers?


