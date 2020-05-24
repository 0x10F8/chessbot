from chessboard.board import Board
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.colour import Colour
from pieces.location import Location
from game.next_move import NextMove

def __add_inital_pieces__(board, colour):
    first_row = 1 if colour == Colour.WHITE else 8
    second_row = 2 if colour == Colour.WHITE else 7

    board.__add_piece__(Rook(colour), Location('a', first_row))
    board.__add_piece__(Knight(colour), Location('b', first_row))
    board.__add_piece__(Bishop(colour), Location('c', first_row))
    board.__add_piece__(Queen(colour), Location('d', first_row))
    board.__add_piece__(King(colour), Location('e', first_row))
    board.__add_piece__(Bishop(colour), Location('f', first_row))
    board.__add_piece__(Knight(colour), Location('g', first_row))
    board.__add_piece__(Rook(colour), Location('h', first_row))

    board.__add_piece__(Pawn(colour), Location('a', second_row))
    board.__add_piece__(Pawn(colour), Location('b', second_row))
    board.__add_piece__(Pawn(colour), Location('c', second_row))
    board.__add_piece__(Pawn(colour), Location('d', second_row))
    board.__add_piece__(Pawn(colour), Location('e', second_row))
    board.__add_piece__(Pawn(colour), Location('f', second_row))
    board.__add_piece__(Pawn(colour), Location('g', second_row))
    board.__add_piece__(Pawn(colour), Location('h', second_row))


def setup_game_board_worker():
    board = Board()
    __add_inital_pieces__(board, Colour.WHITE)
    __add_inital_pieces__(board, Colour.BLACK)
    return board


def insufficient_material_draw(board):
    white_piece_locations = board.white_piece_locations
    black_piece_locations = board.black_piece_locations
    # king versus king
    if (len(white_piece_locations) == 1 and len(black_piece_locations) == 1):
        return True
    
    if (len(white_piece_locations) == 2 and len(black_piece_locations) == 1) \
        or (len(white_piece_locations) == 1 and len(black_piece_locations) == 2):
        # king and bishop versus king

        # king and knight versus king
        return False
    
    # king and bishop versus king and bishop with the bishops on the same color
    return False


def get_all_next_moves(colour, board, calc_king=True):
    if colour == Colour.WHITE:
        king_location, king_piece = board.white_king
        piece_locations = board.white_piece_locations
    else:
        king_location, king_piece = board.black_king
        piece_locations = board.black_piece_locations
    next_moves = [move for move in
                  [NextMove(piece, location, piece.allowed_moves(location, board))
                   for (location, piece) in piece_locations.items()]
                  if len(move.moves) > 0]
    if calc_king and is_king_in_check(colour, board):
        next_moves = __get_moves_which_remove_check__(
            next_moves, colour, board)
        king_moves = king_piece.allowed_moves(king_location, board)
        if len(king_moves) > 0:
            next_moves += [NextMove(king_piece, king_location, king_moves)]
    return next_moves


def __get_moves_which_remove_check__(moves, colour, board):
    next_moves_remove_check = []
    for piece_next_move in moves:
        for move in piece_next_move.moves:
            cloned_board = board.clone()
            cloned_board.move_piece(piece_next_move.piece,
                                    piece_next_move.current_location, move)
            if not is_king_in_check(colour, cloned_board):
                next_moves_remove_check.append(piece_next_move)
    return next_moves_remove_check


def is_king_in_check(colour, board):
    if colour == Colour.WHITE:
        enemy_colour = Colour.BLACK
        _, king_piece = board.white_king
    else:
        enemy_colour = Colour.WHITE
        _, king_piece = board.black_king
    next_enemy_moves = get_all_next_moves(enemy_colour, board, calc_king=False)
    next_enemy_piece_moves = []
    for next_enemy_move in next_enemy_moves:
        next_enemy_piece_moves += next_enemy_move.moves
    king_takes = [enemy_move for enemy_move in next_enemy_piece_moves
                  if enemy_move.take and enemy_move.take_piece is king_piece]
    if len(king_takes) > 0:
        return True
    return False
