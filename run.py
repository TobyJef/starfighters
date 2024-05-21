# Used for random number generation
import random

#Global Variable
scores = {"Computer": 0}

class Duplicate_Shot(Exception):
    """
    Error message for instances of duplicate shots,
    called by the player
    """


class Out_of_Bounds(Exception):
    """
    Error message for instances of guessed shots
    that is outside of the gameboard
    """


class Negative_Input(Exception):
    """
    Error message for instances of guessed shots
    with a negative value
    """


class No_Username(Exception):
    """
    Error message for when no name given at
    user name input
    """


class GameBoard():
    """
    "*" = The Stars
    "o" = Missed Shot
    "#" = Destroyed Starfighter
    "V" = Players Active Starfighters
    """

    def __init__(self, size, num_of_fighters, player_type, player_name, turns):
        self.size = size
        self.board_grid = [["*" for x in range(size)] for y in range(size)]
        self.num_of_fighters = num_if_fighters
        self.player_type = player_type
        self.player_name = player_name
        self.guess = []
        self.fighters = []
        self.turns = turns

    
    def display_board(self):
        """
        GameBoard column decoration
        """
        for row in self.board_grid:
            print(" | ".join(row))

    
    def guess(self, x, y):
        """
        Missed Shots
        """
        self.guesses.append((x, y))
        self.board_grid[x][y] = "o"
        self.turns += 1

        if (x, y) in self.fighters:
            """
            Destroyed Starfighters
            """
            self.board_grid[x][y] = "#"
            return "Destroyed"
        else:
            return "Miss"


    def display_fighters(self):
        """
        Players Starfighters
        """
        for co_ord in self.fighters:
            x, y = co_ord
            if self.player_type == "user":
                self.board_grid[x][y] = "V"


def random_number(boardsize):
    """
    Helper function that creates a 
    random interger based on the boardsize
    """
return int(random.randint(0, boardsize -1))


def add_fighters(gameboard):
    """
    Function to generate random Starfighter placement,
    for both players and computers gameboard.
    """
    num_of_fighters = gameboard.num_of_fighters
    fighter_list = []
    empty_spaces = []

    while len(empty_space) < num_of_fighters:
        x = rand_num(gameboard.size)
        y = rand_num(gameboard.size)
        fighter = (x, y)
        fighter_list.append(fighter)
        empty_spaces = set(fighter_list)
        gameboard.fighters = list(empty_spaces)
        gameboard.display_fighters()


def input_guess(boardsize, row_or_column):
    """
    Players Guess Input Prompt
    """
    text = ("Enter a number between 0 and ")
    num = int(input(text + f'{boardsize - 1} for the {row_or_column}: \n'))
    return num


def make_guess(gameboard, x, y):
    """
    Stores Player Guess
    """
    return gameboard.guess(x, y)


def validate_input(gameboard, row_or_column):
    """
    Checks the Players guessed shot to ensure they
    fall within the Gameboards dimensions or contain
    valid input
    """
    while True:
        try:
            num = input_guess(gameboard.size, row_or_column)
            if num > gameboard.size - 1:
                raise Out_of_Bounds
            elif num  < 0:
                raise Negative_Input
            return num
        except ValueError as error:
            e = str(error).split()
            print(f'{e[-1]} is not a valid input')
        except Out_of_Bounds:
            print("Sorry Admiral, We cannot fire there")
        except Negative_Input:
            print("Please enter a number between 0 and 4")


def check_username():
    """
    Check to see if a proper username was provided,
    at least one character is required.
    """
    while True:
        try:
            name = input("Please enter your name: ")
            if len(name) == 0:
                raise No_Username
            return name
        except No_Username:
            print("Please enter a name")


def validate_shots(gameboard):
    """

    """
    while True:
        try:
            if gameboard.player_type == "computer":
                x = validate_input(gameboard, "row")
                y = validate_input(gameboard, "column")
                if (x, y) in gameboard.guesses:
                    raise Duplicate_Shot
            else:
                x = int(random_number(gameboard.size))
                y = int(random_number(gameboard.size))
                if (x, y) in gameboard.guesses:
                    raise Duplicate_Shot
            return make_guess(gameboard, x, y), x, y
        except Duplicate_Shot:
            if gameboard.player_type == "computer":
                shot_error = ("You have already guessed those co-ordinates")
                print(shot_error)


def calculate_score(turn, gameboard):
    """
    Tracks the games and updates the scoreboard
    """
    if turn == "Destroyed":
        if gameboard.player_type == "user":
            scores[gameboard.player_name] += 1
            return scores
        else:
            scores["computer"] += 1
            return scores

def shots_fired_counter(gameboard):
    """
    Tracks the total number of the players guesses until
    the win condition is achieved
    """
    turns = gameboard.turns
    print("\n")
    print("-" * 40)
    print("Congratulations Admiral. All enemy Starfighters were destroyed.")
    print(f"Battle Analysis shows the enemy was defeated from {turns} shots")
    print("\n")
    if int(turns) < 5:
        print("A Commendation awaits you Admiral, Well Done")
    elif int(turns) < 10:
        print("")




# Opening message to the player
print("\n", "  ", "*" * 3, "Welcome to Starfighters", "*" * 3, "\n")

# Player name entry
username = input("Please enter your name: \n")
print("\n")
print("Welcome, Admiral", username, "\n")
print("Admiral", username, ",your fleet is in position and awaiting your command.", "\n" * 2,)

# Gameboard key
print("Key:", "\n", "H = Hit", "\n", "o = Miss", "\n", "* = Starfighter", "\n")



def check_placement(fighter, space_filled):
    """
    Check to ensure enemy Starfighters do not occupy the same grid space
    """
    for i in range(len(fighter)):
        num = fighter[i]
        if num in space_filled:
            fighter = -1
            break
        elif num < 0 or num > 24:
            fighter = -1
            break
        elif num % 5 == 4 and i < len(fighter) - 1:
            if fighter[i + 1] % 5 == 0:
                fighter = [-1]
                break
        return (fighter)


def check_starfighter(fighter, enemy_start, enemy_heading, space_filled):
    """
    Sets Starfighter direction
    """
    fighter = []
    if enemy_heading == 1:
        # Fighter displayed vertically
        for i in range(enemy):
            fighter.append(start + i+5)
            fighter = check_placement(fighter, space_filled)

    elif enemy_heading == 2:
        # Fighter displayed horizontally
        for i in range(enemy):
            fighter.append(start + i)
            fighter = check_placement(fighter, space_filled)

    return fighter, space_filled


def check_placement_player(fighter, space_filled):
    """
    Check to ensure player Starfighters do not occupy the same grid space
    """
    for i in range(len(fighter)):
        num = fighter[i]
        if num in space_filled:
            fighter = -1
            break
        elif num < 0 or num > 24:
            fighter = -1
            break
        elif num % 5 == 4 and i < len(fighter) - 1:
            if fighter[i + 1] % 5 == 0:
                fighter = [-1]
                break
        return (fighter)


def get_fighters(starfighters, space_filled):

    return starfighter


def create_fleet(space_filled):

    """
    Creates and places the players fleet at random
    """
    player_fleet = [pilot1, pilot2, pilot3, pilot4, pilot5]
    starfighters = [1, 1, 1, 1, 1]

    for friendly in starfighters:
        pilot = get_fighters(starfighters, space_filled)
        player_fleet.append(starfighter)

    return starfighter

player_fleet = create_fleet


def create_fighters(space_filled):
    """
    Creates and places the enemy fleet at random
    """
    enemy_fleet = [enemy1, enemy2, enemy3, enemy4, enemy5]
    enemy_fighters = [1, 1, 1, 1, 1]
    for enemy in enemy_fighters:
        fighter = [-1]
        while fighter[0] == -1:
            enemy_start = randrange(24)
            enemy_heading = randrange(1, 2)
            fighter = check_starfighter(enemy, enemy_start, enemy_heading)

        enemy_fleet.append(fighter)
        space_filled = space_filled + fighter

    return enemy_fleet, space_filled



# Player shot counter
player_shot = 0
for x in range(5):
    grid_rows = ""
    for y in range(5):
        grid_space = " _ "

    if player_shot in space_filled:
        grid_space = " O "

    grid_rows = grid_rows + grid_space
    player_shot = player_shot + 1

print(x, " ", grid_rows, space_filled)




# Player's Gameboard and Shot Checks
def player_board(hit, miss):
    print(title)
    """
    Function to display the player's shots against the computer
    """
    for x in range(5):
        grid_rows = ""
        for y in range(5):
            grid_space = " ~ "
            # Hit, Miss markers
            if player_shot in miss:
                grid_space = " M "
            elif player_shot in hit:
                grid_space = " H "

            grid_rows = grid_rows + grid_space
            player_shot = player_shot + 1
        print(x, " ", grid_rows)


def check_move(player_turn, enemy_fleet, hit, miss):
    """
    Function to check
    """
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

    return enemy_fleet, hit, miss


def player_move(shot_record):
    """
    Asks player to input their shot co-ordinates
    and checks to the shot lands within the grid
    """
    on_target = "no"
    while on_target == "no":
        try:
            player_turn = input("Admiral, Please enter your shot: ")
            player_turn = input(player_turn)
            if player_turn < 0 or player_turn > 24:
                print("Sorry Admiral, We cannot fire there")
            elif player_turn in shot_record:
                print("We have already used those co-ordinates. Try again")            
            else:
                ok = "yes"
                break
            print("Incorrect shot co-ordinates. Please try again")


# Computers Gameboard and Shot Checks


def computer_board(space_filled):
    """
    # Creates a 5x5 grid to place the computers Starfighters
    """
    print(y-axis)

    for x in range(5):
        grid_rows = ""
    for y in range(5):
        grid_space = " _ "
        # Hit, Miss markers
        if player_shot in space_filled:
            grid_space = " o "
            grid_row = grid_row + grid_space
            player_shot = player_shot + 1

        return (x, " ", grid_row)


def computer_move(shot_record):
    """
    Checks if computers shot is "on_target"
    """
    on_target = "no"
    while on_target == "no":
        try:
            player_turn = randrange(24)
            if player_turn not in shot_record:
                on_target = "yes"
                shot_record.append(player_turn)
                break
            print("Please re-enter new co-ordinates")

    return player_turn, shot_record


def check_move(player_turn, enemy_fleet, hit, miss, missed):
    """
    Function to check if a starfighter has been hit or missed
    """
    missed = 1
    for i in range(len(enemy_fleet)):
        if player_turn in enemy_fleet[i]:
            enemy_fleet[i].remove(player_turn)
            missed = 0
            if len(enemy_fleet[i]) > 0:
                hit.append(player_turn)
            else:
                destroyed.append(player_turn)
    if missed == 1:
        miss.append(player_turn)

    return enemy_fleet, hit, miss, missed


# Test ran with consecutive shots
for i in range(60):
    player_turn, shot_record = computer_move(shot_record)
    enemy_fleet, hit, miss = check_move(
        player_turn, enemy_fleet, hit, miss
    )
    player_board(hit, miss)


def player_move(shot_record):
    """
    Function that calls for shot input from the player
    """
    on_target = "no"
    while on_target == "no":
        try:
            player_turn = input("Admiral, Enter your shot co-ordinates: \n")
            player_turn = int(player_turn)
            if player_turn < 0 or player_turn > 24:
                print("Sorry Admiral, We cannot fire there")
            elif player_turn in shot_record:
                print("We have already used those co-ordinates. Try again")
            else:
                on_target = "yes"
                break

            print("Please re-enter new co-ordinates")

    return player_turn


def check_move(player_turn, enemy_fleet, hit, miss):
    """
    Function to check if the shot on enemy Starfighter has hit or miss
    """
    if player_turn in enemy_ship1:
        enemy_ship1.remove(player_turn)
        if len(enemy_ship1) > 0:
            hit.append(player_turn)
    elif player_turn in enemy_ship2:
        enemy_ship2.remove(player_turn)
        if len(enemy_ship2) > 0:
            hit.append(player_turn)
    else:
        miss.append(player_turn)

    return enemy_fleet, hit, miss


# Empty Array group
hit = []
miss = []
shot_record = []

# Enemy fleet of ships
enemy_fleet = [enemy1, enemy2, enemy3, enemy4, enemy5]
enemy1 = []
enemy2 = []
enemy3 = []
enemy4 = []
enemy5 = []

# Player's fleet of ships
player_fleet = [pilot1, pilot2, pilot3, pilot4, pilot5]
pilot1 = []
pilot2 = []
pilot3 = []
pilot4 = []
pilot5 = []

# Function calling area

# Creates enemy fleet
enemy_fleet, space_filled = create_fighters(taken1)

#
player_board(space_filled, hit, miss)

#
guess_board(space_filled)

#
player_turn, shot_record = computer_move(shot_record)


# Function calling area

# Player move limit. Test at 99.
for i in range(99):

    # Function to check for duplicate player shots
    shot_record1 = hit1 + miss1

    # Function to record players shot
    player_turn = player_move(shot_record)
    player_turn, shot_record = computer_move(shot_record)

    # Function to check players move
    enemy_fleet, hit, miss = check_move(
        player_turn, enemy_fleet, hit, miss)

# Function calling Computer Gameboard
computer_board(space_filled)

# Function calling Player Gameboard
player_board(hit, miss, missed)


# Checks to see if all Starships have been destroyed

if len(enemy_fleet) < 1:
    print("Congratulations Admiral", username, "The enemy fleet has been destroyed")
elif len(player_fleet) < 1:
    print("The enemy has destroyed your fleet")

    print("End of Game, Thank You for playing")