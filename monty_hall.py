## Written by Jason Gabunilas

# Import dependencies - matplotlib, the random module, and pandas

import matplotlib.pyplot as plt
import random
import pandas as pd

print("Welcome to the Monty Hall Problem!")
while True:
    playstyle = input('Would you like to (1) play manually, or (2) run a simulation? (choose 1 or 2) ')
    if playstyle == "1" or playstyle == "2":
        break
    else:
        print("You must choose either 1 or 2.")

# Create a function that runs a simulation of the Monty Hall problem. The only parameter that it takes is "switch", which determines whether the simulator switches doors after the unchosen "goat door" is opened. The function returns a tuple containing the initial choice and the ultimate prize.

def run_sim(switch):
    choices = ['car','goat','goat']
    initial_choice = random.choice(choices)
    # print(f"Initial choice: {initial_choice}")
    choices.remove(initial_choice)
    choices.remove('goat')
    remaining_choice = choices[0]
    # print(f"Remaining choice: {remaining_choice}")

    if switch == 'n':
        prize = initial_choice
    elif switch == 'y':
        prize = remaining_choice
    
    return(initial_choice, prize)

## Manual play
if int(playstyle) == 1: 
    print("Welcome to Let's Make a Deal!")

    # Create the choices (doors) and randomly shuffle them
    choices = ['goat','goat','car']
    random.shuffle(choices)
    # DEV ONLY: print the shuffled choices
    # 1print(choices)

    # Ask the player to choose a door
    while True:
        choice = input("Before you are three doors. Behind one of them is a new car. Behind the other two is a goat. You will win whatever is behind the door you choose! Please choose a door (1, 2, or 3): ")
        if choice == "1" or choice == "2" or choice == "3":
            break
        else:
            print("Your choice must be either 1, 2 or 3.")
        # DEV ONLY: indicate which prize is behind the door (car or goat). Remember that the actual prize is indexed at one position lower than the door number choice.
        # print(f'Chosen prize: {choices[int(choice) - 1]}')
    # Inform the player which door they have chosen.
    print(f'You have chosen Door #{choice}')
    # Open one of the non-selected doors. If a car is behind the selected door, then one of the two remaining doors with a goat will be opened. If a goat is behind the selected door, then the sole remaining door with a goat will be opened. 
    print(f"Before we open Door #{choice}, let's open one of the doors that you did not choose!")
    if int(choice) == 1:
        # If door 1 was selected, then we must open either door 2 or door 3. 
        # randomize which of the remaining doors 2 and 3 will be "checked" first. Remember that doors 2 and 3 are indexed at position 1 and 2 of the choices list, respectively. Therefore, we create a list of the remaining doors, shuffle that list, then check the first door (index 0) of the shuffled list. If that door has a goat, open it. If it does not, then open the door at index 1.
        other_doors = [1, 2]
        random.shuffle(other_doors)
        if choices[other_doors[0]] == 'goat':
            print(f"We have opened Door #{other_doors[0] + 1}, which reveals a goat! Good job dodging that one!")
            remaining_door = other_doors[1]
        else:
            print(f"We have opened Door #{other_doors[1] + 1}, which reveals a goat! Good job dodging that one!")
            remaining_door = other_doors[0]
    elif int(choice) == 2:
        # The same logic applies if door 2 was chosen. The only change is that the other_doors list will have doors 1 and 3 (indexed at 0 and 2 respectively).
        other_doors = [0, 2]
        random.shuffle(other_doors)
        if choices[other_doors[0]] == 'goat':
            print(f"We have opened Door #{other_doors[0] + 1}, which reveals a goat! Good job dodging that one!")
            remaining_door = other_doors[1]
        else:
            print(f"We have opened Door #{other_doors[1] + 1}, which reveals a goat! Good job dodging that one!")
            remaining_door = other_doors[0]
    elif int(choice) == 3:
        # The same logic applies for door 3. The only change is that the other_doors list will have doors 1 and 2 (indexed at 0 and 1 respectively).
        other_doors = [0, 1]
        random.shuffle(other_doors)
        if choices[other_doors[0]] == 'goat':
            print(f"We have opened Door #{other_doors[0] + 1}, which reveals a goat! Good job dodging that one!")
            remaining_door = other_doors[1]
        else:
            print(f"We have opened Door #{other_doors[1] + 1}, which reveals a goat! Good job dodging that one!")
            remaining_door = other_doors[0]
    while True:
        switch = input(f'Would you like to switch to Door #{remaining_door + 1} (y/n)?: ')
        if switch == 'y':
            prize = choices[remaining_door]
            print(f'You have chosen to switch to Door #{remaining_door + 1}. The door opens and... You have won a {prize}!')
            print(f'Your original selection of Door #{choice} was a {choices[int(choice) - 1]}.')
            break
        elif switch == 'n':
            print(f'You have chosen to stay with Door #{choice}. The door opens and... You have won a {choices[int(choice) - 1]}!')
            break
        else:
            print('Invalid entry. You must choose either "y" or "n".')

    print('')



## Simulation
elif int(playstyle) == 2:
    # print("Welcome to the Monty Hall Problem Simulator!")
    # The purpose of this simulator is to demonstrate the outcome of the Monty Hall problem given a large number of playthroughs.

    while True:
        num_sims = input("Please enter the number of simulations you would like to run: ")
        try: 
            num_sims = int(num_sims)
            break
        except:
            print("You must enter an integer number.")

    while True:
        switch = input("Please indicate whether the simulator will switch to the remaining door after one of the unchosen doors is opened (y/n) ")
        if switch == 'y' or switch == 'n':
            break
        else:
            print('You must enter "y" or "n".')

    # Initialize a list that will contain the results of each simulation
    results = []

    # Run the simulation num_sims times
    num_sims = int(num_sims)
    for n in range(num_sims):
        results.append(run_sim(switch))

    # print(results)

    # Create a list of initial choices, which is the first (0-indexed) object of each simulation result tuple in the results list
    initial_choices = []
    for result in results:
        initial_choices.append(result[0])
    # print(initial_choices)

    # Count the number of times that the simulator selected a car first, or a goat first
    initial_cars = 0
    initial_goats = 0
    for choice in initial_choices:
        if choice == 'goat':
            initial_goats += 1
        elif choice == "car":
            initial_cars += 1

    # Createa a list of final prices, which is the second (1-indexed) onject of each simulation result tuple in the results list
    final_prizes = []
    for result in results:
        final_prizes.append(result[1])
    # print(final_prizes)

    # Calculate the percentage of final prizes that are cars and goats
    total_goat_prizes = 0
    total_car_prizes = 0
    for prize in final_prizes:
        if prize == "goat":
            total_goat_prizes += 1
            percent_goats = 100 * total_goat_prizes / num_sims
        elif prize == "car":
            total_car_prizes += 1
            percent_cars = 100 * total_car_prizes / num_sims
    
    print(f"Total car prizes: {total_car_prizes} ({percent_cars}%)")
    print(f"Total goat prizes: {total_goat_prizes} ({percent_goats})%")

    # Create a Pandas dataframe containing the total number of car and goat prizes, and the percentages of each type of prize
    df = pd.DataFrame(data = {'Total Prizes': [total_car_prizes, total_goat_prizes], 'Percent':[str(percent_cars) + "%", str(percent_goats) + "%"]}, index = ["Cars", "Goats"])
    # print(df)

    ax = df.plot(kind = 'bar', title = f"Prize Results for {num_sims} Simulations, switch = {switch}")
    plt.show()

    # print(choices)

    # # Remove the chosen item from the list
    # print(choices)

    # # Remove a goat from the list
    # choices.remove('goat')
    # print(choices)

    # switch = input('Would you like to switch to the remaining door (y/n)? ')
    # if switch == 'y':
    #     prize = random.choice(choices)
    #     print(f'You have chosen to switch to the other door. The door opens and... You have won a {prize}!')
    # elif switch == 'n':
    #     print(f'You have chosen to stay with your chosen door. The door opens and... You have won a {choice}!')


