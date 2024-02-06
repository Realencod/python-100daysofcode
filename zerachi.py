print("\033[33m", """                                     ZERACHI                                           """, "\033[0m")
print("We as the zerachi team are obliged to give you the perfect grading in accordance to your marks...please type in your information below😌")
name = input("What is your name?:")
subject = input("What is the name of the test that you pertook in?:")
max = int(input("What is the maximum achievable number of points for the case of your test?:"))
actual = int(input("What was your score in the test out of the maximum number of points?:"))
percentage = (actual / max) * 100
answer = round(percentage, 2)
if answer >= 90 and answer <= 100:
  print("PERCENTAGE:", answer, "%")
  print("GRADE:",  "A+")
  print("REMARKS: Excellent! You must have really worked hard for your grade...please keep up the good spirit!😁")
elif answer >= 80 and answer <= 89:
  print("PERCENTAGE:", answer, "%")
  print("GRADE:",  "A")
  print("REMARKS: Good work...you are part of the cream..just note that you've not achieved the best possible grade yet so don't slack off!")
elif answer >= 70 and answer <=79:
  print("PERCENTAGE:", answer, "%")
  print("GRADE:",  "B")
  print("REMARKS: You've done well but I'm sure you know that this is not your best so strive towards achieving the very best that you can✊")
elif answer >= 60 and answer <= 69: 
  print("PERCENTAGE:", answer, "%")
  print("GRADE:",  "C")
  print("REMARKS: Your marks are so so😄 I know studying is quite hard but please put in smart effort into it.That's all")
elif answer >= 50 and answer <= 59:
  print("PERCENTAGE:", answer, "%")
  print("GRADE:",  "D")
  print("REMARKS: You are only slightly above average...not something to be quite excited about is it? Pull yourself together and begin working!☹ ")
elif answer < 50:
  print("PERCENTAGE:", answer, "%")
  print("GRADE:",  "E")
  print("REMARKS: All play and no work makes John a dull boy...don't be like John")
print()
print("Thank you for using ZERACHI for your grading...we are glad that we could be of help to you", name, "😁")


  

