import tkinter as tk
from tkinter import messagebox

# Variables globales
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Función para manejar clic
def handle_click(row, col):
    global current_player

    if board[row][col] != "":
        return

    board[row][col] = current_player
    buttons[row][col].config(text=current_player)

    if check_winner():
        messagebox.showinfo("Fin del juego", f"Ganó {current_player}")
        reset_game()
        return

    if check_draw():
        messagebox.showinfo("Fin del juego", "Empate")
        reset_game()
        return

    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Turno: {current_player}")

# Verificar ganador
def check_winner():
    # filas
    for row in board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return True

    # columnas
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return True

    # diagonales
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

# Verificar empate
def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

# Reiniciar juego
def reset_game():
    global current_player, board

    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]

    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")

    status_label.config(text=f"Turno: {current_player}")

# Crear ventana
root = tk.Tk()
root.title("Tic-Tac-Toe PRO")
root.geometry("400x500")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Tic-Tac-Toe", font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)

status_label = tk.Label(root, text=f"Turno: {current_player}", font=("Arial", 12), fg="white", bg="#1e1e1e")
status_label.pack(pady=5)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

# Crear botones del tablero
for r in range(3):
    for c in range(3):
        btn = tk.Button(
            frame,
            text="",
            font=("Arial", 24, "bold"),
            width=5,
            height=2,
            bg="#2d2d2d",
            fg="white",
            activebackground="#444",
            command=lambda row=r, col=c: handle_click(row, col)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

# Botón reset
reset_btn = tk.Button(root, text="Reiniciar", font=("Arial", 12), command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()