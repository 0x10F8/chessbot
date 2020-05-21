from chessboard.board import Board
from pieces.pawn import Pawn
from pieces.colour import Colour
from pieces.location import Location

def pawn_test():
    board = Board()
    white_pawn_one = Pawn(Colour.WHITE)
    current_location = Location('a', 2)
    board.__add_piece__(white_pawn_one, current_location)
    print("For a pawn starting at position {} the moves are:".format(current_location))
    print(white_pawn_one.allowed_moves(current_location, board))


pawn_test()