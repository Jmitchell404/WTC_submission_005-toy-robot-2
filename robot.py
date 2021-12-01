import os
import sys
dirc = ['forward', 'right', 'back', 'left']
x = 0
y = 0
current_rotation = "forward"
min_y, max_y = -201, 201
min_x, max_x = -101, 101
# rotation_var =-1
# position= ({'x':0, 'y':1})
def robot_start():
    """This is the entry function, do not change"""
    robot_name = input("What do you want to name your robot? ")
    print(robot_name + ": Hello kiddo!" )
    commands(robot_name)
    return robot_name


def commands(robot_name):
    global x,y
    answer = input(robot_name + ": What must I do next? ").lower()
    if answer == "off":
        print(robot_name + ": Shutting down..")
        return

    elif answer == "help":
        print("""I can understand these commands:
 OFF - Shut down robot
 HELP - provide information about commands
 RIGHT - Puts the robot in a 90 angle to the right.
 LEFT - Puts the robot in a 90 angle to the left.
""")
        robot_move(robot_name, answer)
        commands(robot_name)
    elif "forward" in answer or "back" in answer:
        # print(f" > {robot_name} moved forward by  steps.")
        robot_move(robot_name, answer)
        return commands(robot_name)

    elif "right" in answer or "left" in answer:
        robot_move(robot_name, answer)
        print(f" > {robot_name} turned {answer}.")
        print(f" > {robot_name} now at position ({x},{y}).")
        #robot_left_or_right(answer, robot_name)
        return commands(robot_name)
    else:
        print(f"{robot_name}: Sorry, I did not understand '{answer.upper}'.")
        return commands(robot_name)
    return commands(robot_name)


def move_forward(input_from_user, robot_name, dirc, x, y):
    """
    since the robot moves on a cartesian plane, x is for x-axis and y is for y-axis
    the instruction(command) and steps(value) is stored in a tuple named stored_movements
    stored_movements will then determine the direction and number of steps the robot should move
    """
    oldy = y
    oldx = x
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    stored_movements = (instruction, steps) 
    if dirc == 1:
        y = oldy + int(steps)
        if y in range(-200, 200):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    elif dirc == 0 or dirc== 4:
        x = oldx - int(steps)
        if x in range(-100,100):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    elif dirc == 2 or dirc == -2:
        x = oldx + int(steps)
        if x in range(-100, 100):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    elif dirc == -1 or dirc == 3:
        y = oldy - int(steps)
        if y in range(-200, 200):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    return x, y, dirc, instruction, oldx, oldy


def move_backward(input_from_user, robot_name, dirc, x, y):
    """
    since the robot moves on a cartesian plane, x is for x-axis and y is for y-axis
    the instruction(command) and steps(value) is stored in a tuple named same
    same will then determine the direction and number of steps the robot should move
    """
    oldy = y
    oldx = x
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    stored_movements = (instruction, steps)
    if dirc == 1:
        y = y - int(steps)
        print(" > {} moved back by {} steps.".format(robot_name, steps))
    elif dirc == 0 or dirc == 4:
        x = x + int(steps)
        print(" > {} moved back by {} steps.".format(robot_name, steps))
    elif dirc == 2 or dirc == -2:
        x = x - int(steps)
        print(" > {} moved back by {} steps.".format(robot_name, steps))
    elif dirc == -1 or dirc== 3:
        y = y + int(steps)
        print(" > {} moved back by {} steps".format(robot_name, steps))
    return x, y, dirc, instruction, oldx, oldy


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(x)+','+str(y)+').')

# def robot_left_or_right(answer, robot_name):
#     global current_rotation
#     current_rotation == 
def is_position_allowed(new_x, new_y):
    global min_y,min_x
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def keep_track_of_sprint(input_from_user, x, y, name, direction, steps):
    """
    the value will decrease by one until it reaches one
    it will take one less step forward
    """
    if steps > 0:
        input_from_user = f"sprint {steps}"
        x, y, direction = robot_move(input_from_user, name, direction, x, y)
        steps = steps - 1
        return keep_track_of_sprint(input_from_user, x, y, name, direction, steps)
    else:
        return x,y


def keep_track_of_position(x, y,robot_name, direction):
    """
    this function soley focuses on the position of the robot
    current position is stored and a print statement will be printed
    otherwise
    (since the robot is allowed to move within certain parameters)
    if the robots future position is outside the boundries, it does not move and
    will notify the user
    """
    if x > -101 and x < 101 and y > -201 and y < 201:
        print(" > {} now at position ({},{}).".format(robot_name, x, y))  
    else:
        print("{}: Sorry, I cannot go outside my safe zone.".format(robot_name))
        print(f" > {robot_name} now at position ({x},{y}).")
        return x, y, direction


def direction_left(direction, robot_name, x, y):
    """
    anti-clockwise 
    """
    direction = direction - 1
    if direction < -2:
        direction = 1
    print(f" > {robot_name} turned left.")
    print(" > {} now at position ({},{}).".format(robot_name, x, y))
    return direction


def direction_right(direction, robot_name, x, y):
    """
    clockwise
    x - position on the x-axis
    y - position on the y-axis
    """
    direction = direction + 1
    if direction > 4:
        direction = 1
    print(f" > {robot_name} turned right.")
    print(" > {} now at position ({},{}).".format(robot_name, x, y))
    return direction


def robot_move(robot_name, answer):
    answer = answer.split()
    global x, y
    if current_rotation == "forward":
        if answer[0] == "forward":
            y = y + int(answer[1])
        if answer[0] == "back":
            y = y - int(answer[1])
    elif current_rotation == "back":
        if answer[0] == "forward":
            y = y - int(answer[1])
        if answer[0] == "back":
            y = y + int(answer[1])
    elif current_rotation == "left":
        if answer[0] == "forward":
            x = x - int(answer[1])
        if answer[0] == "back":
            x = x + int(answer[1])
    elif current_rotation == "right":
        if answer[0] == "forward":
            x = x + int(answer[1])
        if answer[0] == "back":
            x = x - int(answer[1])
    print(f" > {robot_name} moved {answer[0]} by {answer[1]} steps.")
    print(f" > {robot_name} now at position ({x},{y}).")


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_rotation

    current_rotation += 1
    if current_rotation > 4:
        current_rotation = 0

    return True, ' > '+robot_name+' turned right.'


def direction_left(robot_name, x, y):
    """
    anti-clockwise 
    """
    global current_rotation
    current_rotation = current_rotation - 1
    if current_rotation < -4:
        current_rotation = 1
    print(f" > {robot_name} turned left.")
    print(" > {} now at position ({},{}).".format(robot_name, x, y))
    return current_rotation


def direction_right(robot_name, x, y):
    """
    clockwise
    x - position on the x-axis
    y - position on the y-axis
    """
    global current_rotation
    current_rotation = current_rotation + 1
    if current_rotation > 4:
        current_rotation = 1
    print(f" > {robot_name} turned right.")
    print(" > {} now at position ({},{}).".format(robot_name, x, y))
    return current_rotation


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_rotation

    current_rotation -= 1
    if current_rotation < 0:
        current_rotation = 3

    return True, ' > '+robot_name+' turned left.'


# def do_sprint(robot_name, steps):
#     """
#     Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
#     :param robot_name:
#     :param steps:
#     :return: (True, forward output)
#     """

#     if steps == 1:
#         return forward(robot_name, 1)
#     else:
#         (do_next, command_output) = do_forward(robot_name, steps)
#         print(command_output)
#         return do_sprint(robot_name, steps - 1)


# def robot_left_or_right(answer,robot_name):
#     answer = answer.split()
#     global x, y
#     if answer[0] == "left":
#         x = x -int(answer[0])
#     if answer[0] == "right":
#         x = x +int(answer[0])
#     print(f" > {robot_name} moved {answer[0]} by {answer[1]} steps.")
#     print(f" > {robot_name} now at position ({x},{y}).")


#def forward_tracing():

# def robot_directions(answer):
#     if answer == 

# def gets_commands(robot_name,answer):
#     # arr_cmd=line.split()
#     # command=arr_cmd[0]
#     answer = answer.split()
#     global x,y
#     if (answer=='left'):
#         x = x + int(answer[0])
#         print(f" > {robot_name} moved {answer[0]} by {answer[1]} steps.")
#         print(f" > {robot_name} now at position ({x},{y}).")
if __name__ == "__main__":
    robot_start()
