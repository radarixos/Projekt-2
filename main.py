"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie - TicTacToe (piskvorky)

author: Radek Svejda

email: ok1vbr@gmail.com

discord: radarixos

"""
#godblessai4help

def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")


def check_winner(board, player):
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions


def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)


def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player} | Please enter your move number (1-9): "))
            if move < 1 or move > 9:
                print("Invalid choice, please enter a number between 1 and 9.")
            else:
                return move
        except ValueError:
            print("Invalid input, please enter a number.")


def update_board(board, move, player):
    row, col = divmod(move - 1, 3)
    if board[row][col] not in ["X", "O"]:
        board[row][col] = player
        return True
    else:
        print("The cell is already occupied, try a different move.")
        return False


def main():
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid.")
    print("The WINNER is who succeeds in placing three of their marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("========================================")
    print("Let's start the game")

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["O", "X"]
    current_player = 0

    print_board(board)

    while True:
        move = get_move(players[current_player])
        if update_board(board, move, players[current_player]):
            print("========================================")
            print_board(board)
            print("========================================")

            if check_winner(board, players[current_player]):
                print(f"Congratulations, the player {players[current_player]} WON!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            current_player = 1 - current_player


if __name__ == "__main__":
    main()
