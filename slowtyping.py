from time import sleep

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line

print_slow("Hello. I'm feeling a bit slow today")
print()
print_slow("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
ans1 = input("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = int(input("Which lesson number is this?"))
if (ans2 > 12):
  print("We're not quite that far yet")
elif ans2 == 12: 
  print("That's right!")
else:
  print("We've gone well past that!")
