from tkinter import *
import random

app = Tk()
app.title("Lucky Number")
app.columnconfigure(0, weight=1)
app.config(bg="white")

Label(app, text="Lucky Number", bg="white", font=("Arial", 15)).grid(row=0, column=0, pady=5)

output = Label(app, text="", bg="white", fg="green", font=("Arial", 70))
output.grid(row=2, column=0, pady=10)

def luck():
    output.config(text=random.randint(1, 101))
    button.config(state=DISABLED)
    
button = Button(app, text="Try Your Luck", bg="black", fg="white", font=("Courier", 13), command=luck)
button.grid(row=1, column=0, pady=10)
app.mainloop()