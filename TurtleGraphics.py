#TurtleGraphics.py
#Name:Liam Gillispie
#Date:2/15/2026
#Assignment:Lab 4
#Purpose: Create shapes and loops with the Turtle on CodeHS

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    hideturtle()
    up()
    goto(-100,0)
    down()
    left(45)
    for i in range(5):
        forward(100)
        right(72)
    # drawPolygon(myTurtle, 8) #draws an octogon
    hideturtle()
    up()
    goto(-100,0)
    down()
    left(45)
    for i in range(8):
        forward(100)
        right(45)
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    hideturle()
    up()
    goto(-150,150)
    down()
    def drawSquare():
        for i in range(4):
            forward(size)
            right(90)
    size=300
    drawSquare()
    forward(200)
    begin_fill()
    size=100
    drawSquare()
    end_fill()
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    hideturtle()
    up()
    goto(-150,150)
    down()
    def drawSquare():
        for i in range(4):
            forward(size)
            right(90)
    size=300
    drawSquare()
    right(90)
    forward(300)
    left(90)
    forward(100)
    left(180)
    begin_fill()
    size=100
    drawSquare()
    end_fill()
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    hideturtle()
    up()
    goto(-150,-150)
    down()
    def square(size):
        for i in range(4):
            forward(size)
            left(90)
    def squaresInSquares(start_square, num_squares, size_dec):
        current_square=start_square
        for i in range(num_squares):
            if current_square<=0:
                break
            square(current_square)
            up()
            forward(size_dec/2)
            left(90)
            forward(size_dec/2)
            right(90)
            down()
            current_square-=size_dec
    squaresInSquares(300,5,20)
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    hideturtle()
    up()
    goto(-150,-150)
    down()
    def square(size):
        for i in range(4):
            forward(size)
            left(90)
    def squaresInSquares(start_square, num_squares, size_dec):
        current_square=start_square
        for i in range(num_squares):
            if current_square<=0:
                break
            square(current_square)
            up()
            forward(size_dec/2)
            left(90)
            forward(size_dec/2)
            right(90)
            down()
            current_square-=size_dec
    squaresInSquares(300,3,20)

main()
