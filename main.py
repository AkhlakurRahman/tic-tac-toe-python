# Game Board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_",
         ]

# Check if game is still going
check_if_game_still_going = True

# Winner or tie
winner = None

# Current player
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):
    print(player + "'s turn")
    position = input("Please enter a position between 1-9: ")

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "Invalid input. Please enter a position between 1-9: ")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("Already filled. Try again with another position.")

    board[position] = current_player
    display_board()


def check_if_win():
    # Set global winner variable
    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    global check_if_game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        check_if_game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_columns():
    global check_if_game_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        check_if_game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    global check_if_game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    if diagonal_1 or diagonal_2:
        check_if_game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_draw():
    global check_if_game_still_going
    if "_" not in board:
        check_if_game_still_going = False

    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


def check_if_game_over():
    check_if_win()
    check_if_draw()


def start_game():
    display_board()

    while check_if_game_still_going:

        # Handle turn for every player
        handle_turn(current_player)

        # To check if game is over or not
        check_if_game_over()

        # Flip to other player
        flip_player()

    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


start_game()
