import random
chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
inp = str(input("Press 1 to generate Password:"))
if inp == "1" :
    password = ""
    for a in range(8):
        password += random.choice(chars)
    print(password)
else:
    print("Please press 1!")
