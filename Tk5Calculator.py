from tkinter import *
from math import *

root = Tk()
root.title("Bhanja Calculator")
root.configure(background="blue")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global math
    math = "addition"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global math
    math = "subtraction"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global math
    math = "multiplication"
    global f_num
    f_num = float(first_number)
    e.delete(0, END)


def button_sqrt():
    first_number = e.get()
    global math
    math = "sqrt"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global math
    math = "division"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_sin():
    first_number = e.get()
    global math
    math = "square"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_mod():
    first_number = e.get()
    global math
    math = "MOD"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_intdivide():
    first_number = e.get()
    global math
    math = "intdivision"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if (math == "addition"):
        e.insert(0, f_num + float(second_number))
    if (math == "subtraction"):
        e.insert(0, f_num - float(second_number))
    if (math == "multiplication"):
        e.insert(0, f_num * float(second_number))
    if (math == "division"):
        e.insert(0, f_num / float(second_number))
    if (math == "MOD"):
        e.insert(0, f_num % float(second_number))
    if (math == "intdivision"):
        e.insert(0, f_num // float(second_number))
    if (math == "square"):
        e.insert(0, f_num * f_num)


# define the buttons

button_1 = Button(root, text="1", bg="light green", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="light green", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, bg="light green", pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, bg="light green", pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="light green", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="light green", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="light green", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="light green", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="light green", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="light green", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, bg="light green", command=button_add)
button_subtract = Button(root, text="-", padx=41, pady=20, bg="light green", command=button_subtract)
button_multiply = Button(root, text="*", padx=45, pady=20, bg="light green", command=button_multiply)
button_divide = Button(root, text="/", padx=58, pady=20, bg="light green", command=button_divide)
button_equal = Button(root, text="=", padx=105, pady=20, bg="light green", command=button_equal)
button_clear = Button(root, text="Clear", padx=95, pady=20, bg="light green", command=button_clear)
button_mod = Button(root, text="%", padx=42, pady=20, bg="light green", command=button_mod)
button_int = Button(root, text="int(/)", padx=45, pady=20, bg="light green", command=button_intdivide)
button_exp = Button(root, text="Square", padx=42, pady=20, bg="light green", command=button_sin)
# Put the butttons on the screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_mod.grid(row=7, column=0)
button_int.grid(row=7, column=1)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_exp.grid(row=7, column=2)

root.mainloop()
