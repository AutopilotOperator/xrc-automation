import pygame
import keyboard


def map_user_input(joysticks, prev_value):
    if (joysticks == None or len(joysticks) == 0):
        return {}
    else:
        joystick = joysticks[0]
    # print(joystick.get_name())
    value = prev_value
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                value['a'] = 1
            if event.button == 1:
                value['b'] = 1
            if event.button == 2:
                value['x'] = 1
            if event.button == 3:
                value['y'] = 1
            if event.button == 4:
                value['bumper_l'] = 1
            if event.button == 5:
                value['bumper_r'] = 1
            if event.button == 6:
                value['restart'] = 1
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                value['a'] = 0
            if event.button == 1:
                value['b'] = 0
            if event.button == 2:
                value['x'] = 0
            if event.button == 3:
                value['y'] = 0
            if event.button == 4:
                value['bumper_l'] = 0
            if event.button == 5:
                value['bumper_r'] = 0
            if event.button == 6:
                value['restart'] = 0

        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                value['left_x'] = round(joystick.get_axis(0), 3)
            if event.axis == 1:
                value['left_y'] = round(joystick.get_axis(1), 3)
            if event.axis == 4:
                value['trigger_l'] = '1' if joystick.get_axis(4) > 0 else '0'
            if event.axis == 2:
                value['right_x'] = round(joystick.get_axis(2), 3)
            # if event.axis == 4:
            #     value['right_y'] = round(joystick.get_axis(4), 3)
            if event.axis == 5:
                value['trigger_r'] = '1' if joystick.get_axis(5) > 0 else '0'
            
        # if event.type in [pygame.JOYAXISMOTION, pygame.JOYBUTTONDOWN, pygame.JOYHATMOTION]:
        #     value ={
        #         "left_y": round(joystick.get_axis(1), 2),  # Left stick Y
        #         "left_x": round(joystick.get_axis(0), 2),  # Left stick X
        #         # "trigger_l": 1,  # Left Trigger 0 or 1 
        #         # "trigger_r": 0,  # Right Trigger (0 to 1)
        #         # "trigger_l": round((joystick.get_axis(4) + 1) / 2, 2),  # Left Trigger 0 or 1 
        #         # "trigger_r": round((joystick.get_axis(5) + 1) / 2, 2),  # Right Trigger (0 to 1)
        #         "trigger_r": '1' if joystick.get_axis(5) > 0 else '0',  # Left Trigger 0 or 1
        #         "trigger_l": '1' if joystick.get_axis(4) > 0 else '0',  # Left Trigger 0 or 1
        #         "right_x": round(joystick.get_axis(2), 2),  # Right stick X
        #         "x": joystick.get_button(2),  # X Button
        #         "dpad_down": int(joystick.get_hat(0)[1] == -1),
        #         "dpad_left": int(joystick.get_hat(0)[0] == -1),
        #         "dpad_up": int(joystick.get_hat(0)[1] == 1),
        #         "dpad_right": int(joystick.get_hat(0)[0] == 1),
        #         "a": joystick.get_button(0),  # A Button
        #         "y": joystick.get_button(3),  # Y Button
        #         "restart": joystick.get_button(6),  # Start Button
        #     }
    # print(f'{joystick.get_button(0)}' , end='\r')
    # print([joystick.get_axis(i) for i in range(joystick.get_numaxes())], end='\r')

  
    # for event in pygame.event.get():
    #     if event.type in [pygame.JOYAXISMOTION, pygame.JOYBUTTONDOWN, pygame.JOYHATMOTION]:
    #         axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
    #         buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
    #         hats = [joystick.get_hat(i) for i in range(joystick.get_numhats())]

    #         print(f"Axes: {axes}")
    #         print(f"Buttons: {buttons}")
    #         print(f"Hats: {hats}")




    return value
    input_map = {}
    

    if keyboard.is_pressed('w'):
        input_map['left_y'] = -1
    elif keyboard.is_pressed('s'):
        input_map['left_y'] = 1
    else:
        input_map['left_y'] = 0

    if keyboard.is_pressed('a'):
        input_map['left_x'] = -1
    elif keyboard.is_pressed('d'):
        input_map['left_x'] = 1
    else:
        input_map['left_x'] = 0


    if keyboard.is_pressed('-'):
        input_map['trigger_l'] = -1
    elif keyboard.is_pressed('+'):
        input_map['trigger_l'] = 1
    else:
        input_map['trigger_l'] = 0


    if keyboard.is_pressed('+'):
        input_map['trigger_r'] = -1
    elif keyboard.is_pressed('-'):
        input_map['trigger_r'] = 1
    else:
        input_map['trigger_r'] = 0
    

    if keyboard.is_pressed('k'):
        input_map['right_x'] = -1
    elif keyboard.is_pressed(';'):
        input_map['right_x'] = 1
    else:
        input_map['right_x'] = 0

    if keyboard.is_pressed('i'):
        input_map['x'] = 1
    else:
        input_map['x'] = 0
    
    def d_pad():
        if keyboard.is_pressed('up'):
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 1
            input_map['dpad_right'] = 0
            return
        else:
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 0
            


        if keyboard.is_pressed('down'):
            input_map['dpad_down'] = 1
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 0
            return
        else:
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 0

        if keyboard.is_pressed('left'):
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 1
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 0
            return
        else:
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 0

        if keyboard.is_pressed('right'):
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 1
            return
        else:
            input_map['dpad_down'] = 0
            input_map['dpad_left'] = 0
            input_map['dpad_up'] = 0
            input_map['dpad_right'] = 0
    d_pad()


    if keyboard.is_pressed('num 5'):
        input_map['a'] = 1
    else: 
        input_map['a'] = 0

    if keyboard.is_pressed('y'):
        input_map['y'] = 1
    else:
        input_map['y'] = 0

    return input_map




