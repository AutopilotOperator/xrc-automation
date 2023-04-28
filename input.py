import pygame
import keyboard

def map_user_input():
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
        




    if keyboard.is_pressed('e'):
        input_map['right_x'] = -1
    elif keyboard.is_pressed('q'):
        input_map['right_x'] = 1
    else:
        input_map['right_x'] = 0

    
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




