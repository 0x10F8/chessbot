class Location:

    def __init__(self, letter, number,
                 take=False, take_piece=None, take_piece_location=None,
                 castle=False, castle_piece=None, castle_piece_location=None,
                 promotion=False, promotion_piece=None):
        self.letter = letter.lower()
        self.number = number
        self.take = take
        self.take_piece = take_piece
        self.take_piece_location = take_piece_location
        self.castle = castle
        self.castle_piece = castle_piece
        self.castle_piece_location = castle_piece_location
        self.promotion = promotion
        self.promotion_piece = promotion_piece

    def __str__(self):
        location_string = "{}{}".format(self.letter, self.number)
        if self.take:
            location_string += " takes piece {} at location {}".format(
                self.take_piece.name, self.take_piece_location)
        if self.castle:
            location_string += " castles piece {} at location {}".format(
                self.castle_piece.name, self.castle_piece_location)
        if self.promotion:
            location_string += " promotes to piece {}".format(
                self.promotion_piece.name)
        return location_string

    def __repr__(self):
        return self.__str__()

    def __eq__(self, compare):
        if isinstance(compare, Location):
            return self.letter == compare.letter and self.number == compare.number
        return False

    def __hash__(self):
        location_string = "{}{}".format(self.letter, self.number)
        return hash(location_string)
