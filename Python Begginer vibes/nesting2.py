print("=====TRUE FAN SEEKER=====")
print()
anime = input("What's your favourite anime?")
if anime == "one piece":
  print("Oh really?")
  print("Prove it!")
  character = input("Name your favourite character") 
  """
  Don't mind me
         just trying to write multiline comments
         """
         #multiline comments don't work in python 
  if character == "luffy":
    print("You got that by pure chance!")
    job = input("What's his role on the ship?")
    if job == "captain":
      print("Hmph!Lucky guess!")
      form = input("What's his strongest gear?")
      if form == "gear 5":
        print("You're a truly a fan!")
      else:
        print("See!" ,"\033[31m", "FAKE" ,"\033[0m", "one piece fan!")
    else:
      print("See!" ,"\033[31m", "FAKE" ,"\033[0m", "one piece fan!")
  else:
    print("See!" ,"\033[31m", "FAKE" ,"\033[0m", "one piece fan!")
else:
  print("You should watch one piece sometime😉")