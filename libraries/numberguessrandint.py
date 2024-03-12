import random
count = 1
print("I'm thinking of a number", "\033[34m", "between 1 and 1000",  "\033[0m", "...I would like you to guess the number😛")
while True:
  number = random.randint(1,1000 + 1)
  print()
  guess = int(input("What's your guess?>>"))
  if guess == number:
    break
  elif guess != number and guess < 1000:
    count += 1
    number += 14
    if count >= 1:
      print("Nope, try again!")
    if number > 1000:
      exit()
    diff = abs(number - guess)
    if diff <=10:
      print("You are this close to scoring it right🤏")
    elif diff > 10 and diff <= 30:
      print("You are somehow close to the answer")
    elif diff > 30 and diff <= 70:
      print("Yikes, you are far off from home!")
    elif diff > 70 and diff <= 200:
      print("You are a lost cause...please consider dropping this game")
      input("Exit?>>").lower()
      if exit != "yes":
        continue
      else:
        print("Thanks for playing!")
        exit((print("Gutless!")))
    elif diff > 200:
      print("You💀.....please leave....your luck is not good enough")
      input("Exit?>>").lower()
      if exit != "yes":
        continue
      else:
        print("Thanks for playing!")
        exit((print("Gutless!")))

  elif guess > 1000:
    print("Sucks to be you!😂")
    exit((print("Them instructions were clear mate!")))
    
  else:
    print("Seriously...you do know that you can't guess a number less than 1 or type in words right?")

print()
print("Woah you are good at this!😎...or is it because you had a sneak preview on the code😅")
print("Thanks for playing this game!...whoever you are, I hope you enjoyed it😉")
    