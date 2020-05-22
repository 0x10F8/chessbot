from chessboard.board import Board
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.colour import Colour
from pieces.location import Location
from game.game_worker import setup_game_board_worker, get_all_next_moves

board = setup_game_board_worker()
print(board)

print("White's first moves are: ")
moves = get_all_next_moves(board.white_piece_locations, board)
[print(move) for move in moves]