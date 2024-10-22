import tkinter as tk
import tkinter.messagebox
import math

# Main window setup
window = tk.Tk()
window.title('Calculator')
window.configure(bg='black')

# Entry field for expressions
entry = tk.Entry(master=window, relief=tk.SUNKEN, borderwidth=3, width=35, bg='black', fg='white', font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, ipady=10, pady=10)

# Memory storage
memory = 0

# Button click function
def myclick(number):
    entry.insert(tk.END, number)

# Evaluation function with error handling
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Clear entry field
def clear():
    entry.delete(0, tk.END)

# Memory functions
def memory_clear():
    global memory
    memory = 0

def memory_recall():
    global memory
    entry.insert(tk.END, memory)

def memory_add():
    global memory
    try:
        memory += float(eval(entry.get()))
    except:
        tkinter.messagebox.showinfo("Error", "Memory Error")
    clear()

def memory_subtract():
    global memory
    try:
        memory -= float(eval(entry.get()))
    except:
        tkinter.messagebox.showinfo("Error", "Memory Error")
    clear()

# Advanced math functions
def sqrt():
    try:
        value = math.sqrt(float(eval(entry.get())))
        clear()
        entry.insert(0, value)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input for Square Root")

def sin():
    try:
        value = math.sin(math.radians(float(eval(entry.get()))))
        clear()
        entry.insert(0, value)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input for Sin")

def cos():
    try:
        value = math.cos(math.radians(float(eval(entry.get()))))
        clear()
        entry.insert(0, value)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input for Cos")

def tan():
    try:
        value = math.tan(math.radians(float(eval(entry.get()))))
        clear()
        entry.insert(0, value)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input for Tan")

def log():
    try:
        value = math.log10(float(eval(entry.get())))
        clear()
        entry.insert(0, value)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input for Log")

def exp():
    try:
        value = math.exp(float(eval(entry.get())))
        clear()
        entry.insert(0, value)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input for Exponential")

# Dark theme styling
button_style = {
    'padx': 15, 'pady': 10, 'bg': 'gray', 'fg': 'white', 'activebackground': 'darkgray', 'activeforeground': 'black',
    'font': ('Arial', 12), 'width': 5
}

# Create buttons for numbers and basic operations
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('.', 4, 2), ('(', 4, 0), (')', 4, 4),
    ('sqrt', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3),
    ('log', 6, 0), ('exp', 6, 1), ('clear', 6, 2, 'clear'),
    ('=', 6, 3), ('M+', 7, 0), ('M-', 7, 1), ('MR', 7, 2), ('MC', 7, 3)
]

# Create button widgets and grid them
for (text, row, col, *opts) in buttons:
    action = clear if 'clear' in opts else equal if text == '=' else lambda t=text: myclick(t)
    button = tk.Button(master=window, text=text, command=action, **button_style)
    button.grid(row=row, column=col, pady=5)

# Advanced math function buttons
tk.Button(master=window, text="√", command=sqrt, **button_style).grid(row=5, column=0)
tk.Button(master=window, text="sin", command=sin, **button_style).grid(row=5, column=1)
tk.Button(master=window, text="cos", command=cos, **button_style).grid(row=5, column=2)
tk.Button(master=window, text="tan", command=tan, **button_style).grid(row=5, column=3)

tk.Button(master=window, text="log", command=log, **button_style).grid(row=6, column=0)
tk.Button(master=window, text="exp", command=exp, **button_style).grid(row=6, column=1)

# Memory buttons
tk.Button(master=window, text="M+", command=memory_add, **button_style).grid(row=7, column=0)
tk.Button(master=window, text="M-", command=memory_subtract, **button_style).grid(row=7, column=1)
tk.Button(master=window, text="MR", command=memory_recall, **button_style).grid(row=7, column=2)
tk.Button(master=window, text="MC", command=memory_clear, **button_style).grid(row=7, column=3)

# Start the tkinter loop
window.mainloop()
