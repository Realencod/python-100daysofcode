counter = 0
while True:
  number = int(input("Enter a number:"))
  print("Adding it up!")
  counter += number
  print("Cumulative total is", counter)
  addanother = input("Add another number?")
  if addanother == "no" or addanother == "No" or addanother == "NO":
    break
  elif addanother == "yes" or addanother == "Yes" or addanother == "YES":
    continue
print("Thank you for your time! Byee")  
