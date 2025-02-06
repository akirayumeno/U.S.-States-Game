import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What is another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if answer_state not in guess_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 10, "bold"))

# saving the missing state to .csv

# keep the screen on even you click the screen
# turtle.mainloop()

# screen.exitonclick()