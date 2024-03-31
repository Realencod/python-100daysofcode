miles = float(input("State the number of miles>>"))
def km(miles):
    km = miles * 1.6
    return km

final = km(miles)
y = round(final, 15)
print(f"The number of kilometres covered is {y} km")