from auto import helper
from auto_configs import MiniDrone
auto_index = 0
auto_ended = True
auto_config =  MiniDrone.auto_config

def get_auto_input(time_left, robot):
    """
    The main logic for auto
    :param time_left: How many milliseconds left
    :param robot: State of the robot
    :return: Joystick controls for the robot
    """
    global auto_ended
    global auto_index
    print('\rauto index=%s' % (auto_index), end='', flush=True)
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
