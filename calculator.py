import tkinter as tk
from functools import partial

def add(x,y):
    return x + y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x,y):
    if y== 0:
        return "Error!"
    return x/y

def calculate(operation, num1_entry, num2_entry, result_label):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = operation(num1, num2)
        result_label.config(text= f"Result: {result}")
    except ValueError:
        result_label.config(text= "Invalid Input")


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x500")

num1_label =tk.Label(window, text= "Enter first number")
num1_label.pack(padx= 50, pady=50)
num1_entry = tk.Entry(window)
num1_entry.pack()

num2_label = tk.Label(window, text = "Enter second number")
num2_label.pack(padx= 50, pady=50)
num2_entry = tk.Entry(window)
num2_entry.pack()

result_label = tk.Label(window, text="Result")
result_label.pack(padx=50, pady=50)
result_entry = tk.Entry(window)

button_frame = tk.Frame(window)
button_frame.pack()

btn_add = tk.Button(button_frame, text="Add", command=partial(calculate, add, num1_entry, num2_entry, result_label))
btn_add.grid(row = 0, column =0)

btn_subtract = tk.Button(button_frame, text="Subtract", command=partial(calculate, subtract, num1_entry, num2_entry, result_label))
btn_subtract.grid(row = 0, column =1)

btn_multiply = tk.Button(button_frame, text="Multiply", command=partial(calculate, multiply, num1_entry, num2_entry, result_label))
btn_multiply.grid(row = 0, column =2)

btn_divide = tk.Button(button_frame, text="Divide", command=partial(calculate, divide, num1_entry, num2_entry, result_label))
btn_divide.grid(row = 0, column =3)



window.mainloop()



