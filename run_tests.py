from chessboard.board import Board
from pieces.pawn import Pawn
from pieces.colour import Colour
from pieces.location import Location


def basic_pawn_test():
    board = Board()
    pawn_colour = Colour.WHITE
    white_pawn_one = Pawn(pawn_colour)
    current_location = Location('a', 2)
    board.__add_piece__(white_pawn_one, current_location)
    print("For a {} pawn starting at position {} the moves are:".format(
        pawn_colour, current_location))
    print(white_pawn_one.allowed_moves(current_location, board))

    new_location = Location('a', 4)
    board.move_piece(white_pawn_one, current_location, new_location)
    current_location = new_location
    print("Moved the pawn to position {}".format(new_location))
    print("For a {} pawn at position {} the moves are:".format(
        pawn_colour, current_location))
    print(white_pawn_one.allowed_moves(current_location, board))


basic_pawn_test()
