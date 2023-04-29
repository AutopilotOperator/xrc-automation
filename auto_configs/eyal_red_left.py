auto_config = [
    {'timeout':200},
    {'location': {'x': -3.132, 'y': -1.747, 'angle': 270},  # go to cube
     'controls': {'trigger_r': -1, 'trigger_l': 1}},  # Goes to pick up the left cube
    {'controls': {'left_y':-0.17},
     'timeout': 300},
    {'location': {'x': -2.93, 'y': -6.36, 'angle': 90},  # go to grid
     'controls': {'trigger_l': 0 ,'trigger_r':0, 'dpad_down': 1, 'dpad_up': 0, 'dpad_left': 0, 'dpad_right': 0},
     'timeout': 1500},
    {'location': {'x': -2.93, 'y': -6.36, 'angle': 90, 'precise': False},
     'controls': {'dpad_left': 0,'dpad_up': 0, 'dpad_down': 0, 'dpad_right': 1}},  # go to grid
    {'controls': {'left_x':0,'left_y':0,'right_x':0, 'dpad_right':0},
     'timeout':100},
    {'controls': {'a': 1},  # One loop cycle to release the cube
     'timeout': 1000},

    {'location': {'x': -3.147, 'y': -5.89, 'angle': 150, 'precise': False},
     'controls': {'dpad_down': 1, 'a':0}},

    {'location': {'x': -3.19, 'y': -2.85, 'angle': 240, 'precise': False},
     'controls': {'dpad_down': 0}},

    {'location': {'x': -1.847, 'y': -1.93, 'angle': 270},  # go to cone
     'controls': {'trigger_r': -1, 'trigger_l': 1}},

    {'controls': {'left_y':-0.15,'trigger_r': 0, 'trigger_l': 0},
     'timeout': 500},

    {'location': {'x': -1.1, 'y': -4.52, 'angle': 90},
     'controls': {'dpad_down': 1}}  # Lower center of gravity and climbs
]
