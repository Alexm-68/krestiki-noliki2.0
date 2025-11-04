import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

current_player = "X"
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)
# Функция сброса (reset_board), очищает поле и возвращает цвета по умолчанию
def reset_board():
    global current_player
    for row in buttons:
        for btn in row:
            btn.config(text="", fg="black")
    current_player = "X"

# Кнопка сброса
reset_button = tk.Button(window, text="Сброс", font=("Arial", 14), command=reset_board)
reset_button.grid(row=3, columnspan=3, sticky="we")

# •	Изменение цвета текста на кнопках при ходе (чтобы X был красным, 0 — синим):
if current_player == "X":
    buttons[i][j].config(fg="red")
else:
    buttons[row][col].config(fg="blue")


def on_click(row, col):
    pass


window.mainloop()