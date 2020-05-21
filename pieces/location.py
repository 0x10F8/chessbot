class Location:

    def __init__(self, letter, number, take=False, take_piece=None, take_piece_location=None):
        self.letter = letter.lower()
        self.number = number
        self.take = take
        self.take_piece = take_piece
        self.take_piece_location = take_piece_location

    def __str__(self):
        location_string = "{}{}".format(self.letter, self.number)
        if self.take:
            location_string += " takes piece {} at location {}".format(
                self.take_piece.name, self.take_piece_location)
        return location_string

    def __repr__(self):
        return self.__str__()
