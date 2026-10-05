import random

while True:
    user_action = input("enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper","scissors"]
    computer_actions = random.choice(possible_actions)

    if user_action == computer_actions:
        print(f"both players selected {user_action}. it's a tie!")
    elif user_action == "rock":
        if computer_actions == "scissors":
            print("rock smashes scissors! you win!")
        else:
            print("paper covers rock! you lose!")
    elif user_action == "paper":
        if computer_actions == "rock":
            print("paper covers rock! you win!")
        else:
            print("scisssors cuts paper! you lose!")
    elif user_action == "scissors":
        if computer_actions == "paper":
            print("scissors cuts paper! you win!")
        else:
            print("rock smashes scissors! you lose!")
    play_again = input("play again? (y/n): ")
    if play_again != "y":
        break  