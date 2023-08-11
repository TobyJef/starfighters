# Opening message to the player
print("\n", "  ", "*"*3, "Welcome to Starfighters", "*"*3, "\n")

# Player name entry
#Username=input("Please enter your name: ")
print("\n")
#print("Welcome, Admiral", Username,"\n")
#print("Admiral", Username, ",your fleet is in position and awaiting your command.", "\n"*2)

# Gameboard key
print("Key:", "\n", "H = Hit", "\n", "M = Miss", "\n", "D = Destroyed", "\n")

# Opponent Gameboad

#def opponent_board(hit,miss):
    # Creates opponent Gameboard
"""
Creates a 6x6 grid displaying 0-5 along both x & y axis
     
"""
print("\n", "    0  1  2  3  4  5  ", "\n")

hit = [12]
miss = [23]

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

#opponent_board(hit,miss)
