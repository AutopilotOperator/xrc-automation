# import auto.nathanTimeThing as nathan
import auto.logic as eyal

auto = "nathan_red_left"




def auto_main(time, robot, game_state, game_elements):
    match auto:
        case "eyal_red_left":
            return eyal.get_auto_input(time, robot)
        
        case "nathan_red_left":
            return eyal.get_auto_input(time, robot)
        case _:
            return {}