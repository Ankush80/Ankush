import random
a = int(input("Enter the max number: "))
b = random.randint(1, a)
count = 0
while True:
    c = int(input("Guess: "))
    if c > b:
        print("Think Low")
        count += 1
    elif c < b:
        print("Think High")
        count += 1
    else:
        print(f"Congrats, you completed this game in {count} attempts.")
        break