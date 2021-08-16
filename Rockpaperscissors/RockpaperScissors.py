import random
def check_valid(user_action):
    possible_actions = ["rock", "paper", "scissors"]
    if user_action not in possible_actions:
        print('Invalid_move')


def check_winner(cpu,player):
    if cpu == player:
        print('CPU  ||  player')
        print(f' {cpu}        {player}')
        print("it's a tie")

    elif cpu > player:
        print('CPU  ||  player')
        print(f' {cpu}       {player}')
        print("machine prevails")
    else:
        print('CPU  ||  player')
        print(f' {cpu}        {player}')
        print("You've won!!")


while True:
    cpu = 0
    player = 0
    user_action = input("Enter a choice (rock, paper, scissors): ")
    user_action = user_action.lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            player+=1
        else:
            print("Paper covers rock! CPU wins!.")
            cpu+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            player+=1
        else:
            print("Scissors cuts paper! CPU wins!.")
            cpu+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            player+=1
        else:
            print("Rock smashes scissors! CPU wins!.")
            cpu+=1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

check_winner(cpu,player)