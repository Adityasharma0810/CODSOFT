import tkinter as tk
from math import sqrt, sin, cos, tan, log10

# Function to handle button click
def button_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    elif value in ["sqrt", "sin", "cos", "tan", "log"]:
        try:
            num = float(current)
            if value == "sqrt":
                result = sqrt(num)
            elif value == "sin":
                result = sin(num)
            elif value == "cos":
                result = cos(num)
            elif value == "tan":
                result = tan(num)
            elif value == "log":
                result = log10(num)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

# Initialize Tkinter window
window = tk.Tk()
window.title("Python GUI Calculator")

# Entry widget for displaying the calculation
entry = tk.Entry(window, width=20, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'sqrt', 'sin', 'cos', 'tan',
    'log'
]

row_val = 1
col_val = 0

# Create and place buttons
for button in buttons:
    tk.Button(
        window,
        text=button,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda b=button: button_click(b)
    ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
window.mainloop()
