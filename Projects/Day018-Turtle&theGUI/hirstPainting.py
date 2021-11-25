import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(184, 163, 128), (134, 94, 60), (64, 37, 22), (158, 128, 88), (103, 50, 30), (204, 195, 169), (84, 67, 33), (210, 201, 178), (27, 20, 23), (20, 21, 24), (22, 26, 22), (175, 113, 84), (92, 102, 88), (84, 74, 77), (89, 46, 48), (100, 101, 104), (131, 138, 132), (211, 188, 174), (128, 133, 136)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()