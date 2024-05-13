def minimax(board, depth, is_maximizing):
    if check_winner('X', board):  # Assuming 'X' is the computer
        return 1
    elif check_winner('O', board):  # Assuming 'O' is the human
        return -1
    elif '' not in board:  # No more moves left, it's a draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board)):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def make_computer_move():
    best_score = -float('inf')
    move = None
    for i in range(len(squares)):
        if squares[i] == '':
            squares[i] = 'X'
            score = minimax(squares, 0, False)
            squares[i] = ''
            if score > best_score:
                best_score = score
                move = i
    squares[move] = 'X'

def check_winner(player, squares):
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(squares[cell] == player for cell in condition) for condition in winning_conditions)

game_active = True
current_player = 'O'
squares = ['' for _ in range(9)]  # Representa el tablero del juego

while game_active:
    make_computer_move()
    if check_winner(current_player, squares):
        print(f'¡Ganó el jugador {current_player}!')
        game_active = False
    else:
        current_player = 'X' if current_player == 'O' else 'O'