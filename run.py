# Opening message to the player
print("\n", "  ", "*"*3, "Welcome to Starfighters", "*"*3, "\n")

# Player name entry
Username=input("Please enter your name: ")
print("\n")
print("Welcome, Admiral", Username,"\n")
print("Admiral", Username, ",your fleet is in position and awaiting your command.", "\n"*2)

# Gameboard key
print("Key:", "\n", "H = Hit", "\n", "M = Miss", "\n", "D = Destroyed", "\n")

# Opponent Gameboad

opponent_board = []

print("\n", "    0  1  2  3  4  5  ", "\n")
for x in range(6):
    grid_rows = ""
    for y in range(6):
        space = " _ "
    print(x," "," _ "*6)

#cpu_board(opponent_board)
