from location import Location
from colour import Colour
from copy import deepcopy


class Piece:

    def __init__(self, colour, name, points, allowed_moves_worker):
        super().__init__()
        self.colour = colour
        self.name = name
        self.points = points
        self.allowed_moves_worker = allowed_moves_worker
        self.moves_made = 0

    def allowed_moves(self, current_location, board):
        return self.allowed_moves_worker(current_location, board)

    def is_move_allowed(self, current_location, proposed_location, board):
        return proposed_location in self.allowed_moves_worker(current_location, board)

    def piece_moved(self):
        self.moves_made += 1

    def __is_valid_square__(self, location, board):
        if location.letter not in board.letters.keys() \
                or location.number not in board.numbers.keys():
            return False
        return True

    def __get_next_letter__(self, letter):
        return str(bytes([bytes(letter, 'utf-8')[0]+1]), 'utf-8')

    def __get_previous_letter__(self, letter):
        return str(bytes([bytes(letter, 'utf-8')[0]-1]), 'utf-8')

    def __check_take__(self, take_location, board):
        if self.__is_valid_square__(take_location, board):
            piece_at_move = board.get_piece_at_square(take_location)
            if piece_at_move is not None and piece_at_move.colour is not self.colour:
                take_location.take = True
                take_location.take_piece = piece_at_move


class Pawn(Piece):

    en_passant_row_white = 4
    en_passant_row_black = 5

    def __init__(self, colour):
        super().__init__(colour, "Pawn", 1, self.__pawn_move_worker__)

    def __move_forward__(self, current_location, board):
        moves = []
        if self.colour is Colour.WHITE:
            foward_move = Location(current_location.letter, current_location+1)
        else:
            foward_move = Location(current_location.letter, current_location-1)
        if self.__is_valid_square__(foward_move, board) \
                and board.get_piece_at_square(foward_move) is None:
            moves.append(foward_move)
        return moves

    def __first_move__(self, current_location, board):
        moves = []
        if self.moves_made == 0:
            if self.colour is Colour.WHITE:
                foward_move = Location(
                    current_location.letter, current_location+2)
            else:
                foward_move = Location(
                    current_location.letter, current_location-2)
            if self.__is_valid_square__(foward_move, board) \
                    and board.get_piece_at_square(foward_move) is None:
                moves.append(foward_move)
        return moves

    def __normal_takes__(self, current_location, board):
        moves = []
        if self.colour is Colour.WHITE:
            up_left_take = Location(self.__get_previous_letter__(
                current_location.letter), current_location+1)
            self.__check_take__(up_left_take, board)
            if up_left_take.take:
                moves.append(up_left_take)
            up_right_take = Location(self.__get_next_letter__(
                current_location.letter), current_location+1)
            self.__check_take__(up_right_take, board)
            if up_right_take.take:
                moves.append(up_right_take)
        else:
            down_left_take = Location(self.__get_previous_letter__(
                current_location.letter), current_location-1)
            self.__check_take__(down_left_take, board)
            if down_left_take.take:
                moves.append(down_left_take)
            down_right_take = Location(self.__get_next_letter__(
                current_location.letter), current_location-1)
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
                    last_move.piece.name is "Pawn" \
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
