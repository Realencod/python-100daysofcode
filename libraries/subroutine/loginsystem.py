def loginsystem():
    while True:
        name = input("What is your name?").lower()
        password = input("What's your password?").lower()
        
        if name == "frank" and password == "0000":
            print("Welcome back master!")
            break
        
        elif name == name and password == "0000":
            print("Welcome back guest user, make yourself comfortable.")
            break
        
        else:
            print("Wrong username or password!")
            retry = input("Try again?>>").lower()
            if retry != "yes":
                exit(("Byee!"))
            else:
                continue
    print("Login succesful!")
print()
loginsystem()