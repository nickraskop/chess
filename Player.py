import pygame as pg

from Piece import Piece

INITIAL_FILES = {
    "leftRook": 0,
    "rightRook": 7,
    "leftKnight": 1,
    "rightKnight": 6,
    "leftBishop": 2,
    "rightBishop": 5,
    "queen": 3,
    "king": 4,
}


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
            self.addPiece("pawn", pg.Vector2(col, rank))

    def initRooks(self, rank):
        self.addPiece("rook", pg.Vector2(INITIAL_FILES["leftRook"], rank))  # Left
        self.addPiece("rook", pg.Vector2(INITIAL_FILES["rightRook"], rank))  # Right

    def initKnights(self, rank):
        self.addPiece("knight", pg.Vector2(INITIAL_FILES["leftKnight"], rank))  # Left
        self.addPiece("knight", pg.Vector2(INITIAL_FILES["rightKnight"], rank))  # Right

    def initBishops(self, rank):
        self.addPiece("bishop", pg.Vector2(INITIAL_FILES["leftBishop"], rank))  # Left
        self.addPiece("bishop", pg.Vector2(INITIAL_FILES["rightBishop"], rank))  # Right

    def initQueen(self, rank):
        self.addPiece("queen", pg.Vector2(INITIAL_FILES["queen"], rank))

    def initKing(self, rank):
        self.addPiece("king", pg.Vector2(INITIAL_FILES["king"], rank))
