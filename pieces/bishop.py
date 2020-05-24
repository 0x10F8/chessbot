from pieces.location import Location
from pieces.colour import Colour
from pieces.piece import Piece


class Bishop(Piece):

    def __init__(self, colour):
        super().__init__(colour, "Bishop", 3, self.__bishop_move_worker__)

    def clone(self):
        cloned_piece = Bishop(self.colour)
        self.__clone_piece_properties__(cloned_piece)
        return cloned_piece
        
    def __str__(self):
        return "{}B".format(str(self.colour)[0])

    def __get_directional_move_moves__(self, current_location, board, up=True, right=True):
        moves = []
        vertical_direction = 1 if up else -1
        horizontal_direction_function = self.__get_next_letter__ if right \
            else self.__get_previous_letter__
        next_location = Location(horizontal_direction_function(
            current_location.letter), current_location.number+vertical_direction)
        while self.__is_valid_square__(next_location, board):
            piece_at_move = board.get_piece_at_square(next_location)
            if piece_at_move is None:
                moves.append(next_location)
            else:
                if piece_at_move.colour != self.colour:
                    moves.append(next_location)
                break
            next_location = Location(horizontal_direction_function(
                next_location.letter), next_location.number+vertical_direction)
        return moves

    def __bishop_move_worker__(self, current_location, board):
        moves = []
        moves += self.__get_directional_move_moves__(
            current_location, board, up=True, right=True)
        moves += self.__get_directional_move_moves__(
            current_location, board, up=True, right=False)
        moves += self.__get_directional_move_moves__(
            current_location, board, up=False, right=True)
        moves += self.__get_directional_move_moves__(
            current_location, board, up=False, right=False)
        [self.__check_take__(location, board) for location in moves]
        return moves
