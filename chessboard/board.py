from chessboard.move_history import HistoryItem


class Board:

    letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    numbers = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}

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
        self.move_history = []

    def get_piece_at_square(self, location):
        location_x_array = self.letters[location.letter]
        location_y_array = self.numbers[location.number]
        return self.squares[location_x_array][location_y_array]

    def move_piece(self, piece, from_location, to_location):
        history_item = HistoryItem(piece, from_location, to_location)
        if self.get_piece_at_square(from_location) is not piece:
            raise Exception("The location of the moving piece is incorrect.")
        if to_location.take:
            if self.get_piece_at_square(to_location.take_piece_location) \
                    is not to_location.take_piece:
                raise Exception(
                    "The take piece does not match the piece in that position.")
            else:
                self.__remove_piece__(to_location.take_piece_location)
        self.__remove_piece__(from_location)
        self.__add_piece__(piece, to_location)
        self.move_history.append(history_item)

    def __remove_piece__(self, location):
        location_x_array = self.letters[location.letter]
        location_y_array = self.numbers[location.number]
        if self.squares[location_x_array][location_y_array] is not None:
            piece_removed = self.squares[location_x_array][location_y_array]
            self.squares[location_x_array][location_y_array] = None
            return piece_removed
        else:
            raise Exception("There is no piece at this location.")

    def __add_piece__(self, piece, location):
        location_x_array = self.letters[location.letter]
        location_y_array = self.numbers[location.number]
        if self.squares[location_x_array][location_y_array] is not None:
            raise Exception("There is already a piece at this location")
        else:
            self.squares[location_x_array][location_y_array] = piece
