import turtle

turtle.setup(410, 310)
screen = turtle.Screen()
screen.bgcolor("black")

moon = turtle.Turtle()
moon.speed(5)
moon.pensize(1)

def drawMoon(x, y, size, color):
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    
    moon.color(color)
    moon.begin_fill()
    moon.circle(size)  
    moon.end_fill()
    

    moon.penup()

    moon.goto(x + size*0.4, y + size*0.2)
    moon.pendown()
    
    moon.color(screen.bgcolor())  
    moon.begin_fill()
    moon.circle(size * 0.8)
    moon.end_fill()
    
    moon.hideturtle()


drawMoon(0, 0, 40, "lightgray")

turtle.exitonclick()
