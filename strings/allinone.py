#basic string
name = "My name is Frank!"
print(name)

#all letters in strings, numbers, symbols and spaces all occupy a position in the said string....count starts from zero
print()
print("number 4 position in the string belongs to the letter",name[4])

#Checking the string length
print("The string length is",len(name))

#looping through a string
for i in "Frank":
    print(i)

#how to check if a certain letter is in the said string
print()
print("Frank" in name)
#or...
if "Frank" in name:
    print("His name is Frank")

#a word is not in the string
if "Allan" not in name:
    print("His name is not Allan")

