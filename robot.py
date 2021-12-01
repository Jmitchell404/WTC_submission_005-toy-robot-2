def name_the_robot():
    """
    name of the robot is asked
    name is stored and returned
    """
    robot_name = input("What do you want to name your robot? ")
    print(robot_name + ": Hello kiddo!")
    return robot_name


def get_command_input(robot_name):
    """
    print statement asking user what the robot will do next appears
    user input coverted into casefold and returned
    """
    user_input =  input(f"{robot_name}: What must I do next? ")
    new_input = user_input.casefold()
    return new_input, user_input


def moving_forward(input_from_user, robot_name, direction, x, y):
    """
    x is for x-axis and y is for y-axis
    the instruction(command) and steps(value) is stored in a tuple named same
    same will then determine the direction and number of steps the robot should move
    """
    oldy = y
    oldx = x
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    same = (instruction, steps) 
    if direction == 1:
        y = oldy + int(steps)
        if y in range(-200, 200):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    elif direction == 0 or direction == 4:
        x = oldx - int(steps)
        if x in range(-100,100):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    elif direction == 2 or direction == -2:
        x = oldx + int(steps)
        if x in range(-100, 100):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    elif direction == -1 or direction == 3:
        y = oldy - int(steps)
        if y in range(-200, 200):
            print(" > {} moved forward by {} steps.".format(robot_name, steps))
    return x, y, direction, instruction, oldx, oldy


def moving_backward(input_from_user, robot_name, direction, x, y):
    """
    x is for x-axis and y is for y-axis
    the instruction(command) and steps(value) is stored in a tuple named same
    same will then determine the direction and number of steps the robot should move
    """
    oldy = y
    oldx = x
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    same = (instruction, steps)
    if direction == 1:
        y = y - int(steps)
        print(" > {} moved back by {} steps.".format(robot_name, steps))
    elif direction == 0 or direction == 4:
        x = x + int(steps)
        print(" > {} moved back by {} steps.".format(robot_name, steps))
    elif direction == 2 or direction == -2:
        x = x - int(steps)
        print(" > {} moved back by {} steps.".format(robot_name, steps))
    elif direction == -1 or direction == 3:
        y = y + int(steps)
        print(" > {} moved back by {} steps".format(robot_name, steps))
    return x, y, direction, instruction, oldx, oldy


def keep_track_of_position(x, y, steps, robot_name, direction, oldx, oldy):
    """
    this function soley focuses on the position of the robot
    current position is stored and a print statement will be printed
    otherwise
    """
    if x > -101 and x < 101 and y > -201 and y < 201:
        print(" > {} now at position ({},{}).".format(robot_name, x, y))  
    else:
        print("{}: Sorry, I cannot go outside my safe zone.".format(robot_name))
        print(f" > {robot_name} now at position ({oldx},{oldy}).")
        return oldx, oldy, direction
    return x, y, direction


def keep_track_of_sprint(input_from_user, x, y, robot_name, direction, steps):
    """
    the value will decrease by one until it reaches one
    it will take one less step forward
    """
    if steps > 0:
        input_from_user = f"sprint {steps}"
        x, y, direction, instruction, oldx, oldy = \
        moving_forward(input_from_user, robot_name, direction, x, y)
        steps = steps - 1
        return keep_track_of_sprint(input_from_user, x, y, robot_name, direction, steps)
    else:
        return x, y, input_from_user


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


def need_help():
    """
    when "help" is typed in by the user it will print out the help variable
    """
    help = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - in the direction that one is facing or travelling
BACK - in the direction that one is not facing or travelling
SPRINT - accelerates in the direction that one is not facing or travelling
LEFT - turns left
RIGHT - turns right"""

    print(help)
    return help


def off_command(robot_name):
    """
    when "off" is the user input, this function runs
    returns false to prevent it from running
    """
    print(f"{robot_name}: Shutting down..")
    return False


def invalid_command(user_input, robot_name):
    """
    as long as user input is not a valid command, the below will be printed
    """
    print(f"{robot_name}: Sorry, I did not understand '{user_input}'.")
    robot_start


def robot_start():
    """
    This is where the robot starts running
    a certain set of commands is laid
    Redirects the users input to the command
    """
    x = 0
    y = 0
    direction = 1

    commands = ["off", "help", "forward", "back", "right", "up", "left", "down", "sprint"]
    robot_on = True
    """
    as long as it is true, robot will continue running
    """
    robot_name = name_the_robot()
    while robot_on:
        """
        user input is split and searches for specific command
        """
        input_from_user, new_input = get_command_input(robot_name)
        cmd = input_from_user.split(" ")

        if "help" in input_from_user:
            need_help()
        elif "off" in input_from_user:
            robot_on = off_command(robot_name)
        elif "forward" == cmd[0] and cmd[1].isdigit():
            x, y, direction, instruction, oldx, oldy = \
            moving_forward(input_from_user, robot_name, direction, x, y )
            x, y, direction = \
            keep_track_of_position(x, y, int(cmd[1]), robot_name, direction, oldx, oldy)
        elif "back" == cmd[0] and cmd[1].isdigit():
            x, y , direction, instruction, oldx, oldy = \
            moving_backward(input_from_user, robot_name, direction, x, y )
            x, y, direction = \
            keep_track_of_position(x, y, int(cmd[1]), robot_name, direction, oldx, oldy)
        elif input_from_user == "left":
            direction = direction_left(direction, robot_name, x, y)
        elif input_from_user == "right":
            direction = direction_right(direction, robot_name, x, y)
        elif "sprint" in cmd and cmd[1].isdigit():
            x, y, input_from_user = \
            keep_track_of_sprint(input_from_user, x, y, robot_name, direction, int(cmd[1]))
            print(" > {} now at position ({},{}).".format(robot_name, x, y))
        else:
            invalid_command(new_input, robot_name)


if __name__ == "__main__":
    robot_start()