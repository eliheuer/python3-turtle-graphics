from math import sin, cos, pi
from turtle import Turtle, Screen

def line(x1, y1, x2, y2, turtle):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def graph(f, t, c):
    t.pensize(8)
    t.pencolor(c)
    x = -4
    t.penup()
    t.goto(x, f(x*2))
    t.pendown()
    while x < 4:
        x += 0.1
        t.goto(x, f(x*2))

def main():
    e = Turtle()
    s = Screen()
    s.setworldcoordinates(-4,-2,4,2)
    s.bgcolor('gray12')
    s.reset()
    e.shapesize(2,2,2)
    e.pencolor('grey45')
    e.pensize(4)
    line(-4, 0, 4, 0, e)
    line(0, -2, 0, 2, e)
    graph(sin, e, 'red')
    graph(cos, e, 'yellow')
    return "DONE! :-)"

if __name__ == "__main__":
    msg = main()
    print(msg)
    Screen().mainloop()
