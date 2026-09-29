from tkinter import *
import psycopg
from tkinter import messagebox
conn = psycopg.connect(
    host="localhost",
    dbname="user",
    user="postgres",
    password="972279"
)
cursor = conn.cursor()

root = Tk()
root.geometry("1280x720")
root.title("Окно для ввода данных")
root.configure(bg = '#2F4F4F')

def Register():
    Login = StringLogin.get()
    Parol = StringParol.get()
    if Login == "" or Parol == "":
        messagebox.showerror('Ошибка', ' Заполните все поля')
        return
    cursor.execute("SELECT * FROM users WHERE login = %s", (Login,))
    existing = cursor.fetchone()
    if existing is not None:
        messagebox.showerror('Упсссссс','Такой пользователь уже есть')
        return
    cursor.execute("INSERT INTO users (Login, Parol) VALUES (%s, %s)", (Login, Parol))
    messagebox.showerror('Да', 'Успех')
    conn.commit()

def Create():
    Login = StringLogin.get()
    Parol = StringParol.get()
    if Login == "" or Parol == "":
        messagebox.showerror('Ошибка', ' Заполните все поля')
        return
    cursor.execute("SELECT * FROM users WHERE login = %s AND parol = %s", (Login, Parol))
    users = cursor.fetchone()
    if users is None:
        messagebox.showerror('Что то пошло не так', 'Такого пользователя нет')
        return
    messagebox.showinfo('Вход успешен', 'Вы вошли')


def NewAccount():
    global CreateAccountRoot, StringCreateLogin, StringCreateParol
    CreateAccountRoot = Toplevel()
    CreateAccountRoot.geometry("1280x720")
    CreateAccountRoot.title("Окно для регистрации")
    CreateAccountRoot.configure(bg='#2F4F4F')
    TextCreateLogin = Label(CreateAccountRoot, text='Введите логин', bg='#2F4F4F', font=("Arial", 10))
    TextCreateLogin.pack()
    StringCreateLogin = Entry(CreateAccountRoot, width=50)
    StringCreateLogin.pack(pady=10)

    # Создание пароля
    TextCreateParol = Label(CreateAccountRoot, text='Введите пароль', bg='#2F4F4F', font=("Arial", 10))
    TextCreateParol.pack()
    StringCreateParol = Entry(CreateAccountRoot, width=50)
    StringCreateParol.pack(pady=10)

    # Кнопка для регистрации
    EnterCreateAccount = Button(CreateAccountRoot, text='Создать аккаунт', bg='#483D8B', command = Register)
    EnterCreateAccount.place(x=590, y=250)

# Заголовок
TextGlav = Label(root, text = 'Добро пожаловать на платформу!\nДля проверки входа введите свой логин и пароль',
bg = '#2F4F4F', font = ("Arial", 14))
TextGlav.pack(pady = 30)

# Логин
TextLogin = Label(root, text = 'Введите логин', bg = '#2F4F4F', font = ("Arial", 10))
TextLogin.pack()
StringLogin = Entry(root, width = 50)
StringLogin.pack(pady = 10)

# Пароль
TextParol = Label(root, text = 'Введите пароль', bg = '#2F4F4F', font = ("Arial", 10))
TextParol.pack()
StringParol = Entry(root, width = 50)
StringParol.pack(pady = 10)

#Кнопка для входа
EnterAccount= Button(root, text = 'Войти в аккаунт', bg = '#483D8B', command = Create)
EnterAccount.place(x = 590, y = 250)

#Кнопка для регистрации
TextRegis = Label(root, text = 'Нет аккаунта?', bg = '#2F4F4F', font = 15)
TextRegis.pack(pady = 200)
NewAccount = Button(root, text = 'Создать аккаунт', bg = '#483D8B', command = NewAccount)
NewAccount.place(x = 590, y = 500)


root.mainloop()