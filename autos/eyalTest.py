from autos import helper

auto_index = 0
auto_ended = True
auto_config = [
    {'location': {'x': -3.132, 'y': -1.747, 'angle': 270},  # go to cube
     'controls': {'trigger_r': -1, 'trigger_l': 1}},  # Goes to pick up the left cube
    {'controls': {'left_y':-0.17},
     'timeout': 300},
    {'location': {'x': -2.93, 'y': -6.36, 'angle': 90},  # go to grid
     'controls': {'trigger_l': 0, 'dpad_down': 1},
     'timeout': 1500},
    {'location': {'x': -2.93, 'y': -6.36, 'angle': 90},
     'controls': {'trigger_l': 0, 'dpad_right': 1}},  # go to grid
    {'controls': {'a': 1, 'left_x':0,'left_y':0,'right_x':0},  # One loop cycle to release the cube
     'timeout': 100},

    {'location': {'x': -3.147, 'y': -5.89, 'angle': 150, 'precise': False},
     'controls': {'dpad_down': 1,'dpad_right':0}},

    {'location': {'x': -3.19, 'y': -2.85, 'angle': 240, 'precise': False},
     'controls': {'dpad_down': 1,'dpad_right':0, 'a': 0}},

    {'location': {'x': -1.847, 'y': -1.93, 'angle': 270},  # go to cone
     'controls': {'trigger_r': -1, 'trigger_l': 1}},

    {'controls': {'left_y':-0.15},
     'timeout': 500},

    {'location': {'x': -1.1, 'y': -4.52, 'angle': 90},
     'controls': {'trigger_r': 0, 'trigger_l': 0, 'dpad_down': 1}}  # Lower center of gravity and climbs

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
    # print('\rauto index=%s' % (auto_index), end='', flush=True)
    if time_left > 149998:
        # auto.reset()
        auto_ended = False
        auto_index = 0

    if auto_ended:
        return {}
    if auto_index >= len(auto_config):
        return {'left_x': 0, 'left_y': 0, 'right_x': 0}

    finished_step = False
    controls_output = {}
    if 'controls' in auto_config[auto_index]:
        controls_output = {**controls_output, **auto_config[auto_index]['controls']}
    if 'location' in auto_config[auto_index]:
        controls, finished_step = helper.get_input_from_wanted_coords(auto_config[auto_index]['location'], robot)
        controls_output = {**controls, **controls_output}
    if finished_step:
        auto_index += 1

    elif 'timeout' in auto_config[auto_index]:
        if 'start_time' not in auto_config[auto_index]:
            auto_config[auto_index]['start_time'] = time_left
        if auto_config[auto_index]['start_time'] - time_left > auto_config[auto_index]['timeout']:
            auto_index += 1

    return controls_output
