import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

states = data["state"]
all_states = data.state.to_list()


writer = turtle.Turtle()
writer.up()
writer.hideturtle()

guessed_state = set()
while len(guessed_state) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_state)}/50 States Correct", prompt= "What's another state's name?").title().strip()
    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_state:
                states_to_learn.append(state)
            
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in guessed_state:
        continue
    elif answer_state in all_states:
        guessed_state.add(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(answer_state , align="center", font= ("Arial", 8, "normal"))




