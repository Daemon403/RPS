import random
def game(my_choice,computer_choice):
    if my_choice == "Rock" and computer_choice == "Scissors":
        print("Player ({}) : CPU ({}). You won".format(my_choice, computer_choice))
    elif my_choice == "Paper" and computer_choice == "Rock":
        print('Player ({}) : CPU ({}). You won'.format(my_choice, computer_choice))
    elif my_choice == "Scissors" and computer_choice == "Paper":
        print("Player ({}) : CPU ({}). You won".format(my_choice, computer_choice))
    elif my_choice == computer_choice:
        print("Player ({}) : CPU ({}). NOBODY won".format(
            my_choice, computer_choice))
        gameplay()
    else:
        print("Player ({}) : CPU ({}). Computer won".format(my_choice, computer_choice))
        
possibilities = ["Rock","Paper","Scissors"]
def gameplay():
    my_choice =""
    while my_choice not in possibilities:
        my_choice = input('Please select your option. Enter either R, P or S: ')
        my_choice = my_choice.upper()
        if my_choice == 'R': my_choice = "Rock"
        elif my_choice == "S": my_choice = "Scissors"
        elif my_choice == "P": my_choice = "Paper"
    computer_choice = random.choice(possibilities)
    game(my_choice, computer_choice)

gameplay()