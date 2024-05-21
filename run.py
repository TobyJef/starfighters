# Used for random number generation
import random

"""
Global Variable
"""
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
        self.num_of_fighters = num_of_fighters
        self.player_type = player_type
        self.player_name = player_name
        self.guesses = []
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
    return int(random.randint(0, boardsize-1))


def add_fighters(gameboard):
    """
    Function to generate random Starfighter placement,
    for both players and computers gameboard.
    """
    num_of_fighters = gameboard.num_of_fighters
    fighter_list = []
    empty_spaces = []

    while len(empty_spaces) < num_of_fighters:
        x = random_number(gameboard.size)
        y = random_number(gameboard.size)
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
            elif num < 0:
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
            if gameboard.player_type == "Computer":
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
            if gameboard.player_type == "Computer":
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
            scores["Computer"] += 1
            return scores


def shots_fired_counter(gameboard):
    """
    Tracks the total number of the players guesses until
    the win condition is achieved, and displays a custom
    message based on number of shots taken by the player
    """
    turns = gameboard.turns
    print("\n")
    print("-" * 40)
    print("Congratulations Admiral. All enemy Starfighters were destroyed.")
    print(f"Battle Analysis shows the enemy was defeated from {turns} shots")
    print("\n")
    if int(turns) < 5:
        print("A Commendation awaits you Admiral, Congratulations")
    elif int(turns) < 10:
        print("An impressive display Admiral, Well Done")
    elif int(turns) < 15:
        print("A solid victory!")
    elif int(turns) < 20:
        print("A hard fought victory")
    else:
        print("That was a close call Admiral, but a win is still a win")
    print("-" * 40)


def board_display(players_board, computers_board):
    """
    Function containing both the Players and Computers Gameboards
    """
    print()
    print(f"{players_board.player_name}'s Tactical Display")
    print("-" * 40)
    players_board.display_board()
    print()
    print(f"{computers_board.player_name}'s Tactical Display")
    print("-" * 40)
    computers_board.display_board()
    print()


def play_game(players_board, computers_board):
    """
    Used for displaying the in game text and victory/loss messages
    """
    while scores["Computer"] or scores[players_board.player_name] <= 5:
        print(f"{players_board.player_name}. It is your turn to attack!")
        print("Prepare to enter the co-ordinates you would like to strike.")
        print("-" * 65)
        players_turn, x, y = validate_shots(computers_board)

        print("-" * 65)
        print(f"Shot fired!, target '{players_turn}' at co-ordinate{(x, y)}")
        calculate_score(players_turn, players_board)
        if (scores[players_board.player_name] == 5):
            print()
            break

        print("-" * 65)
        print(f"It's now the {computers_board.player_name}'s turn to attack.")
        computers_turn, x, y = validate_shots(players_board)
        print("-" * 65)
        calculate_score(computers_turn, computers_board)
        print(f"Shot fired!, target '{computers_turn}' at co-ordinate{(x, y)}")
        if (scores["Computer"] == 5):
            print()
            break

        board_display(players_board, computers_board)
        print("The scores at the end of the round are:")
        print(scores)
        print()

    board_display(players_board, computers_board)
    if scores[players_board.player_name] == 5:
        print(f"Congratulations {players_board.player_name}! You won!")
        shots_fired_counter(computers_board)
    else:
        print("Unlucky, The computer beat you this time!")
    print()
    print("The scores at the end of the game are:")
    print(scores)
    print()

    text_a = ("Would you like to play again? ")
    text_b = ("Press any key to continue or 'n' to quit:")
    play_again = str(input(text_a + text_b + " \n"))
    if play_again != "n":
        scores.pop(players_board.player_name)
        start_game()


def start_game():
    """
    Runs the complete Starfighters Game
    """

    boardsize = 5
    fighters = 5
    players_name = check_username()
    scores["Computer"] = 0
    scores[players_name] = 0
    turns = 0
    players_board = GameBoard(boardsize, fighters, "user", players_name, turns)
    computer_board = GameBoard(boardsize, fighters, "Computer",
                               "Computer", turns)

    # Opening message to the player
    print("*" * 40)
    print("Hello Admiral and welcome to the Starfighters Tactical Display")
    print("Your fleet is in position and awaiting your command.")
    print(f"The tactical displays are 5x5")
    print("The number of enemy Starfighters is 5")
    print("The top left grid co-ordinate is (0, 0)")
    print("*" * 40)

    # Gameboard key
    print("Key:", "\n", "* = Stars", "\n", "# = Destroyed Starfighter",
          "\n", "o = Miss", "\n", "V = Starfighter", "\n")

    add_fighters(players_board)
    add_fighters(computer_board)

    board_display(players_board, computer_board)
    play_game(players_board, computer_board)


print()
print("-" * 65)
print("\n", "  ", "*" * 3, "Welcome to Starfighters", "*" * 3, "\n")
print("Shoot first and ask questions later in this tactical grid game")
print("Destroy the hidden enemy Starfighters before your own Starfighter")
print("fleet is destroyed, leaving you defenceless!")
print("-" * 65)
print()
start_game()
