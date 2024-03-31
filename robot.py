import input
import keyboard

class Robot:
    def __init__(self) -> None:
        self.pos =[0,0]
        self.rot = 0
        self.time_left = 0
        self.release_timeout = 0
        self.is_releasing = False



    def update_params(self, pos, rot, time_left):
        self.pos = pos
        self.rot = rot
        self.time_left = time_left


    def get_controls(self, pos, rot, time_left):
        self.update_params(pos, rot, time_left)
        user_input = input.map_user_input()
        user_input['x'] = 1 

        if keyboard.is_pressed('o') and self.is_releasing == False:
                self.is_releasing = True
                self.release_timeout = self.time_left - 500

        if self.is_releasing:
             user_input['x'] = 0
             if self.release_timeout < time_left:
                  self.is_releasing = False
        
    

        
        return user_input
        


    