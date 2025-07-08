
#Chatbot

name = input("Enter your name: ")
while True:
    a = input("🙂: ")
    if a.lower() == "hello":
        print(f"🤖Hey {name}, How may i help you?")
        
    elif a.lower() == "i wanna ask you some questions":
        print("🤖: Ask without any hesitation")
        
    elif a.lower() == "what's the table of 35?":
        print("🤖: The table of 35 is super easy\n")
        for i in range(1, 11):
            print(f"35 x {i} = {35*i}")
            
    elif a.lower() == "okay bye, my doubts are cleared":
        print("🤖: Bye")
        break