import autos.nathanTimeThing as nathan
import autos.eyalTest as eyal

auto = "eyal"


def auto_main(time, robot, game_state, game_elements):
    match auto:
        case "nathanTime":
            return nathan.get_auto_input(time)
        case "eyal":
            return eyal.get_auto_input(time, robot)
        case _:
            return {}