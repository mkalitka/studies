import turtle

def gwiazda(t, size):
    if size <= 10:
        return
    else:
        for _ in range(5):
            t.forward(size)
            gwiazda(t, size / 3)
            t.left(216)

t = turtle.Turtle()
s = turtle.getscreen()

s.tracer(0)

t.penup()
t.goto(-200, 50)
t.pendown()
gwiazda(t, 360)
turtle.mainloop()
