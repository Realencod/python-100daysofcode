import random 
print("\033[34m", """INFINITY DICE""", "\033[0m")
def rolldice(dice):
    if dice < 6:
        print("Now that's creative")
    elif dice == 6:
        print("Utterly unambicious...try another pick next time")
    elif dice > 6 and dice <= 20:
        print("Not gonna lie...I was expecting more from you😒")        
    elif dice > 20 and dice <= 100:
        print("Barely passable but whatever")
    elif dice > 100 and dice <= 1000:
        print("Great! Someone who is close to understanding the essense of infinity")
    elif dice > 1000:
        print("Finally! Someone that's as crazy as I am😂...have fun yo")

while True:
    dice = int(input("Type the number of the sides you want your dice to have>>"))
    rolldice(dice)
    rolled = random.randint(1, dice)
    print("You rolled", rolled)

    go_on = input("Continue?>>").lower()
    if go_on != "yes":
        print()
        exit(("Alright, byee!"))
    else:
        continue

"""
alternatively...print("You rolled", random.randint(1,dice))
"""    


