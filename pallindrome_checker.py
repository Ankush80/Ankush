#Pallindrome Checker
def check(x):
    y = x[::-1]
    if y == x:
        print(f"{x} is a Pallindrome\n{x} == {y}")
    else:
        print(f"{x} isn't a Pallindrome\n{x} =/= {y}")
        
while True:
    a = input("Enter: ").upper()
    if a == 'EXIT':
        print("Visit Again")
        break
    else:
        check(a)