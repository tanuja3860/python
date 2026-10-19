board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
def display_board():
    print("\n")
    for row in board:
        print(" | ".join(row))
    print()
def check_winner(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
def is_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True
def minimax(depth, is_maximizing):
    if check_winner('X'):
        return 10 - depth
    if check_winner('O'):
        return depth - 10
    if is_full():
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(depth + 1, False)
                    board[i][j] = '-'
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(depth + 1, True)
                    board[i][j] = '-'
                    best_score = min(best_score, score)
        return best_score
print("TIC TAC TOE")
print("Player 1: X")
print("Player 2: O")
print("Enter row and column values from 0 to 2")
display_board()
current_player = 'X'
while True:
    if current_player == 'X':
        print("Player 1 Turn")
    else:
        print("Player 2 Turn")
    row = int(input("Enter row (x) VALUE: "))
    col = int(input("Enter column (y) VALUE: "))
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid position! Enter values from 0 to 2.")
        continue
    if board[row][col] != '-':
        print("Cell already occupied! Choose another cell.")
        continue
    board[row][col] = current_player
    print(f"\nUpdated Grid ({current_player} placed at {row},{col}):")
    display_board()
    if check_winner(current_player):
        if current_player == 'X':
            print("Player 1 (X) Wins!")
        else:
            print("Player 2 (O) Wins!")
        print("Game Over.")
        break
    if is_full():
        print("Game Draw!")
        print("Game Over.")
        break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'