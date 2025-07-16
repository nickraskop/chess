from ChessBoard import ChessBoard
from Player import Player


class ChessGame:
    whitePlayer = None
    blackPlayer = None
    chessBoard = None

    def __init__(self):
        self.chessBoard = ChessBoard()
        self.whitePlayer = Player("white", self.chessBoard)
        self.blackPlayer = Player("black", self.chessBoard)

    def getWhitePlayer(self):
        return self.whitePlayer

    def getBlackPlayer(self):
        return self.blackPlayer

    def getChessBoard(self):
        return self.chessBoard
