import turtle

pen_color = ['red','orange','yellow',
             'green','blue','navy','purple']
def rainbow(radius,x,y):
    rainbow = turtle.Turtle()
    rainbow.speed(2)
    rainbow.pensize(5)

    for i in reversed(pen_color):
        rainbow.penup()
        rainbow.color(i)
        rainbow.goto(x,y)
        rainbow.pendown()


        rainbow.setheading(90)
        rainbow.circle(radius,180)
       
        x +=5
        radius+=5



        rainbow.hideturtle()


if __name__ == '__main__':
    turtle.setup(410,310)
    turtle.bgcolor('skyblue')
    rainbow(50,50,0)
    turtle.exitonclick()

