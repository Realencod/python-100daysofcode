print("=======GENERATION GENERATOR========")
gender = input("What should I refer you as....." ,"\033[33m","male" ,"\033[0m" ,"," ,"\033[33m" ,"female" ,"\033[0m" ,"or" ,"\033[33m" ,"they?")
year = int(input("What year were you born?"))
if year >=1926 and year<=1946:
  print("Traditionalist...be kind enough as to share your wisdom with us young ones")
elif year >= 1947 and year < 1964 and gender == "female" or gender == "Female":
  print("Hello grandma!")
elif year >= 1947 and year < 1964 and gender == "male" or gender == "Male":
  print("Hello grandpa!")
elif year >= 1947 and year < 1964 and gender == "they" or gender == "They":
  print("Woah ,I'm surprised that this option existed in your time")

