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


def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player
    # Изменение цвета текста на кнопках при ходе (чтобы X был красным, 0 — синим):
    if current_player == "X":
        buttons[row][col].config(fg="red")
    else:
        buttons[row][col].config(fg="blue")

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_board()
        return
    if is_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_board()
        return

    current_player = "0" if current_player == "X" else "X"


def is_draw():
    # Если все кнопки заполнены и никто не победил
    return all(btn['text'] != "" for row_btn in buttons for btn in row_btn)



def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


window.mainloop()