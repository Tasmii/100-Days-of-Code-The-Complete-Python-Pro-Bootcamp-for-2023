#NOTE:
#It's important to note that this code assumes the presence of two files: "blank_states_img.gif" for the map image and "50_states.csv" for the state data. 
#Additionally, it creates a new file called "states to learn.csv" to store the names of the states that the user did not guess correctly.
#If another user intends to run this code, they need to make sure they have the required files in the specified locations and modify the file paths accordingly.

import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"Day 25 US State Game (CSV Data)\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"Day 25 US State Game (CSV Data)\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states = []
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        #print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day 25 US State Game (CSV Data)/states to learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
