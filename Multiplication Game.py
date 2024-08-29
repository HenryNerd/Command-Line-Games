import os
import random

gamemode = 0
turn = 1
num1 = 0
num2 = 0
correctAnswer = 0
userAnswer = 0
score = 0

os.system('cls')
print("  __  __       _ _   _       _ _           _   _                _____                      ")
print(" |  \/  |     | | | (_)     | (_)         | | (_)              / ____|                     ")
print(" | \  / |_   _| | |_ _ _ __ | |_  ___ __ _| |_ _  ___  _ __   | |  __  __ _ _ __ ___   ___ ")
print(" | |\/| | | | | | __| | '_ \| | |/ __/ _` | __| |/ _ \| '_ \  | | |_ |/ _` | '_ ` _ \ / _ \ ")
print(" | |  | | |_| | | |_| | |_) | | | (_| (_| | |_| | (_) | | | | | |__| | (_| | | | | | |  __/")
print(" |_|  |_|\__,_|_|\__|_| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|  \_____|\__,_|_| |_| |_|\___|")
print("                      | |                                                                  ")
print("                      |_|                                                                  ")
print("")
print("1. 1 Digit")
print("2. 2 Digits")
print("3. 3 Digits")
print("4. 4 Digits")
gamemode = input("What Gamemode would you like to play ")

if int(gamemode) == 1:
    os.system('cls')
    while int(turn) != 10:
        os.system('cls')
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        answer = num1 * num2
        print("Round:",turn,"Mode: Easy")
        print("Equation: ",num1," X ",num2)
        print("")
        userAnswer = input("What is the awnser")
        turn = turn + 1
        if int(userAnswer) == int(correctAnswer):
            score = score + 1
elif int(gamemode) == 2:
    os.system('cls')
    while int(turn) != 10:
        os.system('cls')
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
elif int(gamemode) == 3:
    os.system('cls')
    while int(turn) != 10:
        num1 = random.randint(0,999)
        num2 = random.randint(0,999)
elif int(gamemode) == 4:
    os.system('cls')
    while int(turn) != 10:
        num1 = random.randint(0,9999)
        num2 = random.randint(0,9999)