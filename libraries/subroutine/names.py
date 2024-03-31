def person(name):
    if name == "frank":
       print("Welcome back boss!")
    elif name == "lydia":
        print("Welcome, boss' siz")
    elif name == "kevin":
        print("Welcome boss' only brother!")
    elif name == "osama":
        print("\033[31m", "Oh no....run for my life!", "\033[0m")

you = input("What's your name?>>").lower()
person(you)
  
