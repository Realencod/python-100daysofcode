score = 0
print("Welcome to the math quiz!")
name = input("What is your name?>>")
print(name, "pick any multiple and you'll be asked a multiplication quiz to check on your comprehension level")
multiple = int(input("Name your multiple>>"))
for i in range(1, 11, 1):
    print(i, "x", multiple, "=")
    answer = int(input("Answer>>"))
    correct_answer = i*multiple
    if answer == correct_answer:
       print("Great job! That is the correct answer")
       score += 1
    else:
        print("That's not the correct answer😥")
        print("The correct answer is", correct_answer)

if score == 10:
    print("Wow a perfect score! You are really good at this")  
elif score > 6 and score <= 9:
    print("Not bad...that was a nice trial...you,", name, "scored",score, "out of 10")      
else:
    print("Really?", name, score, "out of 10 was all that you could manage?")

