from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(725, 491)
screen.tracer(0)
t = Turtle()
t.penup()
t.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data["state"].values.tolist()
x = data["x"].values.tolist()
y = data["y"].values.tolist()
coordinates = [{state: (x,y)} for state, x, y in zip(states, x, y)]
max_score = len(states)
guesses = []

while len(guesses) < max_score:
    answer = screen.textinput(f"{len(guesses)}/50 Guess the state:", "Enter a state")
    if answer == "Exit":
        break
    if answer in states and answer not in guesses:
        guesses.append(answer)
        index = states.index(answer)
        t.goto(coordinates[index][answer])
        t.pendown()
        t.write(states[index], align="center", font=("Arial", 6, "normal"))
        t.penup()


to_learn = []
for state in states:
    if state not in guesses:
        to_learn.append(state)

learn = pandas.DataFrame(to_learn)
learn.to_csv("to_learn.csv")

screen.exitonclick()
