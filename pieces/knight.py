from pieces.location import Location
from pieces.colour import Colour
from pieces.piece import Piece


class Knight(Piece):

    en_passant_row_white = 4
    en_passant_row_black = 5

    def __init__(self, colour):
        super().__init__(colour, "Knight", 3, self.__knight_move_worker__)

    def __str__(self):
        return "{}K".format(str(self.colour)[0])

    def __get_all_potential_moves__(self, current_location, board):
        moves = []
        # Black or white doesn't change the moves from the current position
        # But the comments here only make sense for white

        # Up and to left and right
        up_left = Location(self.__get_previous_letter__(
            current_location.letter), current_location.number+2)
        up_right = Location(self.__get_next_letter__(
            current_location.letter), current_location.number+2)
        moves.append(up_left)
        moves.append(up_right)

        # Down and to left and right
        down_left = Location(self.__get_previous_letter__(
            current_location.letter), current_location.number-2)
        down_right = Location(self.__get_next_letter__(
            current_location.letter), current_location.number-2)
        moves.append(down_left)
        moves.append(down_right)

        # Left and up and down
        left_up = Location(self.__get_previous_letter__(
            self.__get_previous_letter__(
                current_location.letter)
        ), current_location.number+1)
        left_down = Location(self.__get_previous_letter__(
            self.__get_previous_letter__(
                current_location.letter)
        ), current_location.number-1)
        moves.append(left_up)
        moves.append(left_down)

        # Right and up and down
        right_up = Location(self.__get_next_letter__(
            self.__get_next_letter__(
                current_location.letter)
        ), current_location.number+1)
        right_down = Location(self.__get_next_letter__(
            self.__get_next_letter__(
                current_location.letter)
        ), current_location.number-1)
        moves.append(right_up)
        moves.append(right_down)

        # Remove any invalid squares (e.g. j,-1)
        moves = [
            move for move in moves if self.__is_valid_square__(move, board)]

        return moves

    def __remove_moves_with_current_team__(self, moves, board):
        return [move for (move, piece) in
                [(move, board.get_piece_at_square(move)) for move in moves]
                if piece is None or piece.colour != self.colour]

    def __knight_move_worker__(self, current_location, board):
        moves = self.__get_all_potential_moves__(current_location, board)
        moves = self.__remove_moves_with_current_team__(moves, board)
        [self.__check_take__(location, board) for location in moves]
        return moves
