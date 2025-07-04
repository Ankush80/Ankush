#Even or Odd Finder
def check(x):
    if x % 2 == 0:
        return f"{x} is an Even Number!"
    else:
        return f"{x} is an Odd Number!"
        
while True:
    a = input("Check the Number: ")
    if a.lower() == "exit":
        break
    try:
        print(check(int(a)))
    except ValueError:
        print("Please Enter a Valid Integer")