auto_index = 0
auto_ended = True
auto_config = [
    {
        'end_timestamp': 14.0,
        'controls': {
            'left_x': 0.05
        }
    },

    {
        'end_timestamp': 12.5,
        'controls': {
            'left_y': -0.5
            
            # 'trigger_r': -1
        }
    },
    {
        'end_timestamp': 11.5,
        'controls': {
            'left_y': -0.5,
            'trigger_r': -1,
            'trigger_l': 1
        }
    },
    {
        'end_timestamp': 11.2,
        'controls': {
            'left_y': -0.2
        }
    },
    {
        'end_timestamp': 10.5,
        'controls': {
            'left_y': 0.5
        }

    }, 
]

# class Auto:
#     def __init__(self) -> None:
#         self.index = 0

#     def reset(self):
#         self.index = 0

# auto = Auto()
# auto.reset()


def get_auto_input(time_left):
    global auto_ended
    global auto_index

    if time_left > 149998:
        # auto.reset()
        auto_ended = False
        auto_index = 0

    if auto_ended:
        return {}

    if (auto_index >= len(auto_config)):
        return {}

    time_left = (time_left / 1000) - 135 #Starting from 1500 to 0

    if time_left < auto_config[auto_index]['end_timestamp']:
        auto_index += 1
        if (auto_index >= len(auto_config)):
            auto_ended = True
            return {}





    return auto_config[auto_index]['controls']

