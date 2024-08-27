debugMode = 0

import random
import os

guesses = 3
number = 0
attempt = 1
difficulty = 0
win = 0
active = 1

os.system('cls')
print("  _____                 _ _   _                 ")
print(" |  __ \               | | \ | |                ")
print(" | |__) |__ _ _ __   __| |  \| |_   _ _ __ ___  ")
print(" |  _  // _` | '_ \ / _` | . ` | | | '_ ` _ \ ")
print(' | | \ \ (_| | | | | (_| | |\  | |_| | | | | |')
print(" |_|  \_\__,_|_| |_|\__,_|_| \_|\__,_|_| |_| |_|")
print("")
print("1. Easy")
print('2. Medium')
print('3. Hard')
print('4. Impossible')
difficulty = input("Please select your difficulty (1-4): ")

if int(difficulty) == 1:
    number = random.randint(1, 10)
    while int(active) == 1:
        os.system('cls')
        print("Easy Mode (1-10)")
        print("Attempt", attempt, "/", guesses)
        if ((int(debugMode)) == 1):
            print(number)
        print("")
        player_guess = input("Your Guess: ")
        
        if int(player_guess) == number:
            win = 1
            active = 0
            print(" __     __          __          ___       ")
            print(" \ \   / /          \ \        / (_)      ")
            print("  \ \_/ /__  _   _   \ \  /\  / / _ _ __  ")
            print("   \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
            print("    | | (_) | |_| |    \  /\  /  | | | | |")
            print("    |_|\___/ \__,_|     \/  \/   |_|_| |_|")
            print("")
            print("Your Guess is correct")
        else:
            print("Wrong. Try Again")
            attempt += 1
        
        if attempt > guesses:
            active = 0
            win = 0
            print("You lose! The number was", number)

elif int(difficulty) == 2:
    number = random.randint(1, 50)
    while int(active) == 1:
        os.system('cls')
        print("Medium Mode (1-50)")
        print("Attempt", attempt, "/", guesses)
        if ((int(debugMode)) == 1):
            print(number)
        print("")
        player_guess = input("Your Guess: ")
        
        if int(player_guess) == number:
            win = 1
            active = 0
            print(" __     __          __          ___       ")
            print(" \ \   / /          \ \        / (_)      ")
            print("  \ \_/ /__  _   _   \ \  /\  / / _ _ __  ")
            print("   \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
            print("    | | (_) | |_| |    \  /\  /  | | | | |")
            print("    |_|\___/ \__,_|     \/  \/   |_|_| |_|")
            print("")
            print("Your Guess is correct")
        else:
            print("Wrong. Try Again")
            attempt += 1
        
        if attempt > guesses:
            active = 0
            win = 0
            print("You lose! The number was", number)

elif int(difficulty) == 3:
    number = random.randint(1, 100)
    while int(active) == 1:
        os.system('cls')
        print("Hard Mode (1-100)")
        print("Attempt", attempt, "/", guesses)
        if ((int(debugMode)) == 1):
            print(number)
        print("")
        player_guess = input("Your Guess: ")
        
        if int(player_guess) == number:
            win = 1
            active = 0
            print(" __     __          __          ___       ")
            print(" \ \   / /          \ \        / (_)      ")
            print("  \ \_/ /__  _   _   \ \  /\  / / _ _ __  ")
            print("   \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
            print("    | | (_) | |_| |    \  /\  /  | | | | |")
            print("    |_|\___/ \__,_|     \/  \/   |_|_| |_|")
            print("")
            print("Your Guess is correct")
        else:
            print("Wrong. Try Again")
            attempt += 1
        
        if attempt > guesses:
            active = 0
            win = 0
            print("You lose! The number was", number)



null = input("Press Enter to exit")