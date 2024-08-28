import os
import random
gamemode = 0
result = 0

os.system('cls')
print("  _____            _         _______                        _______      _                        ")
print(" |  __ \          | |       / /  __ \                      / / ____|    (_)                       ")
print(" | |__) |___   ___| | __   / /| |__) |_ _ _ __   ___ _ __ / / (___   ___ _ ___ ___  ___  _ __ ___ ")
print(" |  _  // _ \ / __| |/ /  / / |  ___/ _` | '_ \ / _ \ '__/ / \___ \ / __| / __/ __|/ _ \| '__/ __|")
print(" | | \ \ (_) | (__|   <  / /  | |  | (_| | |_) |  __/ | / /  ____) | (__| \__ \__ \ (_) | |  \__ \ ")
print(" |_|  \_\___/ \___|_|\_\/_/   |_|   \__,_| .__/ \___|_|/_/  |_____/ \___|_|___/___/\___/|_|  |___/")
print("                                         | |                                                      ")
print("                                         |_|                                                      ")
print("")
print("1. Player vs PC")
print("2. Player vs Player")
gamemode = input("What gamemode would you like to play ")

if int(gamemode) == 1:
    os.system('cls')
    print("Player vs PC")
    print("")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player1Choice = input("Whitch would you like to choose ")
    player2Choice = random.randint(1,3)
    
    if int(player1Choice) == 1:
        if int(player2Choice) == 1:
            result = 2
        elif int(player2Choice) == 2:
            result = 1
        elif int(player2Choice) == 2:
            result = 3

    elif int(player1Choice) == 2:
        if int(player2Choice) == 1:
            result = 3
        elif int(player2Choice) == 2:
            result = 2
        elif int(player2Choice) == 2:
            result = 1

    elif int(player1Choice) == 3:
        if int(player2Choice) == 1:
            result = 1
        elif int(player2Choice) == 2:
            result = 3
        elif int(player2Choice) == 2:
            result = 2

    if int(player2Choice) == 1:
        print("Your PC chose Rock")
    elif int(player2Choice) == 2:
        print("Your PC chose Paper")
    elif int(player2Choice) == 2:
        print("Your PC chose Scissors")

if int(result) == 1:
    print("Lose")
elif int(result) == 2:
    print("Tie")
elif int(result) == 3:
    print("Win")