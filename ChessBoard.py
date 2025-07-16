import pygame as pg

from Piece import Piece

BOARD_SIZE = 8


class ChessBoard:
    topLeft: pg.Vector2 = pg.Vector2(0, 0)
    surface: pg.Surface = None
    board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def addPiece(self, piece: Piece):
        self.board[int(piece.location.x)][int(piece.location.y)] = piece

    def printBoard(self):
        for rank in range(BOARD_SIZE):
            for file in range(BOARD_SIZE):
                piece: Piece = self.board[file][rank]
                pieceType = "    "
                if piece:
                    pieceType = piece.pieceType
                print(pieceType, end="|")
            print()
