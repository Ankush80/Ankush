import tkinter as tk
import random

app = tk.Tk()
app.title("Motivational quote")
app.config(bg="black")

quotes = ["Believe in yourself and all that you are.", "Push yourself, because no one else is going to do it for you.", "Success is not for the lazy.", "Every day is a second chance.", "Discipline is stronger than motivation.", "Dream big. Start small. Act now.", "You’re capable of more than you know.", "Don’t wish for it. Work for it.", "Stay consistent, not perfect.", "Your future is created by what you do today.", "Doubt kills more dreams than failure ever will.", "It's not about being the best. It's about being better than you were yesterday.", "Hard work beats talent when talent doesn’t work hard.", "Wake up with determination, go to bed with satisfaction.", "Make it happen. Shock everyone.", "If you’re tired, learn to rest, not quit.", "Fall seven times, stand up eight.", "Progress, not perfection.",  "Winners are not afraid of losing. Losers are.", "You don't have to be extreme, just consistent.", "Small steps every day lead to big results.", "When you feel like quitting, remember why you started.", "Success is built on discipline and pain tolerance.", "You won’t always be motivated, so be disciplined.", "Success starts with self-belief.", "You become what you consistently do.", "Start where you are. Use what you have. Do what you can.", "Energy grows where focus goes.", "If it matters to you, you’ll find a way.", "One day or day one — you decide."]

def quote():
    output.config(text=random.choice(quotes))
    
tk.Button(app, text="Motivate Me", bg="green", fg="black", width=15, bd=1, relief="solid", command=quote).pack(pady=20)

output = tk.Label(app, text="", bg="black", fg="lightblue", font=("Arial", 12), wrap=1000)
output.pack(pady=20)

app.mainloop()