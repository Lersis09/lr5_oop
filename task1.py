import tkinter
from tkinter import messagebox


class Task1Window(tkinter.Frame):  # MainWindow наслідуючий клас Frame
    """Графічний інтерфейс користувача і логіка рішення задачі Func19"""

    def __init__(self, parent):
        """Початкові налаштування інтерфейсу користувача"""
        super().__init__(parent)  # виклик конструктора базового класу
        # Розтягнути фрейм за розмірами вікна
        self.pack(fill=tkinter.BOTH, expand=1)
        # Розтягнути сітку 2х2 за розмірами фрейма
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # Створити об'єкти віджетів (змінні екземпляра)
        self.lb1 = tkinter.Label(self, text="Enter 5 integer numbers:")  # статич. текст
        self.n_entr = tkinter.Entry(self)  # поле введення для n!
        # Командна кнопка (запуск обчислень)
        self.btn1 = tkinter.Button(self, text="Calculate factorial", command=self.calc_fact)
        self.n_str = tkinter.StringVar()  # змінна tkinter: факторіали в текстовому вигляді
        self.lb2 = tkinter.Label(self, textvariable=self.n_str)  # Текстове поле(n!)
        # Розмістити віджети в сітці 2х2
        self.lb1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.n_entr.grid(row=0, column=1, sticky=tkinter.NSEW)
        self.btn1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.lb2.grid(row=1, column=1, sticky=tkinter.NSEW)

    def calc_fact(self):
        """Введення-підрахунок-виведення згідно завданню Fuct19"""
        # Зчитування з поля введення
        try:
            n = int(self.n_entr.get())  # вважати і перетворити в ціле
        except ValueError:
            # Вивести вікно з помилкою
            messagebox.showerror("Data ERROR", "Number must be integer!")
            self.n_entr.delete(0, tkinter.END)  # очистити поле введення
        else:
            # Перевірити вхідні дані
         if not isinstance(n, int) or n < 0:
            # Вивести вікно з помилкою
            messagebox.showerror("Data ERROR", "Number must be positive integer!")
            self.n_entr.delete(0, tkinter.END)  # очистити поле введення
         else:
            # обчислення
            numbers = input("Введіть п'ять цілих чисел через кому: ")
            numbers = numbers.split(",")
            numbers = [int(n) for n in numbers]
            # Знайти факторіали вказаних чисел
            factorials = []
            for n in numbers:
                factorials.append(fact(n))
            # Вивести результати обчислень
            result = ",".join(str(n) for n in factorials)
            self.n_str.set(result)


def fact(n):
    """Функція для обчислення факторіалу"""
    if n < 0:
        raise ValueError("Factorial must be non-negative!")
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)
