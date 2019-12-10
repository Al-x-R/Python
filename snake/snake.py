import random
import tkinter as tk
from tkinter import simpledialog


def crossing():
    return any([snake[0].x == s.x and snake[0].y == s.y for s in snake[1:]])


def keypress(e):
    global direction
    if e.keycode == keys['left']: direction = 'left'
    if e.keycode == keys['right']: direction = 'right'
    if e.keycode == keys['up']: direction = 'up'
    if e.keycode == keys['down']: direction = 'down'


def start():  # запуск игры
    global snake, direction, head, counter
    head = snake[0]
    if direction == 'right':
        snake[-1].x = snake[0].x + 1
        if snake[-1].x == n:
            snake[-1].x = 0
        snake[-1].y = snake[0].y
    if direction == 'left':
        snake[-1].x = snake[0].x - 1
        if snake[-1].x == 1:
            snake[-1].x = n - 1
        snake[-1].y = snake[0].y
    if direction == 'up':
        snake[-1].x = snake[0].x
        snake[-1].y = snake[0].y - 1
        if snake[-1].y == -1:
            snake[-1].y = m - 1
    if direction == 'down':
        snake[-1].x = snake[0].x
        snake[-1].y = snake[0].y + 1
        if snake[-1].y == m:
            snake[-1].y = 0
    snake[-1].move()
    snake = snake[-1:] + snake[0:-1]
    if not crossing():
        root.after(200, start)
    else:
        label.config(text='game over\nyour score: {}'.format(counter))
        username = simpledialog.askstring('highscores',
                                          'введите имя')  # вызов окна для введения имени для  сохранения в журнал
        with open('journal.txt', 'a', encoding='utf-8') as f:
            f.write('name: {} score: {}\n'.format(username, counter))
            f.close()
        root.update_idletask()
    eating()
    label.config(text=counter)


def eating():  # поедание яблок
    global snake, direction, counter, head, R, G
    head = snake[0]
    x1, y1 = snake[-1].x, snake[-1].y  # координаты конца змеи last segnm coords
    if head.x == R.x and head.y == R.y:
        R.remove()
        snake.append(Segment(x1, y1, canvas, fill='grey'))
        counter += R.points
        R = RedApple(canvas)
    if head.x == G.x and head.y == G.y:
        G.remove()
        snake.append(Segment(x1, y1, canvas, fill='grey'))
        counter += G.points
        G = GreenApple(canvas)


class Segment:  # кружок
    def __init__(self, x, y, c, fill):  # координата... сегмента c отображает на канвасе
        self.x, self.y, self.c = x, y, c
        self.segment = c.create_oval(x * a, y * a, x * a + a, y * a + a, fill=fill)

    def move(self):  # перемещение сегмента
        self.c.coords(self.segment, self.x * a, self.y * a, self.x * a + a, self.y * a + a)

    def remove(self):  # удаление сегмента
        self.c.delete(self.segment)


class Apple(Segment):  # создаем класс яблоко
    def __init__(self, x, y, c, fill):
        super(Apple, self).__init__(x, y, c, fill)


class RandomApple(Apple):  # создаем наследуемый от яблока класс яблока произвольно появляющегося
    def __init__(self, c, fill):
        randX = random.randint(1, (((n * a) - a) / a))
        randY = random.randint(1, (((m * a) - a) / a))
        super(RandomApple, self).__init__(randX, randY, c, fill)


class RedApple(RandomApple):
    def __init__(self, c):
        super(RedApple, self).__init__(c, 'red')
        self.points = 2


class GreenApple(RandomApple):
    def __init__(self, c):
        super(GreenApple, self).__init__(c, 'green')
        self.points = 3


class Snake(Segment):
    def __init__(self, segment):
        self.segment = segment


m, n, a = 20, 20, 25  # размеры
root = tk.Tk()

label = tk.Label(root, font=('Courier', 40, 'bold'),
                 width=40, height=3, text='', highlightcolor="black")  # для вывода очков на экран
label.pack()

canvas = tk.Canvas(root, height=m * a, width=n * a, background='silver')  # создали канвас
canvas.pack()

direction = 'right'
keys = {'left': 37, 'right': 39, 'up': 38, 'down': 40}
counter = 0

snake = []
snake.append(Segment(7, 10, canvas, fill='grey'))
snake.append(Segment(6, 10, canvas, fill='grey'))
snake.append(Segment(5, 10, canvas, fill='grey'))

R = RedApple(canvas)
G = GreenApple(canvas)

root.bind('<Key>', keypress)
root.after(100, start)  # вызываем функцию запуск игры
root.mainloop()
