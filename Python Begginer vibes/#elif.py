print()
print("\033[33m" ,"SECURE LOGIN.")
print("\033[0m")
username= input("Username >")
password = input("Password >")
print()
if username == "Frank" and password == "1234":
  print("Welcome master!")
elif username == "frank" and password == "1234":
  print("Welcome master!")
elif username == "keys" and password == "1234":
  how = input("Hey there siz! Are you doing great?")
  if how == "yes":
    print("Thats absolutely great to hear!")
  elif how == "no":
    input("Oh dear, What could the problem be?")
    print("""I'm so sorry to hear that😯, I hope that you'll get through it""")
elif username == "Keys" and password == "1234":
    how = input("Hey there siz! Are you doing great?")
    if how == "yes":
      print("Thats absolutely great to hear!")
    elif how == "no":
      input("Oh dear, What could the problem be?")
      print("""I'm so sorry to hear that😯, I hope that you'll get through it""")
elif username == "lydia" and password == "1234":
    how = input("Hey there siz! Are you doing great?")
    if how == "yes":
      print("Thats absolutely great to hear!")
    elif how == "no":
      input("Oh dear, What could the problem be?")
      print("""I'm so sorry to hear that😯, I hope that you'll get through it""")
elif username == "Lydia" and password == "1234":
  how = input("Hey there siz! Are you doing great?")
  if how == "yes":
    print("Thats absolutely great to hear!")
  elif how == "no":
    input("Oh dear, What could the problem be?")
    print("""I'm so sorry to hear that😯, I hope that you'll get through it""")

else:
  print("Username or password incorrect")
print()
print("\033[33m" ,"Have a great day!" ,"\033[0m")