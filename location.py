class Location:

    def __init__(self, letter, number, take=False, take_piece=None, take_piece_location=None):
        self.letter = letter.lower()
        self.number = number
        self.take = take
        self.take_piece = take_piece
        self.take_piece_location = take_piece_location
