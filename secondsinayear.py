print("=======SECONDS IN A YEAR======")
year = int(input("You would like to find out the number of seconds in a certain year....question is, which year?:"))
print()
print("\033[33m", "ON IT!", "\033[0m")
modulus = year % 4
if modulus == 0:
  seconds = 366*24*60*60
  print("The year", year, "has", seconds, "seconds.")
elif modulus == 1 or 2 or 3:
  seconds = 365*24*60*60
  print("The year", year, "has", seconds, "seconds.")
else:
  print("Type in figures please")
print()
print("Thank you for using our programme!")
  