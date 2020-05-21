from piece import Piece
from location import Location


class HistoryItem:

    def __init__(self, piece, from_location, to_location):
        self.piece = piece
        self.from_location = from_location
        self.to_location = to_location
