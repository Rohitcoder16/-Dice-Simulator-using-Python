import random

print("Wellcome  to the Dice Game")

choice=input("Do you want to play the game? (yes/no)")
while choice == "yes":
    num = random.randint(1,6)
    if num==1:
        print("-----------")
        print("     0     ")
        print("           ")
        print("-----------")
    elif num==2:
        print("-----------")
        print("     0     ")
        print("     0     ")
        print("-----------")        
    elif num==3:
        print("-----------")
        print("     0     ")
        print("     0     ")
        print("     0     ")
        print("-----------")
    elif num==4:
        print("-----------")
        print("     0     ")
        print("  0     0  ")
        print("     0     ")
        print("-----------")
    elif num==5:
        print("-----------")
        print("     0     ")
        print("  0     0  ")
        print("     0     ")
        print("  0     0  ")
        print("-----------")
    else:
        print("-----------")
        print("  0     0  ")
        print("  0     0  ")
        print("  0     0  ")
        print("-----------")
    choice=input("Do you want to play the game? (yes/no)")
    if choice == "no":
        print("Thanks for playing the game")
