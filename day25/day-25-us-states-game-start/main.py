import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
turtle.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
score = 0

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 guess the state ", prompt="whats the state name?").title()
    if answer_state == "Exit":
        print(state_list)
        new_data = pandas.DataFrame(state_list)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        turtle_text = turtle.Turtle()
        turtle_text.hideturtle()
        turtle_text.penup()
        state_data = data[data.state == answer_state]
        turtle_text.goto(state_data.x.item(), state_data.y.item())
        turtle_text.write(f"{state_data.state.item()}")
        score += 1
        state_list.remove(answer_state)


