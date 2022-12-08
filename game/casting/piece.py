import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Piece(Actor):
    """
    A falling piece in the game.
    
    The responsibility of the piece is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._blocks = []
        self._prepare_piece()
        # self.win = False

    def get_blocks(self):
        # returns blocks in the piece
        return self._blocks

    def move_next(self):
        # move all blocks
        for block in self._blocks:
            block.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_center_block(self):
        # returns center block
        return len(self._blocks) // 2

    # def build_piece(self, number_of_blocks):
    #     # builds the piece
    #     for i in range(number_of_blocks):
    #         tail = self._blocks[-1]
    #         velocity = tail.get_velocity()
    #         offset = velocity.reverse()
    #         position = tail.get_position().add(offset)
            
    #         block = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text("■")
    #         segment.set_color(constants.YELLOW)
    #         self._blocks.append(block)

    def move_piece(self, velocity):
        # moves the piece
        self._blocks[self.get_center_block()].set_rotation(velocity)

    # need a rotation method?
    
    def _prepare_piece(self):
        # prepares the center block location
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y)

        # prepare the rest of the blocks
        for i in range(constants.NUMBER_BLOCKS):
            if i == 1:
                position = Point(x - i * constants.CELL_SIZE, y)
            elif i == 2:
                position = Point(x - i * constants.CELL_SIZE, y)
            elif i == 3:
                position = Point(x - i * constants.CELL_SIZE, y)
            elif i == 4:
                position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "■"
            color = constants.YELLOW
            
            block = Actor()
            block.set_position(position)
            block.set_velocity(velocity)
            block.set_text(text)
            block.set_color(color)
            self._blocks.append(block)

    def won_game(self):
        
        pass
        # returns win Boolean
        # return self.win

    def set_win(self, bool):

        pass
        # sets win boolean
        # self.win = bool