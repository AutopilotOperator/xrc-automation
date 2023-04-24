import keyboard
import math as m
import json
import time
import utils
import input
import pygame

pygame.init()


Turn = 0
YMov = 0
xMov = 0


Key = True


current_direction = ""

joysticks = []

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick "),joysticks[-1].get_name(),"'"
    Controller = True

while True:
    start = time.time()
    Rbot = open('myRobot.txt', 'rt')
    Gme = open('GameElements.txt', 'rt')
    # Output = open('Controls.txt', 'r')
    # # print(Output.read())
    # Output.close()
    try:
        Robot = json.load(Rbot)
        Game = json.load(Gme)
        
    except:
        continue

    Controls = open('Controls.txt', 'w')

    #grabs positions
    # print(Robot['myrobot'][0])
    # print('Is it working?')
    RPos = Robot['myrobot'][1]['global pos']
    RVol = Robot['myrobot'][1]['velocity']
    RAngle = Robot['myrobot'][1]['global rot']
    RRotV = Robot['myrobot'][1]['rot velocity']

    
    '''
    #Writes to the controls text file
    Controls.write()
    '''
    input_map = input.map_user_input()
    if input_map == {}: continue

    control_str = utils.generate_control_input(**input_map)

    # print(control_str)
    Controls.write(control_str)


    # if (keyboard.is_pressed('w')):
    #     current_direction = '1'
    # if (keyboard.is_pressed('s')):
    #     current_direction = '-1'


    # Controls.write('left_y='+current_direction)
    #Prints for debugging

    if keyboard.is_pressed('`'):
        break

    #Keeps fps at 60
    time.sleep(max(1./60 - (time.time() - start), 0))
#cheat sheet
'''
a=0
b=0
x=0
y=0
dpad_left=0
dpad_right=0
bumper_l=0
bumper_r=0
stop=0
restart=0
right_y=0
right_x=0
left_y=0
left_x=0
trigger_l=0
trigger_r=0
'''