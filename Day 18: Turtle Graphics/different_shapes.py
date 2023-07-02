from turtle import Turtle, Screen
import random

timmy = Turtle()
colours = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        timmy.forward(50)
        timmy.left(angle)

for i in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(i)

screen = Screen()
screen.exitonclick()
