from Player import Player


class ChessGame:
    whitePlayer = None
    blackPlayer = None

    def __init__(self):
        self.whitePlayer = Player("white")
        self.blackPlayer = Player("black")
