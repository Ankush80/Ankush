#Temperature Converter
def temp(x):
    print(f"Celcius: {x-273.15}")
    print(f"Fahrenheit: {(((x-273.15)/5)*9)+32}")
    print(f"Rankine: {(9*x)/5}")
while True:
    a = input("Enter Kelvin Temperature: ")
    if a.lower()=='exit':
        break
    elif not a.replace('.', '', 1).isdigit():
        print("Invalid Input")
    else:
        temp(float(a))