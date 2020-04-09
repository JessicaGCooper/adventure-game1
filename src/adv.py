from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
human = Player(room['outside'])
##BEGIN SETUP
human.name = input("Please enter your name: \n")
player = human.name.upper()
place = human.location.name.upper()
print("#############################################")
print(f"#### Welcome to the Adventure Game {player}! ####")
print("#############################################\n")
##DEFINE COMMANDS

game_running = True

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while game_running == True:
    print(f"{player} you are in the {place}.\n")
    print(f"{human.location.description}...\n")
    print("Your choices are: [n] North  [s] South  [w] West [e] East  [q] Quit\n")
    choice = input("Please make a selection to continue: ")
    if choice == "n":
        if human.location.n_to is not None:
            human.location = human.location.n_to
        else:
            print("######")
            print("BUMP! Please choose another direction!")
            print("######")
    elif choice == "s":
        if human.location.s_to is not None:
            human.location = human.location.s_to
        else:
            print("######")
            print("BUMP! Please choose another direction!")
            print("######")
    elif choice == "e":
        if human.location.e_to is not None:
            human.location = human.location.e_to
        else:
            print("######")
            print("BUMP! Please choose another direction!")
            print("######")
    elif choice == "w":
        if human.location.w_to is not None:
            human.location = human.location.w_to
        else:
            print("######")
            print("BUMP! Please choose another direction!")
            print("######")
    elif choice == "q":
        print("GOODBYE!!!")
        game_running = False
        break
    else:
        print("######") 
        print("Please choose a valid command.")
        print("######")


