# Used for random number generation
import random

# Opening message to the player
print("\n", "  ", "*" * 3, "Welcome to Starfighters", "*" * 3, "\n")

# Player name entry
username = input("Please enter your name: \n")
print("\n")
print("Welcome, Admiral", username, "\n")
print("Admiral", username,",your fleet is in position and awaiting your command.","\n" * 2,)

# Gameboard key
print("Key:", "\n", "H = Hit", "\n", "M = Miss", "\n", "D = Destroyed", "\n", "* = Starfighter","\n")

"""
Lists to hold a 5x5 gameboard for the player's gameboard,
the players guesses and the computer's gameboard.
Adds an underscore to show empty grid spaces.
"""
grid_space = "_"
player_board = [[grid_space for _ in range(5)] for _ in range (5)]
computer_board = [[grid_space for _ in range(5)] for _ in range (5)]
player_guesses = [[grid_space for _ in range(5)] for _ in range (5)]

# Create gameboards
def print_board(board):
    """
    Creates a 5x5 gameboard, 
    Prints the grid columns as 1-5
    Also prints 11 -'s underneath to,
    create a top border to the gameboards.
    """
    print("   1 2 3 4 5")
    print("  -----------")
    for i, row in list(board):
        print(f"{i+1}| " + ' '.join(row))

# Checks players co-ordinates
def player_guess(player_input):
    """
    Checks the length of the players input to,
    make sure that a players guess does not exceed
    two co-ordinates
    """
    if len(player_input) != 2:
        return None
    row = ord(player_input[0]) - ord('A')
    col = int(player_input[1]) - 1
    if 0 <= row < board_size and 0 <= col < board_size:
        return row, col
    return None


# Place player's Starfighters at random
for _ in range(6):
    """
    Assigns the players 6 Starfighters at random
    grid co-ordinates and displays the Starfighter
    with an "*"
    """
    while True:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if player_board[row][col] == ' ':
            player_board[row][col] = '*'
            break


# Place computer's ships
for _ in range(6):
    """
    Assigns the computer 6 Starfighters at random
    grid co-ordinates and displays the Starfighter
    with an "*"
    """
    while True:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if computer_board[row][col] == ' ':
            computer_board[row][col] = '*'
            break



    # Player shot counter
    player_shot = 0
    for x in range(5):
        grid_rows = ""
        for y in range(5):
            grid_space = " _ "
            """
# Enemy Boat markers for testing
"""
            if player_shot in space_filled:
                grid_space = " O "

            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x, " ", grid_rows)

def computer_move(shot_record):
    on_target = "no"
    while on_target == "no":
        try:
            player_turn = randrange(24)
            if player_turn not in shot_record:
                on_target = "yes"
                shot_record.append(player_turn)
                break
        except:
            print("Please re-enter new co-ordinates")

    return player_turn, shot_record

def player_board(hit, miss, destroyed):
    print("\n", "     1  2  3  4  5 ", "\n")

    # Player shot counter
    player_shot = 0
    for x in range(5):
        grid_rows = ""
        for y in range(5):
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
        print(x, " ", grid_rows)

def check_move(player_turn, enemy_fleet, hit, miss, destroyed):
    computer_miss = 1
    for i in range(len(enemy_fleet)):
        if player_turn in enemy_fleet[i]:
            enemy_fleet[i].remove(player_turn)
            computer_miss = 0
            if len(enemy_fleet[i]) > 0:
                hit.append(player_turn)
            else:
                destroyed.append(player_turn)
    if computer_miss == 1:
        miss.append(player_turn)

    return enemy_fleet, hit, miss, destroyed

hit = []
miss = []
destroyed = []
shot_record = []

enemy_fleet, space_filled = place_enemies()
opponent_board(space_filled)

# Test ran at continuos shots
for i in range(60):
    player_turn, shot_record = computer_move(shot_record)
    enemy_fleet, hit, miss, destroyed = check_move(
        player_turn, enemy_fleet, hit, miss, destroyed
    )
    player_board(hit, miss, destroyed)

def player_move(shot_record):
    on_target = "no"
    while on_target == "no":
        try:
            player_turn = input("Admiral, Enter your shot co-ordinates: \n")
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
def player_board(hit, miss, destroyed):
    # Creates a 10x10 grid displaying 0-5 along both x & y axis

    print("\n", "    0  1  2  3  4  5   ", "\n")

    # Player shot counter
    player_shot = 0
    for x in range(5):
        grid_rows = ""
        for y in range(5):
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
        print(x, " ", grid_rows)

# enemy_ships,filled_space = place_enemies()

# Function to check if shot on enemy ship has hit,miss,destroyed

def check_move(player_turn, enemy_ship1, enemy_ship2, hit, miss, destroyed):
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

    return enemy_ship1, enemy_ship2, hit, miss, destroyed

# Starship placement testing

enemy_ship1 = [15, 16]
enemy_ship2 = [1, 7]
# enemy_ship3 = []
# enemy_ship4 = []
# enemy_ship5 = []


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
    enemy_ship1, enemy_ship2, hit, miss, destroyed = check_move(
        player_turn, enemy_ship1, enemy_ship2, hit, miss, destroyed
    )

    # Function calling Player Gameboard
    player_board(hit, miss, destroyed)

    if len(enemy_ship1) < 1 and len(enemy_ship2) < 1:
        print("Enemy ship destroyed")
        break

print("End of test")
