from math import sin, cos, pi
from turtle import Turtle, Screen

def main():
    turtle = Turtle()
    screen = Screen()
    screen.setworldcoordinates(-4,-2.5,4,2.5)
    screen.bgcolor('gray12')
    screen.reset()
    turtle.shapesize(1,1,1)
    turtle.pencolor('grey45')
    turtle.pensize(4)
    turtle.speed("fast")

    # Draw grid
    x = -4
    while x <= 4.1:
        turtle.goto(x, 0)
        if round(x,3) % 1 == 0:
            turtle.goto(x,0.4)
            turtle.goto(x,-0.4)
        turtle.goto(x, 0)
        x += 0.2
        print("x =",round(x,4))

    turtle.penup()
    x = 0
    y = -2
    while y <= 2:
        turtle.goto(0, y)
        turtle.pendown()
        if round(y,3) % 1 == 0:
            turtle.goto(0.4, y)
            turtle.goto(-0.4, y)
        turtle.goto(0, y)
        y += 0.2
    turtle.pencolor('red')

    # Move turtle to start point
    x = -4
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()

    # Draw graph    
    while x <= 4:
        turtle.goto(x, sin(x))
        x += 0.1
    return "DONE! :-)"

if __name__ == "__main__":
    msg = main()
    print(msg)
    Screen().mainloop()
