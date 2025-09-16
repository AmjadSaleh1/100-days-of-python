def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def go_down():
    turn_right()
    move()
    turn_left()


def start():
    jump()
    move()
    go_down()


while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()