import tkinter as tk
from tkinter import simpledialog, messagebox

name1, name2 = 'Krestik', 'Nolik'
win_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
p1, p2 = [], []

root = tk.Tk()
root.title('Tic Tac Toe')
symbol = 'X'

buttons = []

for i in range(3):
    for j in range(3):
        buttons.append(tk.Button(root, font=('Arial', 26), text=' ', width=7, height=3))
        buttons[-1].grid(row=i, column=j)
        buttons[-1]['command'] = lambda x=len(buttons): click(x)


def click(arg):
    global p1, p2, symbol
    if symbol == 'X':
        p1.append(arg)
    else:
        p2.append(arg)
    print(p1, p2)
    change_view(arg)
    check_winner()
    if symbol == 'X':
        symbol = 'O'
    else:
        symbol = 'X'


def check_winner():
    if any([contains(item, p1) for item in win_combos]):
        messagebox.showinfo('', f'winner is  {name1}!')
        root.destroy()
    if any([contains(item, p2) for item in win_combos]):
        messagebox.showinfo('', f'winner is  {name2}!')
        root.destroy()


def contains(small, big):
    return all([s in big for s in small])


def pass_command():
    pass


def change_view(arg):
    global symbol, buttons
    buttons[arg - 1].config(text=symbol, command=pass_command)


root.mainloop()
