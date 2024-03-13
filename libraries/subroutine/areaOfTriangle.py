def AreaOfTriangle(base, height):
    area = 0.5 * base * height
    return area

print("Area of a triangle")
base = int(input("What is the base of your triangle?>>"))
height = int(input("What's the height?>>"))

area = AreaOfTriangle(base, height)   #the variable area in the subroutine is only available in the subroutine and doesn't affect stuff out of its jurisdiction
print("The area of the Triangle is", area) # ie the variable area in this case is treated as a separate entity that is not related to the one in the subroutine(indent)