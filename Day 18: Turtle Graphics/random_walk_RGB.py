import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

#colours = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']
directions=[0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(5)
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
