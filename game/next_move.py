from pieces.piece import Piece
from pieces.location import Location


class NextMove:

    def __init__(self, piece, current_location, moves):
        self.piece = piece
        self.current_location = current_location
        self.moves = moves

    def __str__(self):
        return "{} @ {} -> {}".format(self.piece, self.current_location, self.moves)

    def __repr__(self):
        return self.__str__()
