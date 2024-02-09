print("I love your smile!")
exit = ""
while exit != "yes":
   animal1 = input("What animal do you want?")
   if animal1 == "Cow" or animal1 == "cow":
      print("A cow goes moo!")
   elif animal1 == "Dog" or animal1 == "dog":
      print("A dog goes woof!")
   else:
      print("You should try either a dog or a cow")
   exit = input("Do you want to exit?:")
   if exit == "yes":
      print("Have a great day!")