import turtle

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("")

    
    t = turtle.Turtle()
    t.hideturtle()  
    t.penup()

   
    screen.exitonclick()

if __name__ == "__main__":
    main()
