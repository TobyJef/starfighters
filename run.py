# Used for random number generation
from random import randrange

# Functions to check placement of enemy starfighters

"""
Function to place enemy starfighters within the game board

"""
def check_placement(fighter,space_filled):

    for i in range(len(fighter)):
        num = fighter[i]
        if num in space_filled:
            fighter = [-1]
            break
        elif num < 0 or num > 99:
            fighter = [-1]
            break
        elif num % 10 == 9 and i < len(fighter) -1:
           if fighter[i+1] % 10 == 0:
                fighter = [-1]
                break

    return fighter

# Function to determine random placement and heading of enemy ships within grid size

def check_enemy(enemy, placement, heading, space_filled):

    heading = 4
    fighter = []
    # head of fighter heading North
    if heading == 1:
        for i in range(enemy):
            fighter.append(placement - i*10)
            fighter = check_placement(fighter,space_filled)
            print(placement - i*10)
    # head of fighter heading East
    elif heading == 2:
        for i in range(enemy):
            fighter.append(placement + i)
            fighter = check_placement(fighter,space_filled)
            print(placement + i)
    #head of fighter heading South
    elif heading == 3:
        for i in range(enemy):
            fighter.append(placement + i*10)
            fighter = check_placement(fighter,space_filled)
            print(placement + i*10)
    #head of fighter heading West
    elif heading == 4  :
        for i in range(enemy):
            fighter.append(placement - i)
            fighter = check_placement(fighter,space_filled)
            print(placement - i)
    return fighter

"""
Function to place enemy starfighters at random.
While not sharing the same grid space,
or spilling out of the game board

"""

def place_enemies ():

    space_filled = []
    enemy_fleet = []
    enemy_fighters = [5, 3, 3, 2, 1, 1]

    for enemy in enemy_fighters:
        fighter = [-1]
        while fighter[0] == -1:

        # Places enemy Starfighter at random

            enemy_start = randrange(99)
            enemy_heading = randrange(1,4)

            print(enemy, enemy_start, enemy_heading)
            fighter = check_enemy(enemy, enemy_start, enemy_heading, space_filled)
        
        enemy_fleet.append(fighter)
        space_filled = space_filled + fighter
        print (enemy_fleet)

    return enemy_fleet, space_filled

# Opponent Gameboad
# Creates opponent Gameboard
def opponent_board(space_filled):
    """

# Creates a 10x10 grid displaying 0-9 along both x & y axis


"""
    print("\n", "    0  1  2  3  4  5  6  7  8  9 ", "\n")

    # Player shot counter
    player_shot = 0
    for x in range(10):
        grid_rows = ""
        for y in range(10):
            grid_space = " _ "
            """
# Hit, Miss, Destroyed markers
"""
            if player_shot in space_filled:
                grid_space = " O "


            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x," ",grid_rows)

def computer_move(shot_record):

    on_target = "no"
    while on_target == "no":
        try:
            player_turn = randrange(99)
            if player_turn not in shot_record:
                on_target = "yes"
                shot_record.append (player_turn)
                break
        except:
            print("Please re-enter new co-ordinates")
        
    return player_turn, shot_record

def player_board(hit,miss,destroyed):
    print("\n", "    0  1  2  3  4  5  6  7  8  9 ", "\n")

    # Player shot counter
    player_shot = 0
    for x in range(10):
        grid_rows = ""
        for y in range(10):
            grid_space = " _ "
            """
# Hit, Miss, Destroyed markers
"""
            if player_shot in miss:
                grid_space = " M "
            elif player_shot in hit:
                grid_space = " H "
            elif player_shot in destroyed:
                grid_space = " D "

            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x," ",grid_rows)

def check_move(player_turn,enemy_fleet,hit,miss,destroyed):

    for
    if player_turn in enemy_ship1:
        enemy_ship1.remove(player_turn)
        if len(enemy_ship1) > 0:
            hit.append(player_turn)
        else:
            destroyed.append(player_turn)
    elif player_turn in enemy_ship2:
        enemy_ship2.remove(player_turn)
        if len(enemy_ship2) > 0:
            hit.append(player_turn)
        else:
            destroyed.append(player_turn)
    else:
        miss.append(player_turn)

    return enemy_fleet,hit,miss,destroyed

hit = []
miss = []
destroyed = []
shot_record = []

enemy_fleet, space_filled = place_enemies()
opponent_board(space_filled)
player_turn, shot_record = computer_move(shot_record)
enemy_fleet,hit,miss,destroyed = check_move(player_turn,enemy_fleet,hit,miss,destroyed)
player_board(hit,miss,destroyed)

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
            if player_turn < 0 or player_turn > 99:
                print("Sorry Admiral, We cannot fire there")
            elif player_turn in shot_record:
                print("We have already used those co-ordinates. Try again")
            else:
                on_target = "yes"
                break
        except:
            print("Please re-enter new co-ordinates")
        
    return player_turn

# Player Gameboard
# Creates player Gameboard
def player_board(hit,miss,destroyed):
    """

# Creates a 10x10 grid displaying 0-9 along both x & y axis


"""
    print("\n", "    0  1  2  3  4  5  6  7  8  9 ", "\n")

    # Player shot counter
    player_shot = 0
    for x in range(10):
        grid_rows = ""
        for y in range(10):
            grid_space = " _ "
            """
# Hit, Miss, Destroyed markers
"""
            if player_shot in miss:
                grid_space = " M "
            elif player_shot in hit:
                grid_space = " H "
            elif player_shot in destroyed:
                grid_space = " D "

            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x," ",grid_rows)

#enemy_ships,filled_space = place_enemies()

# Function to check if shot on enemy ship has hit,miss,destroyed

def check_move(player_turn,enemy_ship1,enemy_ship2,hit,miss,destroyed):

    if player_turn in enemy_ship1:
        enemy_ship1.remove(player_turn)
        if len(enemy_ship1) > 0:
            hit.append(player_turn)
        else:
            destroyed.append(player_turn)
    elif player_turn in enemy_ship2:
        enemy_ship2.remove(player_turn)
        if len(enemy_ship2) > 0:
            hit.append(player_turn)
        else:
            destroyed.append(player_turn)
    else:
        miss.append(player_turn)

    return enemy_ship1,enemy_ship2,hit,miss,destroyed

# Starship placement testing

enemy_ship1 = [15,16]
enemy_ship2 = [1,7]

#enemy_ship3 = []
#enemy_ship4 = []
#enemy_ship5 = []
#enemy_ship6 = []

# Hit and Miss testing area
hit = []
miss = []
destroyed = []

# Function calling area

# Player move limit. Test at 99.
for i in range(99):

    # Function to check for duplicate player shots
    shot_record = hit + miss + destroyed

    # Function to record players shot
    player_turn = player_move(shot_record)

    # Function to check players move
    enemy_ship1,enemy_ship2,hit,miss,destroyed = check_move(player_turn,enemy_ship1,enemy_ship2,hit,miss,destroyed)

    # Function calling Player Gameboard
    player_board(hit,miss,destroyed)


    if len(enemy_ship1) < 1 and len(enemy_ship2) < 1:
        print("Enemy ship destroyed")
        break

print ("End of test")

"""
