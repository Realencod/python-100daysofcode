def pinPicker(number):
    import random

    pin=""
    for i in range(number):
        pin += str(random.randint(0, 5)) #one pin plus another repeated 'number' number of times as string values
    return pin

myNumber = pinPicker(5)
print(myNumber)   
