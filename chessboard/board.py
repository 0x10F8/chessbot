from chessboard.move_history import HistoryItem
from pieces.location import Location
from pieces.colour import Colour


class Board:

    letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    numbers = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}

    def clone(self):
        board = Board()
        [board.__add_piece__(piece.clone(), location) for location,
         piece in self.white_piece_locations.items()]
        [board.__add_piece__(piece.clone(), location) for location,
         piece in self.black_piece_locations.items()]
        return board

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
        self.white_piece_locations = {}
        self.black_piece_locations = {}
        self.white_king = (None, None)
        self.black_king = (None, None)

    def get_piece_at_square(self, location):
        location_y_array = self.letters[location.letter]
        location_x_array = self.numbers[location.number]
        return self.squares[location_x_array][location_y_array]

    def move_piece(self, piece, from_location, to_location):
        history_item = HistoryItem(piece, from_location, to_location)
        if self.get_piece_at_square(from_location) != piece:
            raise Exception("The location of the moving piece is incorrect.")
        if to_location.take:
            if self.get_piece_at_square(to_location.take_piece_location) \
                    != to_location.take_piece:
                raise Exception(
                    "The take piece does not match the piece in that position.")
            else:
                self.__remove_piece__(to_location.take_piece_location)
        if to_location.castle:
            if self.get_piece_at_square(to_location.castle_piece_location) \
                    != to_location.castle_piece:
                raise Exception(
                    "The castle piece does not match the piece in that position.")
            else:
                self.__remove_piece__(to_location.castle_piece_location)
                self.__add_piece__(to_location.castle_piece,
                                   self.__calculate_rook_castle_position__(to_location))
                to_location.castle_piece.moves_made += 1
        self.__remove_piece__(from_location)
        if to_location.promotion:
            self.__add_piece__(to_location.promotion_piece, to_location)
        else:
            self.__add_piece__(piece, to_location)
            piece.moves_made += 1
        self.move_history.append(history_item)

    def __calculate_rook_castle_position__(self, king_to_position):
        if king_to_position == Location('g', 1):
            return Location('f', 1)
        if king_to_position == Location('c', 1):
            return Location('d', 1)
        if king_to_position == Location('g', 8):
            return Location('f', 8)
        if king_to_position == Location('c', 8):
            return Location('d', 8)
        else:
            raise Exception('Invalid king move castle location.')

    def __remove_piece__(self, location):
        location_y_array = self.letters[location.letter]
        location_x_array = self.numbers[location.number]
        if self.squares[location_x_array][location_y_array] is not None:
            piece_removed = self.squares[location_x_array][location_y_array]
            self.squares[location_x_array][location_y_array] = None
            if piece_removed.colour == Colour.WHITE:
                del self.white_piece_locations[location]
            else:
                del self.black_piece_locations[location]
            return piece_removed
        else:
            raise Exception("There is no piece at this location.")

    def __add_piece__(self, piece, location):
        location_y_array = self.letters[location.letter]
        location_x_array = self.numbers[location.number]
        if self.squares[location_x_array][location_y_array] is not None:
            raise Exception("There is already a piece at this location")
        else:
            self.squares[location_x_array][location_y_array] = piece
            if piece.colour == Colour.WHITE:
                self.white_piece_locations[location] = piece
                if piece.name == "King":
                    self.white_king = (location, piece)
            else:
                self.black_piece_locations[location] = piece
                if piece.name == "King":
                    self.black_king = (location, piece)

    def __str__(self):
        board_string = ""
        row_i = 1
        for row in self.squares:
            board_string = " |".join(" " + str(square)
                                     if square is not None else "   " for square in row) \
                + " | {}\n".format(row_i) \
                + board_string
            board_string = "_______________________________________\n" + board_string
            row_i += 1
        board_string += "_______________________________________\n"
        board_string += "  A    B    C    D    E    F    G    H  \n"
        return board_string
