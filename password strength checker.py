#Password strength checker
import string
def strength(pwd):
    total = 0
    if len(pwd) > 7:
        total += 1
    if any(a.islower() for a in pwd):
        total += 1
    if any(a.isdigit() for a in pwd):
        total += 1
    if any(a.isupper() for a in pwd):
        total += 1
    if any(a in string.punctuation for a in pwd):
        total += 1
        
    if total <= 2:
        return "Weak"
    elif 2 < total < 5:
        return "Medium"
    else:
        return "Strong"
        
while True:
    password = input("Enter your password: ")
    if password == 'exit':
        break
    else:
        print("Password Strength:", strength(password))