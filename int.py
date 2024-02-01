print("=======GENERATION GENERATOR========")
#only male,female and they in yellow
print("What should I refer you as....." ,"\033[33m","male" ,"\033[0m" ,"," ,"\033[33m" ,"female" ,"\033[0m" ,"or" ,"\033[33m" ,"they?", "\033[0m")
gender = input("Gender:")
year = int(input("What year were you born?"))
  #1926 to 1946
if year >=1926 and year<=1946:
  print("Traditionalist...be kind enough as to share your wisdom with us young ones")
  #1947 to 1964
elif year >= 1947 and year < 1964 and gender == "female" or gender == "Female":
  print("Hello grandma!")
elif year >= 1947 and year < 1964 and gender == "male" or gender == "Male":
  print("Hello grandpa!")
elif year >= 1947 and year < 1964 and gender == "they" or gender == "They":
  print("Woah ,I'm surprised that this option existed in your time")
  #1965 to 1981
elif year >= 1965 and year <=1981:
  print("Generation liberised...happy after independence to you!")
  #1982 to 1995
elif year >= 1982 and year <= 1995:
  millennium = input("How did crossing the millenium feel? bad,good, great,amazing or neutral?")
  if millennium == "great" or millennium == "good" or millennium == "amazing":
    print("For the best!")
    memorable = input("What was your most memorable event?:")
  elif millennium == "bad":
    sorry = input("Oh I'm so sorry about that...what annoyed you?:")
  elif millennium == "neutral":
    print("That's alright and all I guess")
  #1996 to 2015
elif year >=1996 and year <=2015:
  print("Congratulations...you're part of the", "\033[31m" ,"worst", "\033[0m" ,"generation")
print()
print("Thank you for your time!😁")

