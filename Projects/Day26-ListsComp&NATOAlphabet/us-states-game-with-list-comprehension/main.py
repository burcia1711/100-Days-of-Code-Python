import turtle, pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
true = 0
right_answers = []
data = pandas.read_csv("50_states.csv")
all_sates = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{true}/50 States Correct", prompt="What is the state's name?").title()

    if answer_state == 'Exit':

        missing_states = [state for state in all_sates if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in data.state:
        if answer_state not in right_answers:
            if answer_state == state:
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                true += 1
                right_answers.append(answer_state)
                t.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
                t.write(answer_state)


screen.exitonclick()