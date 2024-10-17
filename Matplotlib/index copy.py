import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Simple Calculator")

label1 = tk.Label(root, text="First Number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Second Number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

button_add = tk.Button(root, text="Add", command=add)
button_add.pack()

button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.pack()

button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
