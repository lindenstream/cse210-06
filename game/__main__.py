import constants

from casting.cast import Cast
from casting.score import Score
from casting.IBlock import IBlock
from casting.JBlock import JBlock
from casting.LBlock import LBlock
from casting.OBlock import OBlock
from casting.SBlock import SBlock
from casting.TBlock import TBlock
from casting.ZBlock import ZBlock
from scripting.script import Script
from scripting.control_actors_action import ControlActorsAction
from scripting.move_actors_action import MoveActorsAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.draw_actors_action import DrawActorsAction
from directing.director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("IBlock", IBlock())
    cast.add_actor("JBlock", JBlock())
    cast.add_actor("LBlock", LBlock())
    cast.add_actor("OBlock", OBlock())
    cast.add_actor("SBlock", SBlock())
    cast.add_actor("TBlock", TBlock())
    cast.add_actor("ZBlock", ZBlock())

    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()