from enum import Enum

class Colour(Enum):
    WHITE = "White"
    BLACK = "Black"

    def __str__(self):
        return self.name