import os
import random

mathMode = 0
gamemode = 0
turn = 1
num1 = 0
num2 = 0
correctAnswer = 0
userAnswer = 0
score = 0
grade = 0

os.system('cls')
print("1. Addition")
print("2. Multiplication")
mathMode = input("What Operation Would you like to practice")
if int(mathMode) == 1:
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
            correctAnswer = num1 * num2
            print("Round:",turn,"Mode: Easy")
            print("Equation: ",num1," X ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
            null = input("Press enter to continue ")
    elif int(gamemode) == 2:
        os.system('cls')
        while int(turn) != 10:
            os.system('cls')
            num1 = random.randint(0,99)
            num2 = random.randint(0,99)
            correctAnswer = num1 * num2
            print("Round:",turn,"Mode: Medium")
            print("Equation: ",num1," X ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
            null = input("Press enter to continue ")
    elif int(gamemode) == 3:
        os.system('cls')
        while int(turn) != 10:
            num1 = random.randint(0,999)
            num2 = random.randint(0,999)
            correctAnswer = num1 * num2
            print("Round:",turn,"Mode: Hard")
            print("Equation: ",num1," X ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
            null = input("Press enter to continue ")
    elif int(gamemode) == 4:
        os.system('cls')
        while int(turn) != 10:
            num1 = random.randint(0,9999)
            num2 = random.randint(0,9999)
            correctAnswer = num1 * num2
            print("Round:",turn,"Mode: Very Hard")
            print("Equation: ",num1," X ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
            null = input("Press enter to continue ")

    if int(score) == 10:
        grade = "S"
    elif int(score) == 9:
        grade = "A"
    elif int(score) == 8:
        grade = "A"
    elif int(score) == 7:
        grade = "B"
    elif int(score) == 6:
        grade = "B"
    elif int(score) == 5:
        grade = "C"
    elif int(score) == 4:
        grade = "C"
    elif int(score) == 3:
        grade = "D"
    elif int(score) == 2:
        grade = "D"
    elif int(score) == 1:
        grade = "F"
if int(mathMode) == 2:
    print("              _     _ _ _   _                _____                      ")
    print("     /\      | |   | (_) | (_)              / ____|                     ")
    print("    /  \   __| | __| |_| |_ _  ___  _ __   | |  __  __ _ _ __ ___   ___ ")
    print("   / /\ \ / _` |/ _` | | __| |/ _ \| '_ \  | | |_ |/ _` | '_ ` _ \ / _ \ ")
    print("  / ____ \ (_| | (_| | | |_| | (_) | | | | | |__| | (_| | | | | | |  __/")
    print(" /_/    \_\__,_|\__,_|_|\__|_|\___/|_| |_|  \_____|\__,_|_| |_| |_|\___|")
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
            correctAnswer = num1 + num2
            print("Round:",turn,"Mode: Easy")
            print("Equation: ",num1," + ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
        null = input("Press enter to continue ")
    elif int(gamemode) == 2:
        os.system('cls')
        while int(turn) != 10:
            os.system('cls')
            num1 = random.randint(0,99)
            num2 = random.randint(0,99)
            correctAnswer = num1 + num2
            print("Round:",turn,"Mode: Medium")
            print("Equation: ",num1," + ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
        null = input("Press enter to continue ")
    elif int(gamemode) == 3:
        os.system('cls')
        while int(turn) != 10:
            os.system('cls')
            num1 = random.randint(0,999)
            num2 = random.randint(0,999)
            correctAnswer = num1 + num2
            print("Round:",turn,"Mode: Hard")
            print("Equation: ",num1," + ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
        null = input("Press enter to continue ")
    elif int(gamemode) == 4:
        os.system('cls')
        while int(turn) != 10:
            os.system('cls')
            num1 = random.randint(0,9999)
            num2 = random.randint(0,9999)
            correctAnswer = num1 + num2
            print("Round:",turn,"Mode: Very Hard")
            print("Equation: ",num1," + ",num2)
            print("")
            userAnswer = input("What is the Answer ")
            turn = turn + 1
            if int(userAnswer) == int(correctAnswer):
                score = score + 1
                print("Answer is correct")
            else:
                print("Answer is incorrect")
        null = input("Press enter to continue ")


if grade == "S":
    os.system('cls')
    print("   _____ ")
    print("  / ____|")
    print(" | (___  ")
    print("  \___ \ ")
    print("  ____) |")
    print(" |_____/ ")
elif grade == "A":
    os.system('cls')
    print("     /\    ")
    print("    /  \   ")
    print("   / /\ \  ")
    print("  / ____ \ ")
    print(" /_/    \_\ ")
elif grade == "B":
    os.system('cls')
    print("  ____  ")
    print(" |  _ \ ")
    print(" | |_) |")
    print(" |  _ < ")
    print(" | |_) |")
    print(" |____/ ")
elif grade == "C":
    os.system('cls')
    print("   _____ ")
    print("  / ____|")
    print(" | |     ")
    print(" | |     ")
    print(" | |____ ")
    print("  \_____|")
elif grade == "D":
    os.system('cls')
    print("  _____  ")
    print(" |  __ \ ")
    print(" | |  | |")
    print(" | |  | |")
    print(" | |__| |")
    print(" |_____/ ")
elif grade == "F":
    os.system('cls')
    print("  ______ ")
    print(" |  ____|")
    print(" | |__   ")
    print(" |  __|  ")
    print(" | |    ")
    print(" |_|     ")