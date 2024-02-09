counter = 1
while True:
  print("\033[34m", "Complete the lyrics!", "\033[0m")
  fill = input("Sitambui wewe maunenge...mamiwa maembe na _______")
  if fill == "marenge" or fill == "Marenge":
     break
    
  else:
    if counter < 4:    
     print("Try again!")
    elif counter == 4:
      print("Stop it...go get help")
    elif counter > 4: 
      print("You're not even trying! Go get help!")
  go_on = input("Do you want to retry?")
  if go_on =="yes" or go_on == "Yes":
    counter += 1
    continue
  elif go_on == "no" or go_on == "No" or go_on == "NO":
    break
  else:
    read = input("Caan you read English?")
    if read == "yes" or read == "Yes" or read == "YES":
      print("Read and understand the questions then!")
    elif read == "no" or read == "No" or read == "NO":
      print("Please leave the game!")
      break
    else:
      print("Follow the preset path and live...go against the preset path...and you'll die without even knowing how to read!")
      break
   
if fill == "marenge" or fill == "Marenge" or fill =="MARENGE":
  print("You got the correct answer in", counter, "attempts!")
  if counter == 1:
    print("You are good at this...though I'm not sure if that's a compliment haha")
  elif counter == 2:
    print("You could have answered this in 1 attempt. Why didn't ya?")
  elif counter == 3:
    print("Not baad...not good either")
  elif counter == 4:
    print("You are so poor at this")
  elif counter > 4:
    print("You are a disgrace to Kenyans and humanity as a whole!Leeave😡")

else:
  print("Yoou suck at this...come back when you're ready")
  if counter >= 3:
    print("At least you attempted...find the answer in the next line")
    print("https://kelxfy.com/kaveve-kazoze-meaning-in-sheng-lyrics-by-ngesh/")