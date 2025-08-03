import turtle

turtle.setup(410, 310)
screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.shape("turtle")
star.pensize(1)
star.speed(5)  

def drawStar(x, y, size, color):
    star.penup()          
    star.goto(x, y)       
    star.pendown()        
    star.color(color)
    star.pensize(1)
    star.speed(5)

    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)


    star.hideturtle()    


drawStar(0, 0, 60, "yellow")

turtle.exitonclick()
