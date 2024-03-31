def picker(number):

    import random
    pin=""
    for i in range(number):
        pin += str(random.randint(2, 9))
    return pin

pin1 = int(input("pick the number of digits for your randomised number>>"))
no = picker(pin1)
print(no)



