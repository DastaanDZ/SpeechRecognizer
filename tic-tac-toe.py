import numpy as np
board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s = 'X'
p2s = 'O'

def won(symbol):
    check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def check_rows(symbol):
    
def place(symbol):
    print(np.matrix(board))
    while True:
        row = int(input("Enter row: 1 or 2 or 3: "))
        col = int(input("Enter column: 1 or 2 or 3: "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid input. Please enter again.")
    board[row-1][col-1] = symbol

def play():
    for turn in range(9):
        if turn%2 == 0:
            print("X's turn")
            place(p1s)
            if won(p1s):
                print("Player 1 won")
                break
        else:
            print("O's turn")
            place(p2s)
            if won(p2s):
                print("Player 2 won")
                break
        if not(won(p1s)) and not(won(p2s)) and turn==8:
            print("Draw")
