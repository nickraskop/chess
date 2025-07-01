import pygame

from Piece import Piece


class Player:
    pieces = []

    def __init__(self):
        self.initPieces()

    def addPiece(self, pieceType, loc):
        newPiece = Piece(pieceType, loc)
        self.pieces.append(newPiece)

    def initPieces(self):
        self.createPawns()

    def createPawns(self):
        for col in range(8):
            self.addPiece(
                "pawn", pygame.Vector2(col, 1)
            )  # Not sure why its (col, 1) instead of (1, col)
