import tkinter as tk
from tkinter import ttk


root = tk.Tk();
root.title("Modern Calculator")
root.resizable(False, False)

BUTTONS_WIDTH, BUTTONS_HEIGHT = 2, "3m"
DEFAULT_FONT = ("Helvetica", 20, "normal")

total_text = ""
number_text = ""

numbers = {
    7: (1, 0),
    8: (1, 1),
    9: (1, 2),
    4: (2, 0),
    5: (2, 1),
    6: (2, 2),
    1: (3, 0),
    2: (3, 1),
    3: (3, 2),
    0: (4, 0),
    ".": (4, 2),
}

operators = {"\u00F7": (0, 3), "x": (1, 3), "-": (2, 3), "+": (3, 3)}

def add_number(value):
    global total_text, number_text
    number_text += str(value)
    total_text += str(value)
    display_box.config(text=number_text)

def add_operator(operator):
    global total_text, number_text
    total_text = total_text + str(operator)
    number_text = ""

def calculate_total():
    global total_text, number_text
    try:
       total_text = str(total_text).replace("x", "*").replace("\u00F7", "/")
       total = eval(total_text)
       display_box.config(text=total)
       total_text = str(total)
    except ZeroDivisionError:
       display_box.config(text="Not a number")
       total_text, number_text = "", ""
    except Exception:
        display_box.config(text="Error")
        total_text, number_text = "", ""

def calculate_percentage():
    global total_text, number_text
    total_text = str(eval(total_text) / 100)
    number_text = total_text
    display_box.config(text=total_text)

def negate_total():
    global total_text, number_text
    if total_text.startswith("-") or number_text.startswith("-"):
        total_text = "+" + total_text[1:]
        number_text = "+" + number_text[1:]
    elif total_text.startswith("+") or number_text.startswith("+"):
        total_text = "-" + total_text[1:]
        number_text = "-" + number_text[1:]
    else:
        total_text = "-" + total_text
        number_text = "-" + number_text

    display_box.config(text=total_text)

def clear():
    global total_text, number_text
    total_text, number_text = "", ""
    display_box.config(text="0")


calculator_frame = tk.Frame(root)
calculator_frame.pack()

display_box = ttk.Label(
    calculator_frame,
    text="0",
    font=("Helvetica", 40, "normal"),
    anchor="ne",
    width=BUTTONS_WIDTH * 4
)
display_box.pack(anchor="center", fill="both", pady=8)

numbers_and_operators_frame = tk.Frame(calculator_frame)
numbers_and_operators_frame.pack(expand=True, fill="both")

clear_btn = tk.Button(
    numbers_and_operators_frame,
    text="C",
    font=DEFAULT_FONT,
    borderwidth=0,
    width=BUTTONS_WIDTH,
    fg="#25265E",
    command=clear
)
clear_btn.grid(row=0, column=0, sticky=tk.NSEW, ipady=BUTTONS_HEIGHT)

neg_btn = tk.Button(
    numbers_and_operators_frame,
    text="+/-",
    font=DEFAULT_FONT,
    borderwidth=0,
    width=BUTTONS_WIDTH,
    fg="#25265E",
    command=negate_total
)
neg_btn.grid(row=0, column=1, sticky=tk.NSEW)


percentage_btn = tk.Button(
    numbers_and_operators_frame,
    text="%",
    font=DEFAULT_FONT,
    borderwidth=0,
    width=BUTTONS_WIDTH,
    fg="#25265E",
    command=calculate_percentage
)
percentage_btn.grid(row=0, column=2, sticky=tk.NSEW)

equals_btn = tk.Button(
    numbers_and_operators_frame,
    text="=",
    font=DEFAULT_FONT,
    borderwidth=0,
    width=BUTTONS_WIDTH,
    fg="#25265E",
    command=calculate_total
)   

equals_btn.grid(row=4, column=3, sticky=tk.NSEW)


for value, pos in numbers.items():
    number = tk.Button(
        numbers_and_operators_frame,
        text=value,
        font=DEFAULT_FONT,
        width=BUTTONS_WIDTH,
        command=lambda number=value: add_number(number)
    )

    if value == 0:
        number.grid(row=pos[0], column=pos[1], columnspan=2, sticky=tk.NSEW, ipady=BUTTONS_HEIGHT)
    else:
        number.grid(row=pos[0], column=pos[1], sticky=tk.NSEW, ipady=BUTTONS_HEIGHT)

for value, pos in operators.items():
    operator = tk.Button(
        numbers_and_operators_frame,
        text=value,
        font=DEFAULT_FONT,
        width=BUTTONS_WIDTH,
        command=lambda operator=value: add_operator(operator)
    )

    operator.grid(row=pos[0], column=pos[1], sticky=tk.NSEW, ipady=BUTTONS_HEIGHT)


root.mainloop()