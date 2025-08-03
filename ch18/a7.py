import turtle


turtle.setup(410, 310)
screen = turtle.Screen()
screen.bgcolor("black")


star = turtle.Turtle()
star.shape("turtle")
star.pensize(1)
star.speed(0.5)

def drawStar(size, color):
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)

    star.hideturtle()  


drawStar(60, "yellow")


turtle.exitonclick()
