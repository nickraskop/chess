import pygame as pg

from ChessBoard import ChessBoard
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
    color: str = ""
    chessBoard: ChessBoard = None

    def __init__(self, color: str, chessBoard: ChessBoard):
        self.color = color
        self.chessBoard = chessBoard
        self.initPieces()

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
        for file in range(8):
            pawn = Piece(self.color, "pawn", pg.Vector2(file, rank))
            self.chessBoard.addPiece(pawn)

    def initRooks(self, rank):
        leftRook = Piece(
            self.color, "rook", pg.Vector2(INITIAL_FILES["leftRook"], rank)
        )
        rightRook = Piece(
            self.color, "rook", pg.Vector2(INITIAL_FILES["rightRook"], rank)
        )
        self.chessBoard.addPiece(leftRook)
        self.chessBoard.addPiece(rightRook)

    def initKnights(self, rank):
        leftKnight = Piece(
            self.color, "knight", pg.Vector2(INITIAL_FILES["leftKnight"], rank)
        )
        rightKnight = Piece(
            self.color, "knight", pg.Vector2(INITIAL_FILES["rightKnight"], rank)
        )
        self.chessBoard.addPiece(leftKnight)
        self.chessBoard.addPiece(rightKnight)

    def initBishops(self, rank):
        leftBishop = Piece(
            self.color, "bishop", pg.Vector2(INITIAL_FILES["leftBishop"], rank)
        )
        rightBishop = Piece(
            self.color, "bishop", pg.Vector2(INITIAL_FILES["rightBishop"], rank)
        )
        self.chessBoard.addPiece(leftBishop)
        self.chessBoard.addPiece(rightBishop)

    def initQueen(self, rank):
        queen = Piece(self.color, "queen", pg.Vector2(INITIAL_FILES["queen"], rank))
        self.chessBoard.addPiece(queen)

    def initKing(self, rank):
        king = Piece(self.color, "king", pg.Vector2(INITIAL_FILES["king"], rank))
        self.chessBoard.addPiece(king)
