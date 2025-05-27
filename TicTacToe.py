

def print_board(board):

    # Prints the current state of the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row)) # Join and print cells with vertical bars
        print("-" * 9) # Print a horizontal line

def check_winner(board):
    
    # Checks if there is a winner on the board and returns the winner (X or O).
    # Check rows for a winner
    for row in board: 
        # board is a (3x3 grid) list of lists. So the loop goes through the 3 list elements 
        # which are the 3 rows, going through each row for each iteration
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
    # Checks if the board is full (i.e., no empty spaces left).
    # using a nested for loop to check if every cell in the 3x3 grid is full
    # for each row in the board:
    #   for each cell in that row:
    #       ....
    # the all() function returns true, if every condition inside is true, 
    # i.e., if every cell is full
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    # Main function to run the Tic-Tac-Toe game.
    # Initialize a 3x3 board with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    players = ["X", "O"]  # Players symbols
    turn = 0  # Start with Player X (index 0) and Tracks whose turn it is
    
    print("Welcome to Tic-Tac-Toe!\n")
    print("Players take turns entering row and column numbers (0 to 2) to place their mark.\n")
    
    while True:
        # Print the board before each turn
        print_board(board)
        
        # Get the player's input for row and column
        try:
            row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers between 0 and 2 separated by a space.\n")
            continue

        # Validate row and column range of the tic tac toe board
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2. Try again.\n")
            continue

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            # place the player's symbol. 'turn' is the index for the list 
            # 'players' that contains the players 'X' and 'O'
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


tic_tac_toe()