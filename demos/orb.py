from turtle import *

def draw_circle(resolution, size):
    for i in range(resolution):
        rt(360./resolution)
        fd(size)

def draw_object(resolution, size):
    for i in range(resolution):
        pencolor(1.0, 0.0, 0.0)
        rt(360./resolution)
        draw_circle(resolution, size)

def main():
    hideturtle()
    bgcolor(0.03, 0.03, 0.03)
    pensize(6)
    tracer(1,0)
    draw_object(12, 80)
    return "DONE! :-)"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
