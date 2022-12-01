from game.casting.actor import Actor


class Score(Actor):
    """
    A time lapsed recorder. 
    
    The responsibility of Score is to keep track of the time elapsed

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._counter = 0
        self.add_counter(0)
        self._is_playing = True

    def add_counter(self, counter):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._counter += counter
        self.set_text(f"Timer: {self._counter}")

    def get_counter(self):
        """Returns the counter.
        
        """
        return self._counter

    def stop_counter(self):
        # sets the is_playing to False
        self._is_playing = False

    def is_playing(self):
        # returns is_playing status
        return self._is_playing
