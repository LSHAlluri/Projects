

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    """Checks if the board is full (i.e., no empty spaces left)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Initialize a 3x3 board with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]  # Players symbols
    turn = 0  # Tracks whose turn it is
    
    while True:
        # Print the current board state
        print_board(board)
        
        # Get user input for row and column
        row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
        
        # Validate if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = players[turn]
        else:
            print("Cell is already occupied! Try again.")
            continue
        
        # Check if there is a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check if the board is full (game ends in a tie)
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch turn to the other player
        turn = 1 - turn

if __name__ == "__main__":
    tic_tac_toe()