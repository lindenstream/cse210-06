import constants
from casting.actor import Actor
from casting.piece import Piece
from shared.point import Point


class TBlock(Piece):
    """
    A single T-shaped piece.
    
    The responsibility of TBlock is to create a T-shaped piece.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self._blocks = []
        self._prepare_piece()

    def _prepare_piece(self):
        # prepares the center block location
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y)

        # prepare the rest of the blocks
        for i in range(constants.NUMBER_BLOCKS):
            if i == 0:
                position = Point(x - constants.CELL_SIZE, y)
            elif i == 1:
                position = Point(x, y)
            elif i == 2:
                position = Point(x + constants.CELL_SIZE, y)
            elif i == 3:
                position = Point(x, y + constants.CELL_SIZE)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "■"
            color = constants.TEAL
            
            block = Actor()
            block.set_position(position)
            block.set_velocity(velocity)
            block.set_text(text)
            block.set_color(color)
            self._blocks.append(block)