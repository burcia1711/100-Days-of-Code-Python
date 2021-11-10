from turtle import *

timmy: Turtle = Turtle()
timmy.color("coral")
timmy.shape("turtle")

color('black', 'CadetBlue3')
begin_fill()
while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break
end_fill()
done()