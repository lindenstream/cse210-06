from casting.actor import Actor


class Score(Actor):
    """
    A score keeper. 
    
    The responsibility of Score is to keep track of the game score

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        self._is_playing = True

    def add_points(self, added_points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += added_points
        self.set_text(f"Score: {self._points}")

    def get_score(self):
        """Returns the score.
        
        """
        return self._points

    # def stop_counter(self):
    #     # sets the is_playing to False
    #     self._is_playing = False

    def is_playing(self):
        # returns is_playing status
        return self._is_playing
