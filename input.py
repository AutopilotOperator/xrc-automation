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


    if keyboard.is_pressed('+'):
        input_map['trigger_l'] = -1
    elif keyboard.is_pressed('-'):
        input_map['trigger_l'] = 1
    else:
        input_map['trigger_l'] = 0


    if keyboard.is_pressed('-'):
        input_map['trigger_r'] = -1
    elif keyboard.is_pressed('+'):
        input_map['trigger_r'] = 1
    else:
        input_map['trigger_r'] = 0
        

    # if keyboard.is_pressed('+'):
    #     input_map['trigger_l'] = 1

    # if keyboard.is_pressed('-'):
    #     input_map['trigger_r'] = 1




    if keyboard.is_pressed('e'):
        input_map['right_x'] = -1
    elif keyboard.is_pressed('q'):
        input_map['right_x'] = 1
    else:
        input_map['right_x'] = 0

    # if keyboard.is_pressed('num 8'):
    #     input_map['dpad_up'] = 1

    # if keyboard.is_pressed('num 2'):
    #     input_map['dpad_down'] = 1

    # if keyboard.is_pressed('num 4'):
    #     input_map['dpad_left'] = 1

    # if keyboard.is_pressed('num 6'):
    #     input_map['dpad_right'] = 1       



    # for event in pygame.event.get():
    #         if event.type == pygame.JOYBUTTONDOWN:
    #             if event.button == 3:
    #                 input_map['y'] = 1
    #             if event.button == 2:
    #                 ButX = True
    #                 input_map['x'] = 1
    #             if event.button == 1:
    #                 ButB = True
    #                 input_map['b'] = 1
    #             if event.button == 0:
    #                 ButA = True
    #                 input_map['a'] = 1
    #             if event.button == 4:
    #                 BL = True
    #                 input_map['bumper_left'] = 1
    #             if event.button == 5:
    #                 BR = True
    #                 input_map['bumper_right'] = 1
    #             if event.button == 6:
    #                 ButR = True
    #                 input_map['r'] = 1
    #         if event.type == pygame.JOYBUTTONUP:
    #             if event.button == 3:
    #                 ButY = False
    #                 input_map['y'] = 0
    #             if event.button == 2:
    #                 ButX = False
    #                 input_map['x'] = 0
    #             if event.button == 1:
    #                 ButB = False
    #                 input_map['b'] = 0
    #             if event.button == 0:
    #                 ButA = False
    #                 input_map['a'] = 0
    #             if event.button == 4:
    #                 BL = False
    #                 input_map['bumper_left'] = 0
    #             if event.button == 5:
    #                 BR = False
    #                 input_map['bumper_right'] = 0
    #             if event.button == 6:
    #                 ButR = False
    #                 input_map['r'] = 0
    #         if event.type == pygame.JOYAXISMOTION:
    #             if event.axis == 0:
    #                 XMov = event.value
    #                 input_map['left_x'] = event.value
    #                 if(abs(event.value) < 0.1):
    #                     XMov = 0
    #                     input_map['left_x'] = 0

    #             if event.axis == 1:
    #                 YMov = event.value
    #                 input_map['left_y'] = event.value
    #                 if(abs(event.value) < 0.1):
    #                     YMov = 0
    #                     input_map['left_y'] = 0
    #             if event.axis == 2:
    #                 Turn = event.value * .7
    #                 input_map['right_x'] = event.value * 0.7
    #                 if(abs(event.value) < 0.1):
    #                     Turn = 0
    #                     input_map['left_x'] = 0

    #             if event.axis == 4:
    #                 if(event.value > 0.2):
    #                     TrigL = True
    #                     input_map['trigger_l'] = 1

    #                 else:
    #                     TrigL = False
    #                     input_map['trigger_l'] = 0
    #             if event.axis == 5:
    #                 if(event.value > 0.2):
    #                     TrigR = True
    #                     input_map['trigger_r'] = 1
    #                 else:
    #                     TrigR = False
    #                     input_map['trigger_r'] = 0
    # # print(input_map)
    return input_map