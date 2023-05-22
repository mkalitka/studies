import turtle
from random import randrange

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
t.speed("fastest")
turtle.colormode(255)

t.penup()
t.goto(-75, 75)

kolory = []
for i in range(len(data)):
    rzad = []
    d = data[i].split()
    for j in d:
        color = eval(j)
        rzad.append(color)
    kolory.append(rzad)

limit = 0
powt = True
while powt:
    x = randrange(0, len(kolory))
    z = randrange(0, len(kolory[x]))
    if kolory[x][z] != (-1, -1, -1):
        kwadrat(kolory[x][z])
        kolory[x][z] = (-1, -1, -1)
        limit += 1
    if limit == len(kolory[x]):
        t.backward(50 * (len(kolory[x])))
        t.right(90)
        t.forward(50)
        t.left(90)
        limit = 0
    powt = False
    for i in kolory:
        for j in i:
            if j != (-1, -1, -1):
                powt = True
                break

turtle.mainloop()
