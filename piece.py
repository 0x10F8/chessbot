from location import Location


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


class Pawn(Piece):

    def __init__(self, colour):
        super().__init__(colour, "Pawn", 1, self.__pawn_move_worker__)

    def __pawn_move_worker__(self, current_location, board):
        if self.moves_made == 0:
            """
            after first move only 1 move forward or take diagonal other colour pieces 
            or en passant other colour
            """
            return []
        else:
            """
            after first move only 1 move forward or take diagonal other colour pieces 
            or en passant other colour
            """
            return []
