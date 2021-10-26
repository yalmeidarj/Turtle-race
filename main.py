import random
import turtle as t
screen = t.Screen()
screen.setup(width=500, height=400)
color = ["red", "yellow", "green", "purple", "grey", "blue"]
user_bet = screen.textinput(title="Make your bet.", prompt="Choose a turtle color:\nRed, yellow, green, purple, grey, blue").lower()

is_race_on = False


rand_distance = random.randint(0, 35)
if user_bet:
    is_race_on = True


list_turtles = []
position = []
if is_race_on:
    for p in range(len(color)):
        new_pointer = t.Turtle(shape="turtle")
        new_pointer.color(color[p])
        new_pointer.name = (color[p])
        turtles = new_pointer
        list_turtles.append(turtles)
    a = 0
    for turtles in list_turtles:
        new_position = []
        turtles.penup()
        turtles.goto(x=-230, y=-150 + a)
        a += 60
        new_position += turtles.pos()
        position.append(new_position)
while is_race_on:
    for turtle in list_turtles:
        index = list_turtles.index(turtle)
        if turtle.xcor() < 230:
            turtle.forward(random.randint(0, 35))
        else:
            winner = turtle
            if user_bet == winner.name:
                print(f"You WON!!! the winner is: {turtle.name}")
            else:
                print(f"You lost, the winner is: {turtle.name}")
            is_race_on = False


screen.exitonclick()