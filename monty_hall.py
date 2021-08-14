# Import dependencies

import matplotlib
import random
import pandas as pd

print("Welcome to the Monty Hall Problem!")
playstyle = input('Would you like to (1) play manually, or (2) run a simulation? (choose 1 or 2) ')

## Manual play
if int(playstyle) == 1: 
    print("Welcome to Let's Make a Deal!")

    # Create the choices (doors) and randomly shuffle them
    choices = ['donkey','donkey','car']
    random.shuffle(choices)
    # DEV ONLY: print the shuffled choices
    print(choices)

    # Ask the player to choose a door
    choice = input("Before you are three doors. Behind one of them is a new car. Behind the other two is a donkey. You will win whatever is behind the door you choose! Please choose a door (1, 2, or 3): ")
    # DEV ONLY: indicate which prize is behind the door (car or donkey)
    print(f'Chosen prize: {choices[int(choice) - 1]}')
    # Inform the player which door they have chosen.
    print(f'You have chosen Door #{choice}')
    # Open one of the non-selected doors. If a car is behind the selected door, then one of the two remaining doors with a donkey will be opened. If a donkey is behind the selected door, then the sole remaining door with a donkey will be opened. 
    print(f"Before we open Door #{choice}, let's open one of the doors that you did not choose!")
    if int(choice) == 1:
        # randomize which of the remaining doors 2 and 3 will be "checked" first. Remember that these are indexed at position 1 and 2 of the choices, respectively. Therefore, we create a list of the remaining doors, shuffle that list, then check the first door (index 0) of the shuffled list. If that door has a donkey, open it. If it does not, then open the door at index 1.
        other_doors = [1, 2]
        random.shuffle(other_doors)
        if choices[other_doors[0]] == 'donkey':
            print(f"We have opened Door #{other_doors[0] + 1}, which reveals a donkey! Good job dodging that one!")
            remaining_door = other_doors[1]
        else:
            print(f"We have opened Door #{other_doors[1] + 1}, which reveals a donkey! Good job dodging that one!")
            remaining_door = other_doors[0]
    if int(choice) == 2:
        # The same logic applies for door 2. The only change is that the other_doors list will have doors 1 and 3 (indexed at 0 and 2 respectively).
        other_doors = [0, 2]
        random.shuffle(other_doors)
        if choices[other_doors[0]] == 'donkey':
            print(f"We have opened Door #{other_doors[0] + 1}, which reveals a donkey! Good job dodging that one!")
            remaining_door = other_doors[1]
        else:
            print(f"We have opened Door #{other_doors[1] + 1}, which reveals a donkey! Good job dodging that one!")
            remaining_door = other_doors[0]
    if int(choice) == 3:
        # The same logic applies for door 3. The only change is that the other_doors list will have doors 1 and 2 (indexed at 0 and 1 respectively).
        other_doors = [0, 1]
        random.shuffle(other_doors)
        if choices[other_doors[0]] == 'donkey':
            print(f"We have opened Door #{other_doors[0] + 1}, which reveals a donkey! Good job dodging that one!")
            remaining_door = other_doors[1]
        else:
            print(f"We have opened Door #{other_doors[1] + 1}, which reveals a donkey! Good job dodging that one!")
            remaining_door = other_doors[0]
    switch = input(f'Would you like to switch to Door #{remaining_door + 1} (y/n)?: ')
    if switch == 'y':
        prize = choices[remaining_door]
        print(f'You have chosen to switch to Door #{remaining_door + 1}. The door opens and... You have won a {prize}!')
        print(f'Your original selection of Door #{choice} was a {choices[int(choice) - 1]}.')
    elif switch == 'n':
        print(f'You have chosen to stay with Door #{choice}. The door opens and... You have won a {choices[int(choice) - 1]}!')

    print('')


## Simulation
elif int(playstyle) == 2:
    # print("Welcome to the Monty Hall Problem Simulator!")
    # The purpose of this simulator is to demonstrate the outcome of the Monty Hall problem given a large number of playthroughs.

    choices = ['car','donkey','donkey']
    # print(choices)

    # # Remove the chosen item from the list
    # print(choices)

    # # Remove a donkey from the list
    # choices.remove('donkey')
    # print(choices)

    # switch = input('Would you like to switch to the remaining door (y/n)? ')
    # if switch == 'y':
    #     prize = random.choice(choices)
    #     print(f'You have chosen to switch to the other door. The door opens and... You have won a {prize}!')
    # elif switch == 'n':
    #     print(f'You have chosen to stay with your chosen door. The door opens and... You have won a {choice}!')


