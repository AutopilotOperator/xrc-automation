from simple_pid import PID

pidy = PID(1.6, 0, 0.33, output_limits=(-1, 1), sample_time=0.016)
pidx = PID(1.9, 0, 0.33, output_limits=(-1, 1), sample_time=0.016)
pidAngle = PID(0.039, 0, 0.01, output_limits=(-1, 1), sample_time=0.016)


def get_important_robot_data(robot):
    RPos = robot['myrobot'][1]['global pos']
    RAngle = robot['myrobot'][1]['global rot']
    return {'x': RPos[0], 'y': RPos[2], 'angle': RAngle[1]}


def get_input_from_wanted_coords(coords, robot):
    """
    returns controls for base drive
    :param coords: where you want the robot to go {'x':x,'y':y,'angle':angle}
    :param robot: the robot object
    """
    curr = get_important_robot_data(robot)
    controls = {'left_y': power_from_curr_and_target(curr['y'], coords['y'], pidy) * -1,
                'left_x': power_from_curr_and_target(curr['x'], coords['x'], pidx),
                'right_x': power_from_curr_and_target(curr['angle'], coords['angle'], pidAngle)}
    done = abs(curr['x'] - coords['x']) < 0.05 and abs(curr['y'] - coords['y']) < 0.05 and abs(
        controls['left_x']) < 0.1 and abs(controls['left_y']) < 0.1 and abs(
        curr['angle'] - coords['angle']) < 2 and abs(controls['right_x']) < 0.3  # Close to the target and slowed down
    return controls, done


def power_from_curr_and_target(curr, target, pid):
    pid.setpoint = target
    return pid(curr)
