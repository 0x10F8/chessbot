from chessboard.board import Board
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.colour import Colour
from pieces.location import Location
from game.game_worker import setup_game_board_worker, get_all_next_moves, is_king_in_check
import random
import time

board = setup_game_board_worker()
print(board)

number_of_moves_since_take = 0


current_turn_colour = Colour.WHITE
while True:
    moves = get_all_next_moves(current_turn_colour, board)
    [print(move) for move in moves]
    print(board)
    selected_next_move = random.choice(moves)
    if number_of_moves_since_take >= 50:
        print("Draw - no takes in 50 moves")
        quit()
    if len(selected_next_move.moves) == 0:
        # Stalemate checker:
        if is_king_in_check(current_turn_colour, board):
            print("{} LOSES!".format(current_turn_colour))
        else:
            print("Stalemate - {} cannot make a legal move".format(current_turn_colour))
        quit()
    selected_piece_move = random.choice(selected_next_move.moves)
    board.move_piece(selected_next_move.piece,
                     selected_next_move.current_location,
                     selected_piece_move)
    number_of_moves_since_take += 1
    if selected_piece_move.take:
        number_of_moves_since_take = 0
    if current_turn_colour == Colour.WHITE:
        current_turn_colour = Colour.BLACK
    else:
        current_turn_colour = Colour.WHITE
