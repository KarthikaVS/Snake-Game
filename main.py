from turtle import Turtle, Screen
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake")
screen.tracer(0)
current_direction = "right"

# default snake structuring
snake = [Turtle(), Turtle(), Turtle()]
positions = [(0, 0), (-20, 0), (-40, 0)]
for turtle in snake:
    index = snake.index(turtle)
    turtle.shape("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(positions[index])


# key events
def update_direction_as_up():
    global current_direction
    current_direction = "Up"


def update_direction_as_down():
    global current_direction
    current_direction = "Down"


def update_direction_as_left():
    global current_direction
    current_direction = "Left"


def update_direction_as_right():
    global current_direction
    current_direction = "Right"


screen.onkey(update_direction_as_up, "Up")
screen.onkey(update_direction_as_down, "Down")
screen.onkey(update_direction_as_left, "Left")
screen.onkey(update_direction_as_right, "Right")
screen.listen()


# update snake positions
def update_positions():
    for segment in snake:
        t_index = snake.index(segment)
        segment.setpos(positions[t_index])


# get updated snake head position with respect to the direction
def get_snake_head_position():
    head = positions[0]
    if current_direction.lower() == "right":
        return [(head[0] + 20, head[1])]
    elif current_direction.lower() == "left":
        return [(head[0] - 20, head[1])]
    elif current_direction.lower() == "up":
        return [(head[0], head[1] + 20)]
    elif current_direction.lower() == "down":
        return [(head[0], head[1] - 20)]

# snake moving
def move_turtle():
    global positions
    snake_head = get_snake_head_position()
    positions = snake_head + positions[:len(positions) - 1]
    print(positions)
    update_positions()


game_is_on = True
while game_is_on:
    move_turtle()
    screen.update()
    time.sleep(1)



screen.exitonclick()
