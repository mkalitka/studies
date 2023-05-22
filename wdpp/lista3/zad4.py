import turtle
from random import randint

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(10)
t.penup()
t.backward(150)
t.left(90)
t.backward(75)

height = 20

for i in range(40):
	t.pendown()
	t.forward(height)
	t.right(90)
	t.forward(5)
	t.right(90)
	t.forward(height)
	t.right(90)
	t.forward(5)
	t.right(180)
	t.penup()
	t.forward(7)
	t.left(90)
	height += randint(0, 4)

turtle.mainloop()
