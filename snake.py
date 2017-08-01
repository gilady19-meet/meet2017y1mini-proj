import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos= (x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)
    bodystamp  = snake.stamp()
    stamp_list.append(bodystamp)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 100

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    move_snake()
    print ("You pressed the up key!")

def left():
    global direction
    direction = LEFT
    move_snake()
    print ("You pressed the left key!")

def down():
    global direction
    direction = DOWN
    move_snake()
    print ("You pressed the down key!")

def right():
    global direction
    direction = RIGHT
    move_snake()
    print ("You pressed the  key!")

turtle.onkeypress(up, UP_ARROW)
