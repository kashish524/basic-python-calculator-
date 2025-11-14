from tkinter import *
import math

# Main window........................................................
root = Tk()
root.title("Advanced Scientific Calculator")
root.geometry("420x650")
root.configure(bg="#1e1e1e")

expression = ""

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def equal_press():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def scientific(func):
    global expression
    try:
        value = float(expression)
        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)

        input_text.set(str(result))
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Input Display
input_text = StringVar()
entry = Entry(root, font=("Arial", 22), textvariable=input_text, bd=10, relief=RIDGE, bg="#ffffff", fg="black", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=15, ipadx=10, ipady=15)

# Buttons Layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, bg="#47a3f3", fg="white", font=("Arial", 16), command=equal_press, height=2, width=7)\
        .grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, bg="#333333", fg="white", font=("Arial", 16), 
        command=lambda t=text: press(t), height=2, width=7)\
        .grid(row=row, column=col, padx=5, pady=5)

# Scientific Buttons
sci_buttons = [
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3),
    ("sqrt", 6, 0)
]

for (text, row, col) in sci_buttons:
    Button(root, text=text, bg="#ff9800", fg="black", font=("Arial", 15, "bold"),
    command=lambda t=text: scientific(t), height=2, width=7)\
    .grid(row=row, column=col, padx=5, pady=5)

# Clear Button
Button(root, text="CLEAR", bg="#ff3b3b", fg="white", font=("Arial", 16), command=clear, height=2, width=33)\
    .grid(row=7, column=0, columnspan=4, pady=10)


# ---------------- TOGGLE THEME FUNCTION (CORRECT PLACE) ----------------

def toggle_theme():
    current = root.cget("bg")
    if current == "#1e1e1e": 
        root.configure(bg="white")
        entry.configure(bg="white", fg="black")
    else:
        root.configure(bg="#1e1e1e")
        entry.configure(bg="white", fg="black")

# Toggle Theme Button
Button(root, text="Toggle Theme", command=toggle_theme, height=2, width=33)\
    .grid(row=8, column=0, columnspan=4, pady=10)


# ---------------- ONLY ONE MAINLOOP ----------------
root.mainloop()
