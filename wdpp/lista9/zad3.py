import turtle

t = turtle.Turtle()
s = turtle.getscreen()

s.tracer(0)

def kwadrat():
    for _ in range(4):
        t.forward(30)
        t.left(90)

def repeat_on_circle(figure, r, n):
    for _ in range(n + 1):
        t.penup()
        t.forward(r)
        t.pendown()
        figure()
        t.penup()
        t.backward(r)
        t.pendown()
        t.left(360 / n)

for i in range(11):
    t.penup()
    t.forward(320)
    repeat_on_circle(kwadrat, 60, 15)
    t.penup()
    t.goto(0, 0)
    t.setheading(36 * i)

turtle.mainloop()
