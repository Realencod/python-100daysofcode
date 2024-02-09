mybill = float(input("What's the bill?:"))
tip = int(input("What percentage do you want to tip?:"))
mybill = ((tip + 100) / 100) * mybill
print()
print("Total bill is", mybill)
people = int(input("How many people?:"))
answer = mybill / people
answer = round(answer, 2)
print("Ya'll should conntribute" ,answer)