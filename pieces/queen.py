from pieces.location import Location
from pieces.colour import Colour
from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook


class Queen(Piece):

    def __init__(self, colour):
        super().__init__(colour, "Queen", 9, self.__queen_move_worker__)
        self.rook = Rook(self.colour)
        self.bishop = Bishop(self.colour)

    def __str__(self):
        return "{}Q".format(str(self.colour)[0])

    def clone(self):
        cloned_piece = Queen(self.colour)
        self.__clone_piece_properties__(cloned_piece)
        return cloned_piece

    def __queen_move_worker__(self, current_location, board):
        moves = []
        moves += self.rook.__rook_move_worker__(current_location, board)
        moves += self.bishop.__bishop_move_worker__(current_location, board)
        return moves
