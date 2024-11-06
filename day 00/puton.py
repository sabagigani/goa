from turtle import *

#we want to paint o hause

#step 1: draw a spuare

width(7)
color("yellow")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
left(90)
end_fill()
color("blue")
begin_fill()
forward(90)
right(90)

forward(50)
right(90)

forward(90)
end_fill()
penup()
goto(200, 200)
pendown()
end_fill()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()