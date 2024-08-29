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

    os.system('cls')
    if int(player2Choice) == 1:
        print("Your PC chose Rock")
    elif int(player2Choice) == 2:
        print("Your PC chose Paper")
    elif int(player2Choice) == 2:
        print("Your PC chose Scissors")

    if int(result) == 1:
        print("     __")
        print("  _ / /")
        print(" (_) | ")
        print("   | | ")
        print("  _| | ")
        print(" (_) | ")
        print("    \_\ ")
        print("")
        print("Sorry, You Lost")
    elif int(result) == 2:
        print("  ______ ")
        print(" |______|")
        print("  ______ ")
        print(" |______|")
        print("")
        print("That was a tie")
    elif int(result) == 3:
        print(" __     __          __          ___       ")
        print(" \ \   / /          \ \        / (_)      ")
        print("  \ \_/ /__  _   _   \ \  /\  / / _ _ __  ")
        print("   \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
        print("    | | (_) | |_| |    \  /\  /  | | | | |")
        print("    |_|\___/ \__,_|     \/  \/   |_|_| |_|")
    
elif int(gamemode) == 2:
    os.system('cls')
    print("Player VS Player")
    print("Player 1")
    print("")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player1Choice = input("What would you like to chose ")
    os.system('cls')
    print("Player VS Player")
    print("Player 2")
    print("")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player2Choice = input("What would you like to chose ")

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
    os.system('cls')
    if int(player1Choice) == 1:
        print("Player 1 Chose: Rock") 
    elif int(player1Choice) == 2:
        print("Player 1 Chose: Paper")
    elif int(player1Choice) == 3:
        print("Player 1 Chose: Scissors") 
    
    if int(player2Choice) == 1:
        print("Player 2 Chose: Rock") 
    elif int(player2Choice) == 2:
        print("Player 2 Chose: Paper")
    elif int(player2Choice) == 3:
        print("Player 2 Chose: Scissors")
    
    if int(result) == 2:
        print("")
        print("  _____  _                         __  __          ___           ")
        print(" |  __ \| |                       /_ | \ \        / (_)          ")
        print(" | |__) | | __ _ _   _  ___ _ __   | |  \ \  /\  / / _ _ __  ___ ")
        print(" |  ___/| |/ _` | | | |/ _ \ '__|  | |   \ \/  \/ / | | '_ \/ __|")
        print(" | |    | | (_| | |_| |  __/ |     | |    \  /\  /  | | | | \__ \ ")
        print(" |_|    |_|\__,_|\__, |\___|_|     |_|     \/  \/   |_|_| |_|___/")
        print("                  __/ |                                          ")
        print("                 |___/                                           ")
    elif int(result) == 2:
        print("  ______ ")
        print(" |______|")
        print("  ______ ")
        print(" |______|")
        print("")
        print("That was a tie")
    elif int(result) == 1:
        print("  _____  _                         ___   __          ___           ")
        print(" |  __ \| |                       |__ \  \ \        / (_)          ")
        print(" | |__) | | __ _ _   _  ___ _ __     ) |  \ \  /\  / / _ _ __  ___ ")
        print(" |  ___/| |/ _` | | | |/ _ \ '__|   / /    \ \/  \/ / | | '_ \/ __|")
        print(" | |    | | (_| | |_| |  __/ |     / /_     \  /\  /  | | | | \__ \ ")
        print(" |_|    |_|\__,_|\__, |\___|_|    |____|     \/  \/   |_|_| |_|___/")
        print("                  __/ |                                            ")
        print("                 |___/                                             ")

null = input("Press enter to exit")