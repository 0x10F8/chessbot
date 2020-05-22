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


def get_all_next_moves(piece_locations, board):
    return [move for move in [NextMove(piece, location, piece.allowed_moves(location, board))
            for (location, piece) in piece_locations.items()] if len(move.moves) > 0]
