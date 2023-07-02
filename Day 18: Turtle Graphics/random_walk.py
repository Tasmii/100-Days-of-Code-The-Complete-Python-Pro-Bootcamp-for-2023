from turtle import Turtle, Screen
import random

timmy = Turtle()
colours = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']
directions=[0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(5)
for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
