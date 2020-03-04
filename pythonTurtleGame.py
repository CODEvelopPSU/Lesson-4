from turtle import *
import random

def main():
    numSides = int(input("Enter the number of sides you want your shape to have, type a number less than 3 to exit: "))

    while numSides >= 3:
        polygon(numSides)
        numSides = int(input("Enter the number of sides you want your shape to have, type a number less than 3 to exit: "))
    else:
        print("Thank you for using the polygon generator!")


def polygon(x):
    sideLength = 600/x

    colors = ["gold", "red", "blue", "green", "purple", "black", "orange"]

    shapeColor = random.choice(colors)

    borderColor = random.choice(colors)

    borderSize = (x % 20) + 1

    makePolygon(x, sideLength, borderColor, borderSize, shapeColor)


def makePolygon(sides, length, borderColor, width, fillColor):
    clear()

    angle = 360/sides

    shape("turtle")

    pencolor(borderColor)

    fillcolor(fillColor)

    pensize(width)

    begin_fill()
    while True:
        if sides != 0:
            forward(length)
            left(angle)
            sides -= 1
        else:
            break

    end_fill()

main()















