import turtle as t
import math

t.pensize(3)


t.penup()
t.goto(-70, 50)
t.pendown()
t.goto(-90, 70)


t.penup()
t.goto(70, 50)
t.pendown()
t.goto(90, 70)

t.penup()
t.goto(0, -100) 
t.pendown()
t.circle(100)

side_length = 100 * math.sqrt(3) 
height = (math.sqrt(3) / 2) * side_length


points = []
for i in range(3):
    angle_deg = 90 + i * 120
    angle_rad = math.radians(angle_deg)
    x = 100 * math.cos(angle_rad)
    y = 100 * math.sin(angle_rad)
    points.append((x, y))

t.penup()
t.goto(points[0])
t.pendown()
for i in range(1, 3):
    t.goto(points[i])
t.goto(points[0]) 
t.hideturtle()
t.done()
