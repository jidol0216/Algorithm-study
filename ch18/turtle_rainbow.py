import turtle

colors =[ 'red','orange','yellow','green','blue','navy','purple']

t = turtle.Turtle()
turtle.bgcolor("black")


t.shape("turtle")

t.pensize(1)
t.speed(0)

def a(n):
    for i in colors:
        t.color(i)
        t.circle(n)
        n +=5








a(50)

t.hideturtle()
turtle.exitonclick()