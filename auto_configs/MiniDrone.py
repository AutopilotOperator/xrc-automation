# from consts import HIGH_SCORING_POS, INTAKE_POS, LOWER_ELEVATOR
import robot_consts


auto_config = [
    {'timeout': 400},
    # {'location': {'x': 0.583, 'y': -1.929, 'angle': 270}, 'controls':  robot_consts.LOWER_ELEVATOR},

    {'location': {'x': 0.2905831, 'y': -7.401, 'angle': 30.85,}, 'controls':  robot_consts.CHARGE_SHOOTER},
    {'timeout': 200, 'controls': robot_consts.RELEASE_SHOOTER},
    {'location': {'x': -0.08995557, 'y': -6.258238, 'angle': 270}},
    {'location': {'x': -0.08995557, 'y': -5.858238, 'angle': 270}},
    {'location': {'x': 1.3, 'y': -6.86, 'angle': 90.23537}, 'controls':  robot_consts.CHARGE_SHOOTER},
    {'timeout': 500, 'controls': robot_consts.RELEASE_SHOOTER},
    {'location': {'x': 1.376801, 'y': -6.023902, 'angle': 270}, 'controls':  robot_consts.CHARGE_SHOOTER},
    {'location': {'x': 1.376801, 'y': -5.923902, 'angle': 270}, 'controls':  robot_consts.CHARGE_SHOOTER},
    {'location': {'x': 1.376801, 'y': -5.923902, 'angle': 270}, 'controls':  robot_consts.CHARGE_SHOOTER},
    {'location': {'x': 1.3, 'y': -6.86, 'angle': 90.23537}, 'controls':  robot_consts.CHARGE_SHOOTER},
    {'timeout': 500, 'controls': robot_consts.RELEASE_SHOOTER},
    # {'location': {'x': 1.509, 'y': -6.813, 'angle': 0}, 'controls':  robot_consts.CHARGE_SHOOTER},
    # {'timeout': 100, 'controls': robot_consts.INTAKE_POS | robot_consts.STOP_ELEVATOR },
    
]


