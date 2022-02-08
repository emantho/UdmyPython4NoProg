# Make a program asking for width and height of a reactangle and draw it with *

def rectangleWidth(width):
    print("*" * width)

def rectangleHeight(height,width):
    for i in range(height):
        rectangleWidth(width)

userWidth = int(input("Enter the width of rectangle to draw: "))
userHeight = int(input("Enter the height of rectangle: "))

rectangleHeight(userHeight,userWidth)

# other solution
'''def draw(width,height):
    for i in range(height):
        for j in range(width):
            print("*",end="")
        print()

width = int(input("enter width: "))
height = int(input("enter the height: "))

print()
draw(width,height)'''