from turtle import Turtle, Screen

timmy = Turtle()
for _ in range(50):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
screen = Screen()
screen.exitonclick()
