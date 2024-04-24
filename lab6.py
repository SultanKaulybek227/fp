import tkinter as tk

class ReactiveCounter:
    def __init__(self):
        self.value = 0
        self.observers = []

    def increment(self):
        self.value += 1
        self.notify_observers()

    def decrement(self):
        self.value -= 1
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer(self.value)

# Создаем экземпляр счетчика
counter = ReactiveCounter()

# Функция для обновления текстового виджета счетчика
def update_counter_label(value):
    counter_label.config(text="Текущее значение счетчика: {}".format(value))

# Создаем окно Tkinter
root = tk.Tk()
root.title("Реактивный счетчик")

# Создаем текстовый виджет для отображения значения счетчика
counter_label = tk.Label(root, text="Текущее значение счетчика: {}".format(counter.value))
counter_label.pack()

# Создаем кнопки для увеличения и уменьшения счетчика
increment_button = tk.Button(root, text="Увеличить", command=counter.increment)
increment_button.pack()

decrement_button = tk.Button(root, text="Уменьшить", command=counter.decrement)
decrement_button.pack()

# Добавляем функцию обновления текстового виджета в список наблюдателей счетчика
counter.add_observer(update_counter_label)

root.mainloop()
