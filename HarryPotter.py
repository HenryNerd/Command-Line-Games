import random
import os

playerName = "Unknown"
playerHealth = 5
oponentHealth = 5
active = 1
win = 0
round = 1
os.system('cls')
print("  _____        _         _____ _           ")
print(" |  __ \      | |       / ____(_)          ")
print(" | |  | |_   _| | ___  | (___  _ _ __ ___  ")
print(" | |  | | | | | |/ _ \  \___ \| | '_ ` _ \ ")
print(" | |__| | |_| | |  __/  ____) | | | | | | |")
print(" |_____/ \__,_|_|\___| |_____/|_|_| |_| |_|")

print("Harry Potter Duel Game")
print("Made by @HenryNerd on github")
print("")
print("")
playerName = input("Hi, What's your name ")
print("Hi,",playerName)
partner = random.randint(1,3)

if (partner == 1):
    print("Your Oponent is Draco Malfoy")
    Oponent = "Draco Malfoy"
elif (partner == 2):
    print("Your Oponent is Harry Potter")
    Oponent = "Harry Potter"
elif (partner == 3):
    print("Your Oponent is Severus Snape")
    Oponent = "Severus Snape"

null = input("Press Enter to contuinue")
os.system('cls')

while active == 1:
    print("Round:",round,"Health",playerHealth)
    print("It is your turn")
    print("1. Atack")
    print("2. Heal")
    print("3. Dodge")
    currentAction = input("What would you like to do (1-3) ")
    if ((int(currentAction)) == 1):
        print("")
        atackDamage = random.randint(1,2)
        print("You atacked",Oponent,"for",atackDamage)
        print("Checking for hit")
        hit = random.randint(1,100)
        if (hit == 100):
            print("Your atack did not hit")
            print("Your atack did 0 Damage")
        else:
            print("Your atack hit")
            print("Your atack did",atackDamage,"Damage")
            oponentHealth = oponentHealth - atackDamage
    elif ((int(currentAction)) == 2):
        if (playerHealth == 5):
            print("You are at full health")
        else:
            print("You healed")
            playerHealth = playerHealth + 1
            print("Your Health is now",playerHealth)
    elif ((int(currentAction)) == 3):
        print("You have dodged")
        print("You will take no damage this round")
    
    null = input("Press Enter to contuinue")
    os.system('cls')
    if ((int(oponentHealth)) > 0):
        print("Round:",round,"Oponent's Health",oponentHealth)
        print("It is",Oponent,"'s turn")
    
        if (currentAction == 3):
            print("You chose to dodge. You don't take any damage")
        else:
            print(Oponent,"Has chosen to atack. Rolling atack")
            hit = random.randint(1,50)
            if (hit == 50):
                print("Atack Missed")
            else:
                print("Atack hit")
                playerHealth = playerHealth - 1
                print("You take 1 damage")
                print ("You are now at",playerHealth)

    round = round + 1
    if (playerHealth == 0):
        active = 0
        win = 0
    elif (oponentHealth == 0):
        active = 0
        win = 1
    os.system('cls')

if ((int(win)) == 1):
    print(" __     __          __          ___       ")
    print(" \ \   / /          \ \        / (_)      ")
    print("  \ \_/ /__  _   _   \ \  /\  / / _ _ __  ")
    print("   \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
    print("    | | (_) | |_| |    \  /\  /  | | | | |")
    print("    |_|\___/ \__,_|     \/  \/   |_|_| |_|")
    print("")
elif ((int(win)) == 1):
    print("     __")
    print("  _ / /")
    print(" (_) | ")
    print("   | | ")
    print("  _| | ")
    print(" (_) |")
    print("    \_\ ")
    print("       ")
    print("")
    print("You lost")

null = input("Press Enter to Exit")
os.system("python main.py")