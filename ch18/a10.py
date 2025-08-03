import turtle


turtle.setup(600, 500)
screen = turtle.Screen()
screen.bgcolor("black")


star = turtle.Turtle()
moon = turtle.Turtle()


for t in (star, moon):
    t.speed(0)
    t.pensize(1)
    t.hideturtle()


def drawStar(x, y, size, color):
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)


def drawMoon(x, y, size, color):
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    moon.color(color)
    moon.begin_fill()
    moon.circle(size)
    moon.end_fill()

    moon.penup()
    moon.goto(x + size * 0.4, y + size * 0.2)
    moon.pendown()
    moon.color(screen.bgcolor())
    moon.begin_fill()
    moon.circle(size * 0.8)
    moon.end_fill()

stars = [
    (-200, 100, 40, "yellow"),
    (-100, 150, 30, "white"),
    (0, 120, 50, "yellow"),
    (150, 180, 35, "white"),
    (200, 90, 25, "yellow"),
]

for x, y, size, color in stars:
    drawStar(x, y, size, color)


drawMoon(100, -50, 60, "lightgray")

turtle.exitonclick()
