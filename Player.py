import pygame

from Piece import Piece


class Player:
    pieces: list[Piece] = []
    color: str = ""

    def __init__(self, color):
        self.color = color
        self.initPieces()

    def addPiece(self, pieceType, loc):
        newPiece = Piece(self.color, pieceType, loc)  # TODO: Allow black pieces
        self.pieces.append(newPiece)

    def initPieces(self):
        self.initPawns()
        self.initRooks()
        self.initKnights()
        self.initBishops()
        self.initQueen()
        self.initKing()

    def initPawns(self):
        for col in range(8):
            self.addPiece(
                "pawn", pygame.Vector2(col, 6)
            )  # Not sure why its (col, 1) instead of (1, col)

    def initRooks(self):
        # Left rook
        self.addPiece("rook", pygame.Vector2(0, 7))

        # Right rook
        self.addPiece("rook", pygame.Vector2(7, 7))

    def initKnights(self):
        # Left knight
        self.addPiece("knight", pygame.Vector2(1, 7))

        # Right knight
        self.addPiece("knight", pygame.Vector2(6, 7))

    def initBishops(self):
        # Left
        self.addPiece("bishop", pygame.Vector2(2, 7))

        # Right
        self.addPiece("bishop", pygame.Vector2(5, 7))

    def initQueen(self):
        self.addPiece("queen", pygame.Vector2(3, 7))

    def initKing(self):
        self.addPiece("king", pygame.Vector2(4, 7))
