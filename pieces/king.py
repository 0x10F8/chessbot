from pieces.location import Location
from pieces.colour import Colour
from pieces.piece import Piece
from copy import deepcopy


class King(Piece):

    def __init__(self, colour):
        super().__init__(colour, "King", 999, self.__king_move_worker__)

    def __str__(self):
        return "{}K".format(str(self.colour)[0])

    def __get_directional_move_moves__(self, current_location, board, up=False, down=False, left=False, right=False):
        directions = [up, down, left, right]
        direction_counts = sum(1 for direction in directions if direction)
        if direction_counts < 1 or direction_counts > 2 or (up and down) or (left and right):
            raise Exception("Invalid directions given.")
        next_number = current_location.number
        next_letter = current_location.letter
        if up:
            next_number = current_location.number+1
        if right:
            next_letter = self.__get_next_letter__(current_location.letter)
        if down:
            next_number = current_location.number-1
        if left:
            next_letter = self.__get_previous_letter__(current_location.letter)
        return Location(next_letter, next_number)

    def __get_all_king_moves__(self, current_location, board):
        moves = []

        moves += [self.__get_directional_move_moves__(
            current_location, board, up=True)]
        moves += [self.__get_directional_move_moves__(
            current_location, board, down=True)]
        moves += [self.__get_directional_move_moves__(
            current_location, board, left=True)]
        moves += [self.__get_directional_move_moves__(
            current_location, board, right=True)]

        moves += [self.__get_directional_move_moves__(
            current_location, board, up=True, right=True)]
        moves += [self.__get_directional_move_moves__(
            current_location, board, down=True, right=True)]
        moves += [self.__get_directional_move_moves__(
            current_location, board, up=True, left=True)]
        moves += [self.__get_directional_move_moves__(
            current_location, board, down=True, left=True)]

        return moves

    def __get_enemy_moves_next_turn__(self, board):
        enemy_moves_next_turn = []
        for letter in board.letters.keys():
            for number in board.numbers.keys():
                board_location = Location(letter, number)
                piece_at_location = board.get_piece_at_square(board_location)
                if piece_at_location is not None and piece_at_location.colour != self.colour:
                    enemy_moves_next_turn += piece_at_location.allowed_moves(
                        board_location, board)
        return enemy_moves_next_turn

    def __non_check_moves__(self, current_location, moves, board):
        non_check_moves = []
        for move in moves:
            cloned_move = deepcopy(move)
            cloned_board = deepcopy(board)
            cloned_king = cloned_board.get_piece_at_square(current_location)
            cloned_board.move_piece(cloned_king, current_location, cloned_move)
            enemy_moves_next_turn = self.__get_enemy_moves_next_turn__(
                cloned_board)
            enemy_king_takes = [
                enemy_move for enemy_move in enemy_moves_next_turn
                if enemy_move.take and enemy_move.take_piece is cloned_king]
            if len(enemy_king_takes) == 0:
                non_check_moves += [move]
        return non_check_moves

    def __castling_moves__(self, current_location, enemy_moves_next_turn, board):
        castling_moves = []
        # Quick calc the castling positions
        castle_row = 1 if self.colour == Colour.WHITE else 8
        left_castle_letter = 'c'
        right_castle_letter = 'g'
        left_rook_castle_pos = Location('a', castle_row)
        right_rook_castle_pos = Location('h', castle_row)
        king_castle_pos = Location('e', castle_row)
        blank_squares_left = [Location(letter, castle_row)
                              for letter in ['b', 'c', 'd']]
        blank_squares_right = [Location(letter, castle_row)
                               for letter in ['f', 'g']]

       # King hasn't already moved and Not in check
        if self.moves_made < 1 and current_location == king_castle_pos \
                and current_location not in enemy_moves_next_turn:
            # Left rook still in original position
            piece_at_left_rook_pos = board.get_piece_at_square(
                left_rook_castle_pos)
            if piece_at_left_rook_pos is not None and piece_at_left_rook_pos.moves_made < 1:
                # Empty spaces between king and rook
                pieces_between_king_and_rook = [piece for piece in [board.get_piece_at_square(
                    location) for location in blank_squares_left] if piece is not None]
                if len(pieces_between_king_and_rook) == 0:
                    castling_moves += [Location(left_castle_letter, castle_row,
                                               castle=True,
                                               castle_piece=piece_at_left_rook_pos,
                                               castle_piece_location=left_rook_castle_pos)]
            # Right rook still in original position
            piece_at_right_rook_pos = board.get_piece_at_square(
                right_rook_castle_pos)
            if piece_at_right_rook_pos is not None and piece_at_right_rook_pos.moves_made < 1:
                # Empty spaces between king and rook
                pieces_between_king_and_rook = [piece for piece in [board.get_piece_at_square(
                    location) for location in blank_squares_right] if piece is not None]
                if len(pieces_between_king_and_rook) == 0:
                    castling_moves += [Location(right_castle_letter, castle_row,
                                               castle=True,
                                               castle_piece=piece_at_right_rook_pos,
                                               castle_piece_location=right_rook_castle_pos)]

        return castling_moves

    def __king_move_worker__(self, current_location, board):
        # Work out all moves
        moves = self.__get_all_king_moves__(current_location, board)
        # Remove invalid squares
        moves = [
            move for move in moves if self.__is_valid_square__(move, board)]
        # Remove where own pieces exist
        moves = self.__remove_moves_with_current_team__(moves, board)

        enemy_moves_next_turn = self.__get_enemy_moves_next_turn__(board)

        # Check for castling
        moves += self.__castling_moves__(current_location,
                                         enemy_moves_next_turn, board)

        # Check takes
        [self.__check_take__(move, board) for move in moves]
        
        # Remove moves that would put the king in check
        moves = self.__non_check_moves__(current_location, moves, board)

        
        return moves
