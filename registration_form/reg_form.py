import tkinter as tk
from tkinter import messagebox
import pickle

root = tk.Tk()
root.geometry('300x500')
root.title('Вход в систему')

def registration():
    text = tk.Label(text='Для входа в систему зарегистрируйтесь')
    text_login = tk.Label(text='Введите ваш логин')
    regisrt_login = tk.Entry()
    text_pass = tk.Label(text='ВВедите пароль')
    reg_pass = tk.Entry()
    text_pass2 = tk.Label(text='ВВедите пароль еще раз')
    reg_pass2 = tk.Entry(show='*')
    button_reg = tk.Button(text='registr', command=lambda: save() )

    text.pack()
    text_login.pack()
    regisrt_login.pack()

    text_pass.pack()
    reg_pass.pack()

    text_pass2.pack()
    reg_pass2.pack()

    button_reg.pack()

    def save():
        log_pass_save = {}
        log_pass_save[regisrt_login.get()] = reg_pass.get() #создаем словарь ключ значение
        f = open('login.txt', 'wb') #открываем файл и записываем в него
        pickle.dump(log_pass_save, f) #сохраняем наш логин пасс сейв в логин тхт
        f.close() #закрываем файл
        login() #вызываем функцию логи и привязваем ф-ю к кнопке зарегистрироваться

def login():
    text_log = tk.Label(text='поздравляем...')
    text_entr_log = tk.Label(text='Введите логин')
    entr_log  = tk.Entry()
    text_entr_pass = tk.Label(text='Введите пароль')
    entr_pass = tk.Entry(show='*')
    button_entr = tk.Button(text='Войти', command=lambda: log_pass_chek() )

    text_log.pack()
    text_entr_log.pack()
    entr_log.pack()
    text_entr_pass.pack()
    entr_pass.pack()
    button_entr.pack()

    def log_pass_chek():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if entr_log.get() in a:
            if entr_pass.get() == a[entr_log.get()]:
                messagebox.showinfo('Hello')
            else:
                messagebox.showerror('Неверный логин или пароль')
        else:
            messagebox.showerror('ошибка ввода')


registration()
root.mainloop()