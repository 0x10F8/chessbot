from pieces.location import Location
from pieces.colour import Colour
from pieces.piece import Piece

class Pawn(Piece):

    en_passant_row_white = 4
    en_passant_row_black = 5

    def __init__(self, colour):
        super().__init__(colour, "Pawn", 1, self.__pawn_move_worker__)

    def __move_forward__(self, current_location, board):
        moves = []
        if self.colour is Colour.WHITE:
            foward_move = Location(current_location.letter, current_location.number+1)
        else:
            foward_move = Location(current_location.letter, current_location.number-1)
        if self.__is_valid_square__(foward_move, board) \
                and board.get_piece_at_square(foward_move) is None:
            moves.append(foward_move)
        return moves

    def __first_move__(self, current_location, board):
        moves = []
        if self.moves_made == 0:
            if self.colour is Colour.WHITE:
                foward_move = Location(
                    current_location.letter, current_location.number+2)
            else:
                foward_move = Location(
                    current_location.letter, current_location.number-2)
            if self.__is_valid_square__(foward_move, board) \
                    and board.get_piece_at_square(foward_move) is None:
                moves.append(foward_move)
        return moves

    def __normal_takes__(self, current_location, board):
        moves = []
        if self.colour is Colour.WHITE:
            up_left_take = Location(self.__get_previous_letter__(
                current_location.letter), current_location.number+1)
            self.__check_take__(up_left_take, board)
            if up_left_take.take:
                moves.append(up_left_take)
            up_right_take = Location(self.__get_next_letter__(
                current_location.letter), current_location.number+1)
            self.__check_take__(up_right_take, board)
            if up_right_take.take:
                moves.append(up_right_take)
        else:
            down_left_take = Location(self.__get_previous_letter__(
                current_location.letter), current_location.number-1)
            self.__check_take__(down_left_take, board)
            if down_left_take.take:
                moves.append(down_left_take)
            down_right_take = Location(self.__get_next_letter__(
                current_location.letter), current_location.number-1)
            self.__check_take__(down_right_take, board)
            if down_right_take.take:
                moves.append(down_right_take)
        return moves

    def __get_en_passant_row_for_attacking_colour__(self, colour):
        if colour is Colour.WHITE:
            return self.en_passant_row_black
        if colour is Colour.BLACK:
            return self.en_passant_row_white

    def __en_passant_takes__(self, current_location, board):
        # The en passant rule means that we can take double moved
        # pawns as if they only moved 1 square, immediately after
        # the move was made.
        moves = []
        move_history = board.move_history
        en_passant_row = self.__get_en_passant_row_for_attacking_colour__(
            self.colour)
        if len(move_history) != 0:
            last_move = move_history[-1]
            if current_location.number == en_passant_row and \
                    last_move.piece.name == "Pawn" \
                    and last_move.piece.colour is not self.colour \
                    and last_move.piece.moves_made == 1 \
                    and last_move.to_location.number == en_passant_row:
                right_letter = self.__get_next_letter__(
                    last_move.to_location.letter)
                left_letter = self.__get_previous_letter__(
                    last_move.to_location.letter)
                if left_letter is current_location.letter \
                        or right_letter is current_location.letter:
                    take_location = Location(
                        last_move.to_location.letter, last_move.to_location.number)
                    if self.colour is Colour.WHITE:
                        take = Location(
                            last_move.to_location.letter, current_location.number+1,
                            True, last_move.piece, take_location)
                        moves.append(take)
                    else:
                        take = Location(
                            last_move.to_location.letter, current_location.number-1,
                            True, last_move.piece, take_location)
                        moves.append(take)
        return moves

    def __pawn_move_worker__(self, current_location, board):
        moves = []
        # White pawns move up
        if self.colour is Colour.WHITE:
            # Move forward one
            moves += self.__move_forward__(current_location, board)
            # If its the first move then 2 space move is possible
            moves += self.__first_move__(current_location, board)
            # Normal takes
            moves += self.__normal_takes__(current_location, board)
            # En Passant Takes
            moves += self.__en_passant_takes__(current_location, board)
        return moves
