from pieces.location import Location


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

    def __is_valid_square__(self, location, board):
        if location.letter not in board.letters.keys() \
                or location.number not in board.numbers.keys():
            return False
        return True
    
    def __remove_moves_with_current_team__(self, moves, board):
        return [move for (move, piece) in
                [(move, board.get_piece_at_square(move)) for move in moves]
                if piece is None or piece.colour != self.colour]

    def __get_next_letter__(self, letter):
        return str(bytes([bytes(letter, 'utf-8')[0]+1]), 'utf-8')

    def __get_previous_letter__(self, letter):
        return str(bytes([bytes(letter, 'utf-8')[0]-1]), 'utf-8')

    def __check_take__(self, take_location, board):
        if self.__is_valid_square__(take_location, board):
            piece_at_move = board.get_piece_at_square(take_location)
            if piece_at_move is not None and piece_at_move.colour is not self.colour:
                take_location.take = True
                take_location.take_piece = piece_at_move
                take_location.take_piece_location = Location(
                    take_location.letter, take_location.number)
