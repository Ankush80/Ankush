#bank account
def bank():
    try:
        with open("account.txt", "r") as file:
            history = file.readlines()
            if history:
                for file in history:
                    print(file.strip())
            else:
                print("Transaction file is empty")
    except FileNotFoundError:
        print("Account doesn't exist")
        
name = input("Enter your name: ")
password = ''
while password != 'open':
    password = input("Password: ")
while True:
    from datetime import datetime
    time = datetime.now().strftime("%d|%m|%Y %H:%M:%S")
    a = input("\n1. Transaction history\n2. Deposit\n3. Withdraw\n4. Exit\n\nEnter your preference in integer: ")
    if a == '1':
        bank()
    elif a == '2':
        deposit = float(input("Deposit: "))
        if deposit > 0:
            print("Deposited sucessfully")
            with open("account.txt", "a") as file:
                file.write(f"Deposit: {deposit}  [{time}]\n")
        else:
            print("Invalid amount")
    elif a == '3':
        withdraw = float(input("Withdraw: "))
        if withdraw > 0:
            print("Withdrawn sucessfully")
            with open("account.txt", "a") as file:
                file.write(f"Withdraw: {withdraw} [{time}]\n")
        else:
            print("Invalid Amount")
    elif a == '4':
        print("Visit Again")
        break
    else:
        print("Enter a valid integer")