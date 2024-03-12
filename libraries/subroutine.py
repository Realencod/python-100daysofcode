def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

number = int(input("How many times do you want to roll the dice?>>"))
for i in range(number):
  rollDice()
