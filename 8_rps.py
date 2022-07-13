import random

# Rock paper scissors 1vC
def rps_game():
    # 1. Get player name
    name = input("What is your name?: ")

    # 2. Get player's choice
    # choice = input("Hello " + name + ", what is your choice?: ")
    valid = False
    while (valid == False):
        choice = input(f"Hello {name}, what is your choice? (rock, paper or scissors): ").lower()
        if choice == "rock" or choice == "paper" or choice == "scissors":
            valid = True

    # 3. Get computers's choice
    possible_choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choice)

    # 4. Evaluate choices to determine winner
    options_for_player_win = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    # options_winner = {
    #     "rock": "scissors",
    #     "scissors": "paper",
    #     "paper": "rock"
    # }

    if computer_choice == choice:
        result = "It's a draw"
    if options_for_player_win[computer_choice] == choice:
        result = f"{name} is the winner!"
    else:
        result = "The computer is the winner"

    # 5. Display outcome
    print(f"Computer has chosen {computer_choice}")
    print(f"{name} has chosen {choice}")
    print(result)

rps_game()