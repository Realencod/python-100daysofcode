import random
while True:
    number = random.randint(1, 1000)
    if number < 900:
       print(number)
    elif number >= 900:
        exit(("You've come to the end of your code"))
