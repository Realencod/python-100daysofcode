#parameters - are variables defined within the parantheses during function definition
#arguments - value passed to a function when it is called. Could be a variable, value or object passed to a function or method as input
#               *written while calling a function
def sum(a,b):
    print(a + b) # a and b in this case are the parameters

sum(3,4) # 3 and 4 are the arguments in this case

#TYPES OF ARGUMENTS

#Positional arguments
def name(first_name, second_name):
    print(first_name, second_name)

name("Monari", "Frank") # argument is expressed in the order of the parameters
name("Frank", "Monari") # arguments have to be expressed in the correct order for them to align with the preset parameters

#Key word arguments
name(second_name = "Nabei", first_name = "Allan") #the order in which the arguments are written does not matter in this case
# * the order of keyword argument with respect to another key word argument does not matter because the values are explicitly assigned

