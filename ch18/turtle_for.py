import turtle

turtle.setup(500,500)

turtle.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.pencolor("skyblue")
t.pensize(1)
colors = ['skyblue','yellow','green','blue','purple']
for i in range(5):
    t.pencolor(colors[i])
    t.right(144); t.fd(70)
t.hideturtle()
turtle.exitonclick()