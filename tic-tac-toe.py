import random

''' This program simulates the tic-tac-toe game in a very simple way..

    >>>Issues/Bug Report<<<
    4 Bugs found till now.
    1>> * 0 *
        $ * #
        player wins at above '*' pattern (bug in Left Diagonal @line 43)       
    2>> This program doesn't know how deal with draw situations  
    3>> This program is inefficient. Can't predict a sure draw and can't break out prematurely in that case
    4>> This program takes irrelevant inputs 
    
    Fixes:
    Bug #1 is fixed
    Bug #2 taken care
'''


# Board Display
def display_board(current_board):
    """Displays the current board on the screen close to classical tic-tac-toe table format"""

    for r in range(len(current_board)):
        for c in range(len(current_board[r])):
            if c in (0, 1):
                print(" ", current_board[r][c], ' | ', end='')
            else:
                print(" ", current_board[r][c])
        if r in (0, 1):
            print("- " * 10)


# Player Action Executor
def chaal(current_board, player_character, player_character_position):
    """
    Puts the players character on the current board where he/she wants to.
    Here chaal stands for Bangla 'চাল'.
    :param current_board: the current board
    :param player_character: players character assigned randomly.
    :param player_character_position: the cell number on the current board he/she wants to put his/her character
    :return: the changed board due to the character insertion
    """
    for row in range(len(current_board)):
        for col in range(len(current_board[row])):
            if current_board[row][col] == player_character_position:
                current_board[row][col] = player_character
    return current_board


# Game Judge
def game_over(current_board):
    """
    Brain of the game.
    Goes through the classical rules of tic-tac-toe game.
    Inspects the current board and checks if the horizontal, vertical or diagonal elements
    are same or not. Also decides explicitly whether the game is draw or not.
    :param current_board: the current board
    :return: 'True' if game is over or,
             'False' if game is not over or,
             'None' if game is a draw
    """
    # horizontal check--> (stable)
    for row in current_board:
        if len(['col' for col in row if col == row[0]]) == 3:
            return True

    # vertical check--> (is stable for now)
    for c in range(len(current_board[0])):
        if (len(['r' for r in range(len(current_board)) if current_board[r][c] == current_board[0][c]])) == 3:
            return True

    # working with diagonals
    # left_diagonal = [col for row in board for col in row if row.index(col) == board.index(row)]  # -->Not stable
    left_diagonal = list()
    for r in range(len(current_board)):
        for c in range(len(current_board[r])):
            if r == c and current_board[r][c] == current_board[0][0]:
                left_diagonal.append(current_board[r][c])

    right_diagonal = list()
    index_of_each_row = len(current_board) - 1
    for row in current_board:
        for member in row:
            if member == row[index_of_each_row]:
                right_diagonal.append(member)
                break
        index_of_each_row -= 1

    # diagonal check--> (is stable for now)
    if len(["x" for x in left_diagonal if x == left_diagonal[0]]) == 3 or len(
            ["x" for x in right_diagonal if x == right_diagonal[0]]) == 3:
        return True

    # draw decider
    draw = list()
    for row in current_board:
        for member in row:
            if not member.isnumeric():
                draw.append(member)
    # draw check
    if len(draw) == 9:
        return None
    return False


# Game Anchor
def GameAnchor(Name_1, Name_2, Score_1, Score_2):
    """
    Displays a well-formatted result on screen based on points of each player.
    :param Name_1: Name of Player 1
    :param Name_2: Name of Player 2
    :param Score_1: Score of Player 1
    :param Score_2: Score of Player 2
    """
    if Score_1 > Score_2:
        print(f"\n\t{Name_1} WINS THE GAME BY {Score_1 - Score_2} POINTS!!!\n\t***P E A C E***")
    elif Score_2 > Score_1:
        print(f"\n\t{Name_2} WINS THE GAME BY {Score_2 - Score_1} POINTS!!!\n\t***P E A C E***")
    else:
        print("\n\tNEITHER WINS, NEITHER LOOSES. FAIR DRAW!!!\n\t***P E A C E***")


# basic needs
characters = ['()', '><']
plr1_score = 0
plr2_score = 0
game_count = 0

# Greeting message and player name registration........................................
print("Hi! This is a very simple version of tic-tac-toe.\n")
Player_1 = input("Enter your name as player 1: ").upper()
Player_2 = input("Enter your name as player 2: ").upper()

# Entering The Game flow................................................................

# <Master Loop>
while True:
    # Print current scores
    print(f"Current Score:\n{Player_1}: {plr1_score}\n{Player_2}: {plr2_score}")
    # Ask to start or exit
    usr = input("\nFight?\n\t"
                "Type 'Y' to start or 'N' to show result and exit>> ")

    # if reply is no
    if usr not in ('y', 'Y'):
        # Print results
        print("\nGame Ended\n")
        print(f"{game_count} Game(s) played.\n\t"
              f"{Player_1} scored {plr1_score} points\n\t"
              f"{Player_2} scored {plr2_score} points")

        GameAnchor(Player_1, Player_2, plr1_score, plr2_score)
        # Now exit the game
        exits = input('Press any key to exit....')
        del exits
        break

    # Otherwise start a new game...

    # Game Pre-requisites:
    print("\n**New Game:\n")
    game_count += 1  # Game number counter updated

    # Set New Board and characters for Player 1 & 2 Then display results
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    # Randomly selecting Game Character for Player 1
    plr1_chr = random.choice(characters)

    # Selecting the remaining Game Character for Player 2
    try:
        plr2_chr = characters[characters.index(plr1_chr) + 1]
    except:
        plr2_chr = characters[0]

    # Pre-requisites of game are complete so print them out
    print(f"\n{Player_1}'s character ====> {plr1_chr}\n"
          f"{Player_2}'s character ====> {plr2_chr}\n")
    display_board(board)

    # Let the Game Begin...
    # <Child loop of the Master loop>
    while True:
        # Player 1's Section:
        p1_pos = input(f"\n{Player_1} Position: ")  # Take cell number from Player 1
        p1Chaal = chaal(board, plr1_chr,
                        p1_pos)  # Insert PLayer 1's Character to his/her cell number IE: Modify the board
        print(f"{Player_1} played:\n")  # Print the modified board
        display_board(p1Chaal)
        if game_over(p1Chaal):  # Check if Player 1 wins
            print(f"\n\t***{Player_1} WINS***\n\n")
            plr1_score += 1
            break
        elif game_over(p1Chaal) is None:  # if not then check if the game is draw
            print("\n\t*** Game is draw. Points --> 50% split ***")
            plr1_score += 0.5
            plr2_score += 0.5
            break

        # if neither win nor draw proceed to player 2

        # Player 2's Section:
        # All steps are similar to Player 1
        p2_pos = input(f"\n{Player_2} Position: ")
        p2Chaal = chaal(board, plr2_chr, p2_pos)
        print(f"{Player_2} played:\n")
        display_board(p2Chaal)
        if game_over(p2Chaal):
            print(f"\n\t***{Player_2} WINS***\n\n")
            plr2_score += 1
            break
        elif game_over(p1Chaal) is None:
            print("\n\t*** Game is draw. points 50% split ***")
            plr1_score += 0.5
            plr2_score += 0.5
            break
