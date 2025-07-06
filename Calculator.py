while True:
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    user_input = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Cube\n7. Square Root\n8. Cube Root\n9. Table\n10. Exit\nEnter your preference in integer: "))
    if user_input == 1:
        print(f"{a} + {b} = {a+b}")
    elif user_input == 2:
        print(f"{a} - {b} = {a-b}")
    elif user_input == 3:
        print(f"{a} x {b} = {a*b}")
    elif user_input == 4:
        try:
            print(f"{a}/{b} = {a/b}")
        except ZeroDivisionError:
            print("Not Defined")
    elif user_input == 5:
        print(f"Square of {a}: {a**2}\nSquare of {b}: {b**2}")
    elif user_input == 6:
        print(f"Cube of {a}: {a**3}\nCube of {b}: {b**3}")
    elif user_input == 7:
        print(f"Square root of {a}: {a**(1/2)}\nSquare root of {b}: {b**(1/2)}")
    elif user_input == 8:
        print(f"Cube root of {a}: {a**(1/3)}\nCube root of {b}: {b**(1/3)}")
    elif user_input == 9:
        print(f"Table of {a}:")
        for i in range(1, 11):
            print(f"{int(a)} x {i} = {int(a)*i}")
        print(f"Table of {b}:")
        for p in range(1, 11):
            print(f"{int(b)} x {p} = {int(b)*p}")
    elif user_input == 10:
         print("Visit Again")
        break
    else:
        print("Invalid User Input")