from chessboard.board import Board
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.colour import Colour
from pieces.location import Location


def basic_pawn_test():
    print("========================================")
    print("Performing the basic pawn movement test")
    print("========================================")
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


def pawn_take_test():
    print("========================================")
    print("Performing the pawn take test")
    print("========================================")
    board = Board()
    white_pawn_one = Pawn(Colour.WHITE)
    black_pawn_one = Pawn(Colour.BLACK)
    black_pawn_two = Pawn(Colour.BLACK)

    wp1_loc = Location('b', 2)
    bp1_loc = Location('a', 7)
    bp2_loc = Location('c', 7)

    board.__add_piece__(white_pawn_one, wp1_loc)
    board.__add_piece__(black_pawn_one, bp1_loc)
    board.__add_piece__(black_pawn_two, bp2_loc)

    print("The board was seeded with the following pieces: ")
    print("{} pawn at position {}".format(white_pawn_one.colour, wp1_loc))
    print("{} pawn at position {}".format(black_pawn_one.colour, bp1_loc))
    print("{} pawn at position {}".format(black_pawn_two.colour, bp2_loc))
    print(board)

    # White pawn moves
    print("For the {} pawn starting at position {} the moves are:".format(
        white_pawn_one.colour, wp1_loc))
    allowed_moves = white_pawn_one.allowed_moves(wp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]
    board.move_piece(white_pawn_one, wp1_loc, new_location)
    wp1_loc = new_location
    print("Moved the pawn to position {}".format(wp1_loc))
    print(board)

    # Black pawn moves
    print("For the {} pawn starting at position {} the moves are:".format(
        black_pawn_one.colour, bp1_loc))
    allowed_moves = black_pawn_one.allowed_moves(bp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]
    print("For the {} pawn starting at position {} the moves are:".format(
        black_pawn_two.colour, bp2_loc))
    allowed_moves = black_pawn_two.allowed_moves(bp2_loc, board)
    print(allowed_moves)

    board.move_piece(black_pawn_one, bp1_loc, new_location)
    print("Moved the {} pawn at {} to position {}".format(
        black_pawn_one.colour, bp1_loc, new_location))
    bp1_loc = new_location
    print(board)

    # White pawn moves
    print("For the {} pawn at position {} the moves are:".format(
        white_pawn_one.colour, wp1_loc))
    allowed_moves = white_pawn_one.allowed_moves(wp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]
    board.move_piece(white_pawn_one, wp1_loc, new_location)
    wp1_loc = new_location
    print("Moved the pawn to position {}".format(wp1_loc))
    print(board)


def pawn_en_passant_test():
    print("========================================")
    print("Performing the pawn en passant test")
    print("========================================")
    board = Board()
    white_pawn_one = Pawn(Colour.WHITE)
    black_pawn_one = Pawn(Colour.BLACK)
    black_pawn_two = Pawn(Colour.BLACK)

    wp1_loc = Location('b', 2)
    bp1_loc = Location('a', 7)
    bp2_loc = Location('c', 7)

    board.__add_piece__(white_pawn_one, wp1_loc)
    board.__add_piece__(black_pawn_one, bp1_loc)
    board.__add_piece__(black_pawn_two, bp2_loc)

    print("The board was seeded with the following pieces: ")
    print("{} pawn at position {}".format(white_pawn_one.colour, wp1_loc))
    print("{} pawn at position {}".format(black_pawn_one.colour, bp1_loc))
    print("{} pawn at position {}".format(black_pawn_two.colour, bp2_loc))
    print(board)

    # White pawn moves
    print("For the {} pawn starting at position {} the moves are:".format(
        white_pawn_one.colour, wp1_loc))
    allowed_moves = white_pawn_one.allowed_moves(wp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]
    board.move_piece(white_pawn_one, wp1_loc, new_location)
    wp1_loc = new_location
    print("Moved the pawn to position {}".format(wp1_loc))
    print(board)

    # Black pawn moves
    print("For the {} pawn starting at position {} the moves are:".format(
        black_pawn_one.colour, bp1_loc))
    allowed_moves = black_pawn_one.allowed_moves(bp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]
    print("For the {} pawn starting at position {} the moves are:".format(
        black_pawn_two.colour, bp2_loc))
    allowed_moves = black_pawn_two.allowed_moves(bp2_loc, board)
    print(allowed_moves)

    board.move_piece(black_pawn_one, bp1_loc, new_location)
    print("Moved the {} pawn at {} to position {}".format(
        black_pawn_one.colour, bp1_loc, new_location))
    bp1_loc = new_location
    print(board)

    # White pawn moves
    print("For the {} pawn at position {} the moves are:".format(
        white_pawn_one.colour, wp1_loc))
    allowed_moves = white_pawn_one.allowed_moves(wp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[0]
    board.move_piece(white_pawn_one, wp1_loc, new_location)
    wp1_loc = new_location
    print("Moved the pawn to position {}".format(wp1_loc))
    print(board)

    # Black pawn moves
    print("For the {} pawn starting at position {} the moves are:".format(
        black_pawn_one.colour, bp1_loc))
    allowed_moves = black_pawn_one.allowed_moves(bp1_loc, board)
    print(allowed_moves)
    print("For the {} pawn starting at position {} the moves are:".format(
        black_pawn_two.colour, bp2_loc))
    allowed_moves = black_pawn_two.allowed_moves(bp2_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]

    board.move_piece(black_pawn_two, bp2_loc, new_location)
    print("Moved the {} pawn at {} to position {}".format(
        black_pawn_two.colour, bp2_loc, new_location))
    bp2_loc = new_location
    print(board)

    # White pawn moves
    print("For the {} pawn at position {} the moves are:".format(
        white_pawn_one.colour, wp1_loc))
    allowed_moves = white_pawn_one.allowed_moves(wp1_loc, board)
    print(allowed_moves)
    new_location = allowed_moves[1]
    board.move_piece(white_pawn_one, wp1_loc, new_location)
    wp1_loc = new_location
    print("Moved the pawn to position {}".format(wp1_loc))
    print(board)
    print("The move history for this board is: ")
    [print(item) for item in board.move_history]


def basic_knight_test():
    print("========================================")
    print("Performing the basic knight movement test")
    print("========================================")
    board = Board()
    white_knight = Knight(Colour.WHITE)
    current_location = Location('b', 1)
    board.__add_piece__(white_knight, current_location)
    print(board)

    allowed_moves = white_knight.allowed_moves(current_location, board)
    print("For a {} {} starting at position {} the moves are:".format(
        white_knight.colour, white_knight.name, current_location))
    print(allowed_moves)

    new_location = allowed_moves[0]
    board.move_piece(white_knight, current_location, new_location)
    current_location = new_location
    print("Moved the {} to position {}".format(white_knight.name, new_location))
    print(board)
    print("For a {} {} at position {} the moves are:".format(
        white_knight.colour, white_knight.name, current_location))
    print(white_knight.allowed_moves(current_location, board))

def knight_take_test():
    print("========================================")
    print("Performing the knight take test")
    print("========================================")
    board = Board()
    white_knight = Knight(Colour.WHITE)
    current_location = Location('b', 1)
    board.__add_piece__(white_knight, current_location)

    white_pawn = Pawn(Colour.WHITE)
    black_pawn = Pawn(Colour.BLACK)

    board.__add_piece__(white_pawn, Location('a', 3))
    board.__add_piece__(black_pawn, Location('c', 3))

    print("Added a knight and 2 pawns to the board...")

    print(board)
    allowed_moves = white_knight.allowed_moves(current_location, board)
    print("For a {} {} starting at position {} the moves are:".format(
        white_knight.colour, white_knight.name, current_location))
    print(allowed_moves)

    new_location = allowed_moves[0]
    board.move_piece(white_knight, current_location, new_location)
    current_location = new_location
    print("Moved the {} to position {}".format(white_knight.name, new_location))
    print(board)
    print("For a {} {} at position {} the moves are:".format(
        white_knight.colour, white_knight.name, current_location))
    print(white_knight.allowed_moves(current_location, board))

def basic_rook_test():
    print("========================================")
    print("Performing the basic rook movement test")
    print("========================================")
    board = Board()
    piece = Rook(Colour.WHITE)
    current_location = Location('d', 5)
    board.__add_piece__(piece, current_location)
    print(board)

    allowed_moves = piece.allowed_moves(current_location, board)
    print("For a {} {} starting at position {} the moves are:".format(
        piece.colour, piece.name, current_location))
    print(allowed_moves)

    new_location = allowed_moves[0]
    board.move_piece(piece, current_location, new_location)
    current_location = new_location
    print("Moved the {} to position {}".format(piece.name, new_location))
    print(board)
    print("For a {} {} at position {} the moves are:".format(
        piece.colour, piece.name, current_location))
    print(piece.allowed_moves(current_location, board))

basic_pawn_test()
pawn_take_test()
pawn_en_passant_test()

basic_knight_test()
knight_take_test()

basic_rook_test()