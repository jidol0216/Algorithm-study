import turtle

turtle.setup(410,310)

t = turtle.Turtle()

t.shape("turtle")

t.pensize(1)
t.speed(0)


n = 5

for i in range(n):
    t.forward(i)
    t.right(144)

turtle.exitonclick()