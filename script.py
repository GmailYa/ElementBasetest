# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

def submit():
    # Получаем значения из полей ввода и чек-боксов
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()

    combo1_value = combo1.get()
    combo2_value = combo2.get()
    combo3_value = combo3.get()

    check1_value = check1_var.get()
    check2_value = check2_var.get()
    check3_value = check3_var.get()

    print("Text 1:", text1)
    print("Text 2:", text2)
    print("Text 3:", text3)
    print("Combo 1:", combo1_value)
    print("Combo 2:", combo2_value)
    print("Combo 3:", combo3_value)
    print("Check 1:", check1_value)
    print("Check 2:", check2_value)
    print("Check 3:", check3_value)

# Создаем главное окно
root = tk.Tk()
root.title("Пример формы")

# Поля ввода текста
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

entry3 = tk.Entry(root)
entry3.pack(pady=5)

# Комбо-боксы
combo1 = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo1.pack(pady=5)

combo2 = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo2.pack(pady=5)

combo3 = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo3.pack(pady=5)

# Чек-боксы
check1_var = tk.BooleanVar()
check1 = tk.Checkbutton(root, text="Check 1", variable=check1_var)
check1.pack(pady=5)

check2_var = tk.BooleanVar()
check2 = tk.Checkbutton(root, text="Check 2", variable=check2_var)
check2.pack(pady=5)

check3_var = tk.BooleanVar()
check3 = tk.Checkbutton(root, text="Check 3", variable=check3_var)
check3.pack(pady=5)

# Кнопка отправки
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Запуск главного цикла
root.mainloop()
