from turtle import Turtle,Screen
import random

is_race_on = False
Screen = Screen()
Screen.bgcolor("green")
Screen.setup(500,400)
user_bet = Screen.textinput("make your bet","enter your fav color!")
colors = ["red","blue","orange","black","purple","yellow"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is Winner.")
            else:
                print(f"You'Lost! The {winning_color} turtle is winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)