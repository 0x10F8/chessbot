class Board:

    letters = {'a': 0, 'b': 1, 'c': 2., 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    def __init__(self):
        self.squares = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]

    def __calculate_location_y_array_ref__(self, location_number):
        return (location_number-1)

    def remove_piece(self, location):
        location_x_array = self.letters[location.letter]
        location_y_array = self.__calculate_location_y_array_ref__(
            location.number)
        if self.squares[location_x_array][location_y_array] is not None:
            piece_removed = self.squares[location_x_array][location_y_array]
            self.squares[location_x_array][location_y_array] = None
            return piece_removed
        else:
            raise Exception("There is no piece at this location.")

    def add_piece(self, piece, location):
        location_x_array = self.letters[location.letter]
        location_y_array = self.__calculate_location_y_array_ref__(
            location.number)
        if self.squares[location_x_array][location_y_array] is not None:
            raise Exception("There is already a piece at this location")
        else:
            self.squares[location_x_array][location_y_array] = piece
