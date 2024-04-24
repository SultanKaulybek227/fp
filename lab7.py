import tkinter as tk
from create_acc import create_account

root = tk.Tk()
root.title("Тіркелу")

username_label = tk.Label(root, text="Логин:")
username_label.grid(row=0, column=0, sticky="w")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Парольды енгіз:")
password_label.grid(row=1, column=0, sticky="w")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

repeat_password_label = tk.Label(root, text="Қайта жаз:")
repeat_password_label.grid(row=2, column=0, sticky="w")

repeat_password_entry = tk.Entry(root, show="*")
repeat_password_entry.grid(row=2, column=1)

register_button = tk.Button(root, text="Тіркелу", command=lambda: create_account(username_entry, password_entry, repeat_password_entry))
register_button.grid(row=3, column=0, columnspan=2)

root.mainloop()


from tkinter import messagebox

def register_user(username, password, repeat_password):
    """
    Регистрирует пользователя.

    :param str username: Имя пользователя.
    :param str password: Пароль пользователя.
    :param str repeat_password: Повторный ввод пароля.
    """
    if password == repeat_password:
        messagebox.showinfo("Алақай!", "Пайдаланушы " + username + " сәтті тіркелді .")
    else:
        messagebox.showerror("Ой", "Пароль сәйкес келмейді.")


def create_account(username_entry, password_entry, repeat_password_entry):
    """
    Создает аккаунт пользователя.

    :param tk.Entry username_entry: Поле ввода имени пользователя.
    :param tk.Entry password_entry: Поле ввода пароля.
    :param tk.Entry repeat_password_entry: Поле ввода повторного пароля.
    """
    from register_user import register_user

    username = username_entry.get()
    password = password_entry.get()
    repeat_password = repeat_password_entry.get()
    register_user(username, password, repeat_password)
