import tkinter
from tkinter import messagebox

class Task1Window(tkinter.Frame):
    """Графічний інтерфейс користувача і логіка рішення задачі Func19"""
    
    def __init__(self, parent):
        """Початкові налаштування інтерфейсу користувача"""
        super().__init__(parent)
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
        self.btn1 = tkinter.Button(self, text="Calculate factorials", command=self.calc_fact)
        self.n_str = tkinter.StringVar()  # змінна tkinter: факторіали в текстовому вигляді
        self.lb2 = tkinter.Label(self, textvariable=self.n_str)  # Текстове поле(n!)
        # Розмістити віджети в сітці 2х2
        self.lb1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.n_entr.grid(row=0, column=1, sticky=tkinter.NSEW)
        self.btn1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.lb2.grid(row=1, column=1, sticky=tkinter.NSEW)
    
    def calc_fact(self):
        """Введення-підрахунок-виведення згідно завдання Fuct19"""
        # Зчитування з поля введення
        try:
            input_numbers = self.n_entr.get().split()  # вважати і розбити по пробілах
            numbers = [int(num) for num in input_numbers]  # перетворити в цілі числа
        except ValueError:
            # Вивести вікно з помилкою
            messagebox.showerror("Data ERROR", "Numbers must be integers!")
            self.n_entr.delete(0, tkinter.END)  # очистити поле введення
        else:
            # Перевірити вхідні дані
            if len(numbers) != 5:
                # Очистити поле
                self.n_entr.delete(0, tkinter.END)
                self.n_entr.insert(tkinter.END, ' '.join(str(num) for num in numbers))
                # Вивести вікно з попередженням
                messagebox.showinfo("Data Warning", "Enter exactly 5 integer numbers")
            elif any(num <= 0 for num in numbers):
                messagebox.showerror("Data ERROR", "Numbers must be greater than 0!")
                self.n_entr.delete(0, tkinter.END)  # очистити поле введення  
            else:
                # обчислення факторіалів
                factorials = [self.Fact(num) for num in numbers]
                # Виведення результату в текстову мітку (за допомогою змінної tkinter)
                self.n_str.set(' '.join(str(fact) for fact in factorials))
    
    def Fact(self, N):
        """Функція для обчислення факторіалу"""
        if N == 0:
            return 1
        else:
            return N * self.Fact(N - 1)