from simple_pid import PID

# pidy = PID(1.6, 0, 0.34, output_limits=(-1, 1), sample_time=0.016)
# pidx = PID(1.9, 0, 0.33, output_limits=(-1, 1), sample_time=0.016)
# pidAngle = PID(0.039, 0, 0.01, output_limits=(-1, 1), sample_time=0.016)
pidy = PID(1.6, 0, 0.34, output_limits=(-1, 1), sample_time=0.016, setpoint=0.0)
pidx = PID(1.9, 0, 0.33, output_limits=(-1, 1), sample_time=0.016, setpoint=0.0)
# pidAngle = PID(0.039, 0.00001, 0.01, output_limits=(-1, 1), sample_time=0.016, setpoint=0.0) # sort of works
# pidAngle = PID(-0.005,-0.0,-0.0, output_limits=(-1, 1), sample_time=0.016, setpoint=0.0) # 254 Base
pidAngle = PID(-0.004,-0.0,-0.0, output_limits=(-1, 1), sample_time=0.016, setpoint=0.0) 
def get_important_robot_data(robot):
    RPos = robot['myrobot'][1]['global pos']
    RAngle = robot['myrobot'][1]['global rot']
    return {'x': RPos[0], 'y': RPos[2], 'angle': RAngle[1]}


def get_move_list(targetArray, currentArray):
    xDistance = targetArray[0] - currentArray[0]
    yDistance = targetArray[1] - currentArray[1]

    a = targetArray[2] - currentArray[2]
    #print(a)
    b = targetArray[2] - currentArray[2] + 360
    #print(b)
    c = targetArray[2] - currentArray[2] - 360
    #print(c)
    if abs(a) < abs(b) and abs(a) < abs(c):
        rDistance = a
    elif abs(b) < abs(c):
        rDistance = b
    else:
        rDistance = c
    
    moveList = [xDistance,yDistance,rDistance]
    return moveList

def get_PID_output(move_list):
    rotation_movement = pidAngle(move_list[2])
    x_move = -pidx(move_list[0])
    y_move = pidy(move_list[1])
    return [x_move, y_move, rotation_movement]



def get_input_from_wanted_coords(coords, robot):
    """
    returns controls for base drive
    :param coords: where you want the robot to go {'x':x,'y':y,'angle':angle}
    :param robot: the robot object
    """
    precise = True
    if 'precise' in coords:
        precise = coords['precise']
    curr = get_important_robot_data(robot)


    move_list = get_move_list([coords['x'], coords['y'], coords['angle']], [curr['x'], curr['y'], curr['angle']])
    move_list = get_PID_output(move_list)
    # # print(curr, flush=True)
    # controls = {'left_y': power_from_curr_and_target(curr['y'], coords['y'], pidy) * -1 ,
    #             'left_x': power_from_curr_and_target(curr['x'], coords['x'], pidx) ,
    #             'right_x': power_from_curr_and_target(curr['angle'], coords['angle'], pidAngle)}
    # print(controls, flush=True)

    controls = {
        'left_y': move_list[1],
        'left_x': move_list[0],
        'right_x': move_list[2]
    }

    if precise:
        done = abs(curr['x'] - coords['x']) < 0.05 and abs(curr['y'] - coords['y']) < 0.05 and abs(
            controls['left_x']) < 0.1 and abs(controls['left_y']) < 0.1 and abs(
            curr['angle'] - coords['angle']) < 2 and abs(
            controls['right_x']) < 0.2  # Close to the target and slowed down
    else:
        done = abs(curr['x'] - coords['x']) < 0.9 and abs(curr['y'] - coords['y']) < 0.9 and abs(
            curr['angle'] - coords['angle']) < 10  # Somewhat on target
    return controls, done


def power_from_curr_and_target(curr, target, pid):
    pid.setpoint = target
    return pid(curr) 
