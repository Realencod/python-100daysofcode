def healthbar(number):
    import random
    number = (random.randint(1, 6)) * (random.randint(1, 8))
    return number

for i in range(1,3+1):
       print(i)
       name = input("What is the name of your character?>>") 
       print(name, "'s healthbar is", "\033[31m", healthbar(""), "hp", "\033[0m")
print("Congratulations on creating a complete party!".upper())

