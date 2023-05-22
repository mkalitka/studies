import random
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def kwadrat(color="red"):
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(10)
        t.right(90)
    t.end_fill()

mapa = [0] * 102

for i in range(len(mapa)):
    mapa[i] = [0] * 102


for _ in range(random.randint(2, 4)):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    mapa[x][y] = random.randint(50, 100) / 100
    mapa[x - 1][y] = mapa[x][y]
    mapa[x - 1][y - 1] = mapa[x][y]
    mapa[x][y - 1] = mapa[x][y]
    mapa[x + 1][y - 1] = mapa[x][y]
    mapa[x + 1][y] = mapa[x][y]
    mapa[x + 1][y + 1] = mapa[x][y]
    mapa[x][y + 1] = mapa[x][y]
    mapa[x - 1][y + 1] = mapa[x][y]

for _ in range(10000):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    srednia = (mapa[x - 1][y] + mapa[x - 1][y - 1] + mapa[x][y - 1] + mapa[x + 1][y - 1] + mapa[x + 1][y] + mapa[x + 1][y + 1] + mapa[x][y + 1] + mapa[x - 1][y + 1]) / 8
    mapa[x][y] = (mapa[x][y] + srednia) / 2

t.speed(10)
turtle.speed(10)
t.penup()
t.goto(-500, 500)
t.pendown()
kwadrat()

for i in mapa:
    print(i)

turtle.mainloop()
