print("""                                     ULTIMATE ROCK PAPER SCISSORS GAME!!!                                   """)
print()
#rules
print("\033[33m", """type: r for rock
       p for paper
       s for scissors """, "\033[0m")
print()

proceed = "yes"
while proceed == "yes" or proceed == "Yes":
 
 from getpass import getpass as input
 player1 = input("Player1>")
 player2 = input("Player2>")

 if player1 == "r" or player1 == "R":
  if player2 == "r" or player2 == "R":
    print("Two rocks were banged against each other...all of them broke into small pieces...don't be like the two rocks")
  elif player2 == "p" or player2 == "P":
    print("And the stupid rock was smothered by the paper...what a loss to player1")
  elif player2 == "s" or player2 == "S": 
    print("Bang! is the sound that was heard at the sacrifice of player2's scissors")
  else:
    print("\033[31m", "Wrong move player2!", "\033[0m")

 elif player1 == "p" or player1 == "P":
   if player2 == "r" or player2 == "R":
     print("Aand it's player1's win...I bet you didn't see that one coming player2")
   elif player2 == "p" or player2 == "P":
    print("Two papers rubbing against each other...what a high level of foolishness")
   elif player2 == "s" or player2 == "S": 
    print("The sound of a paper being cut has never been so exhilirating...player2 wins")
   else:
    print("\033[31m", "Wrong move player2!", "\033[0m")

 elif player1 == "s" or player1 == "S":
   if player2 == "r" or player2 == "R":
     print("Tang' Tang' Tang' nini mbaya nini mbaya!!! Player1 has been K.Oed")
   elif player2 == "p" or player2 == "P":
     print("It's your loss player2...you went against the grain and challenged a scissors despite being a paper...who does that?")
   elif player2 == "s" or player2 == "S": 
     print("As Iron sharpens iron....so does a metallic scissor sharpen another...LOL cut the cra*")
   else:
    print("\033[31m", "Wrong move player2!", "\033[0m")
 else:
  print("\033[31m", "Wrong move player1!", "\033[0m") 
 proceed = input ("Do you want to continue?:")