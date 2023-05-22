import turtle

def kwadrat(color=(0,0,0)):
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.forward(50)

with open("obraz.txt") as f:
    data = f.readlines()
    f.close()

s = turtle.getscreen()
t = turtle.Turtle()
turtle.tracer(0, 1)
turtle.colormode(255)

t.penup()
t.goto(-75, 75)

for i in range(len(data)):
    d = data[i].split()
    for j in d:
        color = eval(j)
        print(color)
        kwadrat(color)
    t.backward(50 * (len(d)))
    t.right(90)
    t.forward(50)
    t.left(90)

turtle.mainloop()
