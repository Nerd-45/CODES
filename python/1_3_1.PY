def findarea(radius):
    pi = 22/7
    area_of_circles = pi * radius * radius
    print("The area of circle is ",area_of_circles)
for i in range(0,10):
    r = int(input("enter Radius of circle : "))
    findarea(r)
