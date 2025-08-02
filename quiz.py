#Quiz
from tkinter import *
app = Tk()
app.title("Quiz")
app.columnconfigure(0, weight=1)
app.config(bg="white")

Label(app, text="Quiz", bg="white", font=("Arial", 15)).grid(row=0, column=0, pady=5)

Label(app, text="1. Where is the capital of India?", bg="white", font=("Arial", 11)).grid(row=1, column=0, pady=10, sticky="w")
ans1 = StringVar(value="none")
options1 = ["Kolkata", "New Delhi", "Mumbai", "Bengaluru"]
for i, option in enumerate(options1):
    Radiobutton(app, text=option, value=option, variable=ans1, width=10, bg="white", anchor="w").grid(row=2+i, column=0, pady=2, sticky="w")
    
Label(app, text="2. What's the height of Mt. Everest?", bg="white", font=("Arial", 11)).grid(row=6, column=0, pady=10, sticky="w")
ans2 = StringVar(value="none")
options2 = ["8,848 m", "8,876 m", "8,879 m", "8,878 m"]
for i, text in enumerate(options2):
    Radiobutton(app, text=text, value=text, variable=ans2, width=10, bg="white", anchor="w").grid(row=7+i, column=0, pady=2, sticky="w")
    
Label(app, text="3. Reason behind lightning in the Sky?", bg="white", font=("Arial", 11)).grid(row=11, sticky="w", column=0, pady=2)
ans3 = StringVar(value="none")
options3 = ["Sonic Boom", "Induction of Charges", "Aeroplanes", "Chloro Fluoro Carbons"]
for i, val in enumerate(options3):
    Radiobutton(app, text=val, value=val, variable=ans3, bg="white", anchor="w", width=20).grid(row=12+i, column=0, pady=2, sticky="w")
    
output = Label(app, text="", bg="white", fg="green", font=("Arial", 13), wrap=1000)
output.grid(row=16, column=0, pady=10)

def result():
    correct = 0
    wrong = []
    if ans1.get() == 'New Delhi': correct += 1
    else: wrong.append("New Delhi is the capital of India")
    if ans2.get() == '8,848 m': correct += 1
    else: wrong.append("8,848 is the height of Mt. Everest")
    if ans3.get() == 'Induction of Charges': correct += 1
    else: wrong.append("Lightning occurs due to the induction of charges")
    if correct != 3: output.config(text=f"Correct answers: {correct}/3\nWrong: {', '.join(wrong)}")
    else: output.config(text=f"Correct answers: {correct}/3")
    
def rst():
    ans1.set("none")
    ans2.set("none")
    ans3.set("none")
    output.config(text="")
    
Button(app, text="Submit", bg="black", fg="white", width=10, command=result).grid(row=17, column=0, pady=5)
Button(app, text="Reset", bg="green", fg="black", width=10, command=rst).grid(row=18, column=0, pady=5)
app.mainloop()