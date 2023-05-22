import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(10)
t.penup()
t.backward(300)
t.left(90)
t.backward(80)
t.pendown()

height = 5
dodawanie = True

for i in range(140):
    t.forward(height)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(5)
    t.left(180)
    t.forward(5)
    t.left(90)
    if i < 10:
        height += 5
    elif i >= 10 and i < 20:
        height += 4
    elif i >= 20 and i < 30:
        height += 3
    elif i >= 30 and i < 33:
        height += 2
    elif i >= 33 and i < 34:
        height += 1
    elif i >= 36 and i < 37:
        height -= 1
    elif i >= 37 and i < 40:
        height -= 2
    elif i >= 40 and i < 50:
        height -= 3
    elif i >= 50 and i < 60:
        height -= 4
    elif i >= 60 and i < 80:
        height -= 5
    elif i >= 80 and i < 90:
        height -= 4
    elif i >= 90 and i < 100:
        height -= 3
    elif i >= 100 and i < 103:
        height -= 2
    elif i >= 103 and i < 104:
        height -= 1
    elif i >= 106 and i < 107:
        height += 1
    elif i >= 107 and i < 110:
        height += 2
    elif i >= 110 and i < 120:
        height += 3
    elif i >= 120 and i < 130:
        height += 4
    elif i >= 130 and i < 140:
        height += 5

turtle.mainloop()
