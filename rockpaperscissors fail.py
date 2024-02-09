from getpass import getpass as input
print("""                                 ROCK PAPER SCISSORS ULTIMATE WORD GAME             """)
#rules of the game
print("\033[33m", """Thank you for taking your time to try out our rock paper scissors game
          Here are a few rules to get you on track!
          Rock breaks scissors....scissors on the other hand cuts paper and lastly paper beats 
           the rock...by covering it or something :D""", "\033[0m")
print("""Another important piece of information to note is that instead of typing the full sstatements 
      that is either rock...paper or scissors....just key in""", "\033[33m", """r for rock...p for paper and s for scissors
      either in caps or not""", "\033[0m")
print()
#thee game

#player 1 and 2 input
player1 = input("Player1>")
player2 = input("Player2>")
print()

if player1 == "r" or player1 == "R" and player2 == "r" or player2 == "R":
  print("A bunch of rocks rubbing against one another...what a stupid way to draw😩")
elif player1 == "r" or player1 == "R" and player2 == "p" or player2 == "P":
  print("Aand the rock is folded in the paper neatly...never to be seen again!")
  
#apparently this code doesn't work...I'm not sure why though...I hope I'll find out why it doesn't soon enough

