import random
import os

guesses = 3
number = 0
guess = 1
difficutiy = 0
win = 0

os.system('cls')
print("  _____                 _ _   _                 ")
print(" |  __ \               | | \ | |                ")
print(" | |__) |__ _ _ __   __| |  \| |_   _ _ __ ___  ")
print(" |  _  // _` | '_ \ / _` | . ` | | | | '_ ` _ \ ")
print(' | | \ \ (_| | | | | (_| | |\  | |_| | | | | | |')
print(" |_|  \_\__,_|_| |_|\__,_|_| \_|\__,_|_| |_| |_|")
print("")
print("1. Easy")
print('2. Medium')
print('3. Hard')
print('4. Imposible')
difficutiy = input("Please sellect your difficulty (1-4) ")

if (difficutiy == 1):
    number = random.randint(1,10)
    while guess < guesses:
        os.system('cls')
        print("Guess",guess,"/",guesses,)
        print("")
        guess = input("")