"""
Cian Herlihy - R00205604 - Task 2

I started off by getting the names of the players off the user. I could have done this is main() but it is cleaner
to get this in its own separate function and then return the list. This was not required, but I think it is an
improvement. I then ask how many players they would like to eject ranging from 1-6. This then gets input as a parameter
for the list_manipulate() function along with the list, so I can then start interacting with the list. I start by making
a copy, so I can see visually at the end that the players got removed and show the old list intact before any removal.
I then just do a simple for while loop to loop the amount of time the person wanted players ejected. I return a new list
with this function and handle the printing in main since it is not that much printing to need its own function.

In the print statements I used the keyword tuple() to print the list as a tuple but this can be done earlier in the
function if needed.
"""
import random
import time


def creating_list():
    all_players = []
    i = 0
    for i in range(12):
        player = input(f'Player {i + 1} Name: ')
        all_players.append(player)
        i += 1
    return all_players


def list_manipulate(all_players, amount):
    new_players = all_players.copy()
    i = 0
    while i < amount:
        player_name = random.choice(new_players)
        new_players.remove(player_name)
        print(f'Step Forth {player_name}')
        time.sleep(30)
        i += 1
    return new_players


def main():
    print("Task 2")
    print("")
    all_players = creating_list()
    result = int(input("How many players would you like to Remove? (1-6) >>> "))
    new_players = list_manipulate(all_players, result)
    print(f'{"="*60}')
    print(f'New List: {tuple(new_players)}')
    print(f'Old List: {all_players}')


if __name__ == "__main__":
    main()
