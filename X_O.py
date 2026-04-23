def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Choose a number between 1 and 9.")
                continue

            row = 2 - ((move - 1) // 3)
            col = (move - 1) % 3

            if board[row][col] != " ":
                print("That position is already taken. Try again.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("""
Board positions:

7 | 8 | 9
4 | 5 | 6
1 | 2 | 3
""")

    while True:
        mode = input("Choose game mode:\n1) Default\n2) Endless\nEnter 1 or 2: ")
        if mode in ["1", "2"]:
            break
        print("Invalid choice.")

    while True:
        player1 = input("Player 1, choose X or O: ").upper()
        if player1 in ["X", "O"]:
            break
        print("Invalid choice. Please choose X or O.")

    player2 = "O" if player1 == "X" else "X"
    current_player = player1

    moves = {player1: [], player2: []}

    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        moves[current_player].append((row, col))

        if mode == "2" and len(moves[current_player]) > 3:
            old_row, old_col = moves[current_player].pop(0)
            board[old_row][old_col] = " "

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if mode == "1" and is_board_full(board):
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    main()