from autos import helper

auto_index = 0
auto_ended = True
auto_config = [
    {'location': {'x': -3.12, 'y': -1.67, 'angle': 270},
     'controls': {'trigger_r': -1, 'trigger_l': 1}},  # Goes to pick up the left cube
    {'location': {'x': -2.93, 'y': -6.36, 'angle': 90},
     'controls': {'trigger_l': 0, 'dpad_right': 1}},  # Goes to put the cube
    {'location': {'x': -2.93, 'y': -6.321, 'angle': 90},
     'controls': {'a': 1}},  # One loop cycle to release the cube
    {'location': {'x': -1.1, 'y': -4.5, 'angle': 90},
     'controls': {'dpad_right': 0, 'dpad_down': 1}}  # Lower center of gravity and climbs

]


def get_auto_input(time_left, robot):
    """
    The main logic for auto
    :param time_left: How many milliseconds left
    :param robot: State of the robot
    :return: Joystick controls for the robot
    """
    global auto_ended
    global auto_index

    if time_left > 149998:
        # auto.reset()
        auto_ended = False
        auto_index = 0

    if auto_ended:
        return {}
    if auto_index >= len(auto_config):
        return {'left_x': 0, 'left_y': 0, 'right_x': 0}

    controls, finished_step = helper.get_input_from_wanted_coords(auto_config[auto_index]['location'], robot)
    controls = {**controls, **auto_config[auto_index]['controls']}
    if finished_step:
        auto_index += 1

    return controls
