import os

os.system('cls')
print("   _____                                          _   _      _               _____                           ")
print("  / ____|                                        | | | |    (_)             / ____|                          ")
print(" | |     ___  _ __ ___  _ __ ___   __ _ _ __   __| | | |     _ _ __   ___  | |  __  __ _ _ __ ___   ___  ___ ")
print(" | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` | | |    | | '_ \ / _ \ | | |_ |/ _` | '_ ` _ \ / _ \/ __|")
print(" | |___| (_) | | | | | | | | | | | (_| | | | | (_| | | |____| | | | |  __/ | |__| | (_| | | | | | |  __/\__ \ ")
print("  \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_| |______|_|_| |_|\___|  \_____|\__,_|_| |_| |_|\___||___/")
print("")
print("1. Random Number Guessing Game")
print("2. Harry Potter Duel Sim")
print("3. Math Game")
print("4. Rock/Paper/Scissors")
selection = input("What game would you like to play ")

if ((int(selection)) == 1):
    print("Luanching Game")
    os.system("python NumberGuessing.py")
elif ((int(selection)) == 2):
    print("Luanching Game")
    os.system("python HarryPotter.py")
elif ((int(selection)) == 3):
    print("Luanching Game")
    os.system("python Multiplication Game.py")
elif ((int(selection)) == 4):
    print("Luanching Game")
    os.system("python Rock,Paper,Scissors.py")
else:
    os.system('cls')
    print("      __ _ ")
    print("     / /| |")
    print("    / (_) |")
    print("   / /  | |")
    print("  / /  _| |")
    print(" /_/  (_) |")
    print("        | |")
    print("        |_|")
    print("That's Not A Valid Input")