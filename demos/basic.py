from turtle import Turtle, Screen

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

def main():
    e = Turtle()
    s = Screen()
    s.setup(800, 600)
    s.bgcolor('gray6')
    s.reset()
    e.pensize(3)
    for i in range(1,31):
        e.pencolor(1.0, 0.0+(i/50), 0.0)
        e.left(90/i)
        drawsq(e, 200)
    return "DONE! :-)"

if __name__ == "__main__":
    msg = main()
    print(msg)
    Screen().mainloop()
