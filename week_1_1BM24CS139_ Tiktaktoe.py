# Tic-Tac-Toe Game

board = [str(i) for i in range(1, 10)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_win(player):
    winning_combinations = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3

        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3

        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False


def check_draw():
    return all(spot in ["X", "O"] for spot in board)


# Main Game Loop
print("Welcome to Tic-Tac-Toe!")

current_player = "X"

while True:

    print_board()

    choice = input(f"Player {current_player}, choose a spot (1-9): ")

    # Check if input is a number
    if not choice.isdigit():
        print("Please enter a number between 1 and 9.")
        continue

    position = int(choice) - 1

    # Check if position is valid
    if position < 0 or position > 8:
        print("Please choose a number between 1 and 9.")
        continue

    # Check if spot is already taken
    if board[position] in ["X", "O"]:
        print("That spot is already taken!")
        continue

    # Place X or O
    board[position] = current_player

    # Check for winner
    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins! 🎉")
        break

    # Check for draw
    if check_draw():
        print_board()
        print("It's a draw!")
        break

    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"