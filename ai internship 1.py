import tkinter as tk
from tkinter import messagebox
import math

# Initial empty board
board = [[" " for _ in range(3)] for _ in range(3)]
winning_cells = []

# Function to check the winner
def check_winner(b):
    global winning_cells
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != " ":
            winning_cells = [(i, 0), (i, 1), (i, 2)]
            return b[i][0]
    for j in range(3):
        if b[0][j] == b[1][j] == b[2][j] != " ":
            winning_cells = [(0, j), (1, j), (2, j)]
            return b[0][j]
    if b[0][0] == b[1][1] == b[2][2] != " ":
        winning_cells = [(0, 0), (1, 1), (2, 2)]
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != " ":
        winning_cells = [(0, 2), (1, 1), (2, 0)]
        return b[0][2]
    return None

# Check if board is full
def is_full(b):
    return all(cell != " " for row in b for cell in row)

# Minimax Algorithm for AI
def minimax(b, is_maximizing):
    winner = check_winner(b)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(b):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = "O"
                    score = minimax(b, False)
                    b[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = "X"
                    score = minimax(b, True)
                    b[i][j] = " "
                    best_score = min(score, best_score)
        return best_score
# Find best move for AI
def best_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
# Handle button click
def button_click(i, j):
    if board[i][j] == " ":
        board[i][j] = "X"
        update_button(i, j, "X", "red")

        winner = check_winner(board)
        if winner:
            highlight_winner()
            end_game(f"{winner} wins!")
            return
        elif is_full(board):
            end_game("It's a Tie!")
            return

        ai_i, ai_j = best_move()
        board[ai_i][ai_j] = "O"
        update_button(ai_i, ai_j, "O", "blue")

        winner = check_winner(board)
        if winner:
            highlight_winner()
            end_game(f"{winner} wins!")
        elif is_full(board):
            end_game("It's a Tie!")

def update_button(i, j, symbol, color):
    buttons[i][j].config(text=symbol, fg=color, disabledforeground=color)
    buttons[i][j]["state"] = "disabled"
# Highlight winning 3 cells
def highlight_winner():
    for (i, j) in winning_cells:
        buttons[i][j]["bg"] = "lightgreen"
# End game popup
def end_game(msg):
    messagebox.showinfo("Game Over", msg)
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe AI - Subhiksha")

buttons = [[None for _ in range(3)] for _ in range(3)]
# Create buttons for grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root, text=" ", font=('Arial', 40), width=5, height=2,
            command=lambda i=i, j=j: button_click(i, j),
            bg="white", fg="black", disabledforeground="black"
        )
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
