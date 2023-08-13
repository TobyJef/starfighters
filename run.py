# Used for random number generation
from random import randrange

# Functions to check placement of enemy starfighters 
"""
def check_placement(enemy_fighter,enemy_spawn):

    for i in range(len(enemy_fighter)):
        num = enemy_fighter[i]
        if num in enemy_spawn:
            enemy_fighter = [-1]
            break
        if num < 0 or num > 35:
            enemy_fighter = [-1]
            break
                   
    return enemy_fighter

def check_opponent(opponent,opponent_fighter,enemy_spawn):

    enemy_fighter = []
    for i in range(opponent):
            enemy_fighter.append(opponent_fighter + i)
            enemy_fighter = check_placement(enemy_fighter)
            return opponent_fighter + i
"""
"""
Number of enemy starfighters compiled into the arrary enemy_fleet

enemy_spawn to check for instances of already taken grid space

"""
"""
def create_enemy():
    enemy_spawn = []
    enemy_fleet = []
    opponent_fighters = [1,1,1,1,1,1]
    for opponent in opponent_fighters:
        enemy_fighter = [-1]
        while enemy_fighter[0] == -1:
            # Places Starfighter opponents at random
            opponent_fighter = randrange(35)
            print(opponent,opponent_fighter)
            
            enemy_fighter = check_opponent(opponent,opponent_fighter,enemy_spawn)

        enemy_fleet.append(opponent_fighters)
        enemy_spawn = enemy_spawn + enemy_fighter
        print(enemy_fleet)

    return enemy_fleet,enemy_spawn

opponent_fighter, enemy_spawn = create_enemy()
"""


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

def player_move(shot_record):

    on_target = "no"
    while on_target == "no":
        try:
            player_turn = input("Admiral, Enter your shot co-ordinates: ")
            player_turn = int(player_turn)
            if player_turn < 0 or player_turn > 35:
                print("Sorry Admiral, We cannot fire there")
            elif player_turn in shot_record:
                print("We have already used those co-ordinates. Try again")
            else:
                on_target = "yes"
                break
        except:
            print("Please re-enter new co-ordinates")
        
        return player_turn

# Opponent Gameboad
# Creates opponent Gameboard
def opponent_board(hit,miss,destroyed):
    
    """
    Creates a 6x6 grid displaying 0-5 along both x & y axis
        
    """
    print("\n", "    0  1  2  3  4  5  ", "\n")

    # Player shot counter
    player_shot = 0
    for x in range(6):
        grid_rows = ""
        for y in range(6):
            grid_space = " _ "
            if player_shot in miss:
                grid_space = " M "
            elif player_shot in hit:
                grid_space = " H "
            elif player_turn in destroyed:
                grid_space = " D "

            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x," ",grid_rows)

#enemy_ships,filled_space = place_enemies()

def check_move(player_turn,enemy_ship1,hit,miss,destroyed):

    if player_turn in enemy_ship1:
        enemy_ship1.remove(player_turn)
        if len(enemy_ship1) > 0:
            hit.append(player_turn)
        else:
            destroyed.append(player_turn)
    else:
        miss.append(player_turn)

    return enemy_ship1,hit,miss,destroyed

# Starship placement testing

enemy_ship1 = [15,16]

# Hit and Miss testing area
hit = []
miss = []
destroyed = []

# Function calling area
for i in range(10):

    # Function to check for duplicate player shots
    shot_record = hit + miss + destroyed

    # Function to record players shot
    player_turn = player_move(shot_record)

    # Function to check players move
    enemy_ship1,hit,miss,destroyed = check_move(player_turn,enemy_ship1,hit,miss,destroyed)

    # Function calling Opponent Gameboard
    opponent_board(hit,miss,destroyed)


