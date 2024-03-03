print("welcome to the world's best debt calculator...answer a few questions to get started")
loan = float(input("How much were you loaned?>>"))
interest = float(input("What is the percentage interest for the loan?>>"))
years = int(input("How many years has it been since you took the loan? (rounded off to the nearest year)>>"))

for counter in range(1, years + 1):
    loan = round( loan + (loan * interest/100), 2)
    print("Year",counter,loan)
