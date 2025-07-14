from tkinter import *

window = Tk()
window.title("App")
window.config(bg="black")
window.geometry("300x200")
window.columnconfigure(0, weight =1)

Label(window, text="Calculator", font=("Arial", 15), bg="black", fg="lightblue").grid(row=0, column=0, pady=5)

Label(window, text="Enter the first number:", font=("Arial", 12), bg="black", fg="white").grid(row=1, column=0, pady=5, sticky="w")
a = Entry(window, width=10)
a.grid(row=1, column=0, pady=5, sticky="e", padx=70)

Label(window, text="Enter second number:", bg="black", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="w")
b = Entry(window, width=10)
b.grid(row=2, column=0,  pady=5, sticky="e", padx=70)

operation = StringVar(value="Summation")
Radiobutton(window, text="Summation", variable=operation, value="Summation", width=15, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Subtraction", variable=operation, value="Subtraction", width=15, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Multiplication", variable=operation, value="Multiplication", width=15, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Division", variable=operation, value="Division", width=15, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)

output = Label(window, text="", bg="black", fg="green", wrap=1000, font=("Arial", 12))
output.grid(pady=5, column=0)

def calculation_one():
    p = a.get()
    q = b.get()
    selected = operation.get()
    try:
        if selected == 'Summation': output.config(text=f"{p} + {q} = {float(p)+float(q)}")
        elif selected == 'Subtraction': output.config(text=f"{p} - {q} = {float(p)-float(q)}")
        elif selected == 'Multiplication': output.config(text=f"{p} x {q} = {float(p)*float(q)}")
        elif selected == 'Division':
            try: output.config(text=f"{p} / {q} = {float(p)/float(q)}")
            except ZeroDivisionError: output.config(text="Denominator can't be zero")
    except ValueError: output.config(text="Invalid Input")

Button(window, text="Calculate", width=10, bg="lightblue", fg="black", command=calculation_one).grid(column=0, pady=5)

Label(window, text="Or Use just a single digit", bg="black", fg="aqua", font=("Arial", 8)).grid(column=0, pady=5)

Label(window, text="Enter the digit:", bg="black", fg="white", font=("Arial", 12)).grid(row=10,column=0, pady=5, sticky="w", padx=10)

c = Entry(window, width=10)
c.grid(row=10, column=0, pady=5, sticky="e", padx=300)

operation_s = StringVar(value="Square Root")
Radiobutton(window, text="Square Root", variable=operation_s, value="Square Root", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Cube Root", variable=operation_s, value="Cube Root", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Square", variable=operation_s, value="Square", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Cube", variable=operation_s, value="Cube", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Logarithm", variable=operation_s, value="Logarithm", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Sin", variable=operation_s, value="Sin", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Cos", variable=operation_s, value="Cos", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Tan", variable=operation_s, value="Tan", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Cosec", variable=operation_s, value="Cosec", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Sec", variable=operation_s, value="Sec", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)
Radiobutton(window, text="Cot", variable=operation_s, value="Cot", width=10, bg="lightyellow", fg="black", font=("Arial", 10), anchor="w").grid(column=0, pady=5)

    
def calculation_two():
    r = c.get()
    selection = operation_s.get()
    try:
        if selection == 'Square Root': output_s.config(text=f"Square Root of {r}: {float(r)**0.5}")
        elif selection == 'Cube Root': output_s.config(text=f"Cube Root of {r}: {float(r)**(1/3)}")
        elif selection == 'Square': output_s.config(text=f"Square of {r}: {float(r)**(2)}")
        elif selection == 'Cube': output_s.config(text=f"Cube of {r}: {float(r)**(3)}")
        elif selection == 'Logarithm':
            from math import log
            output_s.config(text=f"Logarithm of {r}: {log(float(r))}")
        elif selection == 'Sin':
            from math import sin
            output_s.config(text=f"Sin of {r}: {sin(float(r))}")
        elif selection == 'Cos':
            from math import cos
            output_s.config(text=f"Cos of {r}: {cos(float(r))}")
        elif selection == 'Tan':
            from math import tan
            output_s.config(text=f"Tan of {r}: {tan(float(r))}")
        elif selection == 'Cosec':
            from math import sinh
            output_s.config(text=f"Cosec of {r}: {sinh(float(r))}")
        elif selection == 'Cot':
            from math import tanh
            output_s.config(text=f"Cot of {r}: {tanh(float(r))}")
        elif selection == 'Sec':
            from math import cosh
            output_s.config(text=f"Sec of {r}: {cosh(float(r))}")
    except ValueError: output_s.config(text="Invalid Input")

output_s = Label(window, text="", bg="black", fg="lightgreen", font=("Arial", 12), wrap=1000)
output_s.grid(column=0, pady=5)

Button(window, text="Calculate", width=10, bg="lightblue", fg="black", command=calculation_two).grid(column=0, pady=5)

window.mainloop()