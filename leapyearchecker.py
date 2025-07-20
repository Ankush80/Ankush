#Leap year checker
from tkinter import *
app = Tk()
app.title("Leap year checker")
app.config(bg="white")
app.columnconfigure(0, weight=1)

Label(app, text="Leap Year Checker", bg="white", fg="black", font=("Arial", 15)).grid(row=0, column=0, pady=5)
Label(app, text="Enter the Year: ", bg="white", fg="black", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky='w')
a = Entry(app, width=6)
a.grid(row=1, column=0, sticky='n', pady=25)
output = Label(app, text="", bg="white", fg="green", font=("Arial", 13))
output.grid(row=2, column=0, pady=10, sticky='w')

def leap():
    b = a.get()
    if b.isdigit():
        x = int(b)
        if (x%4==0 and x%100!=0) or x%400==0:
            output.config(text=f"{x} is a leap year")
        else:
            output.config(text=f"{x} is not a leap year")
    else:
        output.config(text="Invalid Input")

Button(app, text="Check", bg="black", fg="white", command=leap, width=7).grid(row=3, column=0, pady=10)

app.mainloop()