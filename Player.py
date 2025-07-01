import pygame

from Piece import Piece


class Player:
    pieces: list[Piece] = []
    color: str = ""

    def __init__(self, color):
        self.color = color
        self.initPieces()

    def addPiece(self, pieceType, loc):
        newPiece = Piece(self.color, pieceType, loc)
        self.pieces.append(newPiece)

    def initPieces(self):
        if self.color == "white":
            backLine, frontLine = 7, 6
        else:
            backLine, frontLine = 0, 1

        self.initPawns(frontLine)
        self.initRooks(backLine)
        self.initKnights(backLine)
        self.initBishops(backLine)
        self.initQueen(backLine)
        self.initKing(backLine)

    def initPawns(self, rank):
        for col in range(8):
            self.addPiece("pawn", pygame.Vector2(col, rank))

    def initRooks(self, rank):
        # Left
        self.addPiece("rook", pygame.Vector2(0, rank))

        # Right
        self.addPiece("rook", pygame.Vector2(7, rank))

    def initKnights(self, rank):
        # Left
        self.addPiece("knight", pygame.Vector2(1, rank))

        # Right
        self.addPiece("knight", pygame.Vector2(6, rank))

    def initBishops(self, rank):
        # Left
        self.addPiece("bishop", pygame.Vector2(2, rank))

        # Right
        self.addPiece("bishop", pygame.Vector2(5, rank))

    def initQueen(self, rank):
        self.addPiece("queen", pygame.Vector2(3, rank))

    def initKing(self, rank):
        self.addPiece("king", pygame.Vector2(4, rank))
