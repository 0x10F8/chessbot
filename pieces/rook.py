from pieces.location import Location
from pieces.colour import Colour
from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, colour):
        super().__init__(colour, "Rook", 5, self.__rook_move_worker__)

    def __str__(self):
        return "{}R".format(str(self.colour)[0])

    def __rook_move_worker__(self, current_location, board):
        moves = []

        current_number = current_location.number

        # Upwards moves
        for next_number in range(current_number+1, list(board.numbers.keys())[-1]+1):
            new_location = Location(current_location.letter, next_number)
            piece_at_move = board.get_piece_at_square(new_location)
            if piece_at_move is None:
                moves.append(new_location)
            else:
                if piece_at_move.colour != self.colour:
                    moves.append(new_location)
                break

        # Downwards moves
        for next_number in range(current_number-1, list(board.numbers.keys())[0]-1, -1):
            new_location = Location(current_location.letter, next_number)
            piece_at_move = board.get_piece_at_square(new_location)
            if piece_at_move is None:
                moves.append(new_location)
            else:
                if piece_at_move.colour != self.colour:
                    moves.append(new_location)
                break

        current_letter = current_location.letter

        # Rightwards moves
        right_location = Location(self.__get_next_letter__(
            current_letter), current_location.number)
        while self.__is_valid_square__(right_location, board):
            piece_at_move = board.get_piece_at_square(right_location)
            if piece_at_move is None:
                moves.append(right_location)
            else:
                if piece_at_move.colour != self.colour:
                    moves.append(right_location)
                break
            right_location = Location(self.__get_next_letter__(
                right_location.letter), current_location.number)
        
        # Leftwards moves
        left_location = Location(self.__get_previous_letter__(
            current_letter), current_location.number)
        while self.__is_valid_square__(left_location, board):
            piece_at_move = board.get_piece_at_square(left_location)
            if piece_at_move is None:
                moves.append(left_location)
            else:
                if piece_at_move.colour != self.colour:
                    moves.append(left_location)
                break
            left_location = Location(self.__get_previous_letter__(
                left_location.letter), current_location.number)

        [self.__check_take__(location, board) for location in moves]
        return moves
