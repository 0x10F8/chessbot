class HistoryItem:

    def __init__(self, piece, from_location, to_location):
        self.piece = piece
        self.from_location = from_location
        self.to_location = to_location

    def __str__(self):
        return "{} {} from: {} to: {}".format(self.piece.colour,
                                              self.piece.name,
                                              self.from_location,
                                              self.to_location)
