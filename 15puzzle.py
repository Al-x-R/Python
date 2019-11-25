import tkinter as tk, random as rnd
from tkinter import messagebox as mb
from tkinter import simpledialog

root = tk.Tk()
root.title('15 PUZZLE')
field = []


cellnumber = simpledialog.askinteger('размер поля', 'введите количество клеток линии')
n = cellnumber * cellnumber

def set_nums():
    global field
    captions = [str(i) for i in range(1, n)] + ['']
    rnd.shuffle(captions)
    #print(captions)
    for i in range(len(field)):
        field[i]['text'] = captions[i]

def set_field():
    global field
    for i in range(cellnumber):
        for j in range(cellnumber):
            field.append(tk.Label(root, font=('Arial', 20), text='', width=6,
                height=3, borderwidth=1, relief='solid'))
            field[-1].grid(row=i, column=j)
    set_nums()

def get_empty_index():
    for i in range(len(field)):
        if field[i]['text'] == '':
            return i



def is_victory():
    for i in range(len(field)-1):
        if field[i]['text'] != str(i + 1):
            return False
    return True

def cheeting():
    global field
    for i in range(n):
        field[i]['text'] = str(i+1)
    field[n-4]['text'] = ''
    field[n-3]['text'] = str(n-3)
    field[n-2]['text'] = str(n-2)
    field[n-1]['text'] = str(n-1)

def keypress(e):
    global field
    empty = get_empty_index()
    print(e.keycode)
    if e.keycode == 8320768 and empty > cellnumber - 1: # up
        field[empty]['text'], field[empty-cellnumber]['text'] = field[empty-cellnumber]['text'], field[empty]['text']
    if e.keycode == 8255233 and empty < n - cellnumber: # down
        field[empty]['text'], field[empty+cellnumber]['text'] = field[empty+cellnumber]['text'], field[empty]['text']
    if e.keycode == 8189699 and empty % cellnumber != 0: # right
            field[empty]['text'], field[empty-1]['text'] = field[empty-1]['text'], field[empty]['text']
    if e.keycode == 8124162 and empty not in [ i  for i in range(cellnumber - 1, n, cellnumber)]:# left #% 4 != cellnumber - 1:
            print([ i  for i in range(cellnumber - 1, n, cellnumber)])
            field[empty]['text'], field[empty+1]['text'] = field[empty+1]['text'], field[empty]['text']
    print(empty)
    if e.keycode == 32: cheeting()
    if is_victory():
        mb.showinfo('ПОБЕДА!!!', 'Ты это сделал!!!')

root.bind('<Key>', keypress)
set_field()
root.mainloop()
