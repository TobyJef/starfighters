# Used for random number generation
from random import randrange

# Functions to check placement of enemy starfighters 

def check_opponent(opponent,opponent_fighter):

    enemy_fighter = []
        for i in range(opponent):
            enemy_fighter.append(opponent_fighter + i)
            enemy_fighter = check_placement(enemy_fighter)
            print(opponent_fighter + i)

# Number of enemy starfighters compiled into an arrary
enemy_fleet = []
opponent_fighters = [1,1,1,1,1,1]
for opponent in opponent_fighters:
    # Places Starfighter opponents at random
    opponent_fighter = randrange(35)
    print(opponent,opponent_fighter)
    
    enemy_fighter = check_opponent(opponent,opponent_fighter)

enemy_fleet.append(opponent_fighters)
print(enemy_fleet)

# Opening message to the player
print("\n", "  ", "*"*3, "Welcome to Starfighters", "*"*3, "\n")

# Player name entry
#Username=input("Please enter your name: ")
print("\n")
#print("Welcome, Admiral", Username,"\n")
#print("Admiral", Username, ",your fleet is in position and awaiting your command.", "\n"*2)

# Gameboard key
print("Key:", "\n", "H = Hit", "\n", "M = Miss", "\n", "D = Destroyed", "\n")

# Function to record player move

def player_shot(shot_record):

    on_target = "no"
    while on_target == "no":
        try:
            player_move = input("Admiral, Enter your shot co-ordinates: ")
            player_move = int(player_move)
            if player_move < 0 or player_move > 35:
                print("Sorry Admiral, We cannot fire there")
            elif player_move in shot_record:
                print("We have already used those co-ordinates. Try again")
            else:
                on_target = "yes"
                break
        except:
            print("Please re-enter new co-ordinates")
        
        return player_move

# Opponent Gameboad

def opponent_board(hit,miss):
    #Creates opponent Gameboard
    """
    Creates a 6x6 grid displaying 0-5 along both x & y axis
        
    """
    print("\n", "    0  1  2  3  4  5  ", "\n")

    player_shot = 0

    for x in range(6):
        grid_rows = ""
        for y in range(6):
            grid_space = " _ "
            if player_shot in miss:
                grid_space = " M "
            elif player_shot in hit:
                grid_space = " H "

            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x," ",grid_rows)

enemy_ships, filled_space = place_enemies()

#def check_move

# Starship placement testing

#enemy_ship1 = [15]

# Hit and Miss testing area
hit = [12]
miss = [23]

shot_record = hit + miss

# Function calling area

# Function to record players shot
player_move = player_shot(shot_record)

# Function to check players move
#check_move(starship1,hit,miss)

# Function calling Opponent Gameboard
opponent_board(hit,miss)


