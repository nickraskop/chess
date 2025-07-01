import pygame as pg
from pygame._sdl2 import Window

from ChessBoard import ChessBoard
from ChessGame import ChessGame

# pygame setup
pg.init()
pg.display.set_caption("NICK CHESS")
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
Window.from_display_module().maximize()
clock = pg.time.Clock()
running = True
chessGame = ChessGame()
chessBoard = ChessBoard()

BOARD_SIZE = 8
BOARD_SCALE = 0.7
BROWN = pg.Color(168, 94, 50)
GRAY = pg.Color(84, 83, 77)


def getColor(r, c):
    color = "beige"
    if r % 2 == 0:
        if c % 2 == 0:
            color = BROWN
    else:
        if c % 2 != 0:
            color = BROWN
    return color


def drawChessBoard():
    for rank in range(BOARD_SIZE):
        for file in range(BOARD_SIZE):
            cell = pg.Rect(
                rank * (chessBoard.size / BOARD_SIZE),
                file * (chessBoard.size / BOARD_SIZE),
                chessBoard.size / BOARD_SIZE,
                chessBoard.size / BOARD_SIZE,
            )
            pg.draw.rect(chessBoard.surface, getColor(rank, file), cell)

    for piece in chessGame.whitePlayer.pieces + chessGame.blackPlayer.pieces:
        piece.image = pg.transform.scale(
            piece.image, (chessBoard.size / BOARD_SIZE, chessBoard.size / BOARD_SIZE)
        )
        chessBoard.surface.blit(
            piece.image, piece.location * (chessBoard.size / BOARD_SIZE)
        )

    screen.blit(chessBoard.surface, chessBoard.topLeft)


def updateScreen():
    screenWidth, screenHeight = pg.display.get_surface().get_size()
    centerScreen = pg.Vector2(screenWidth / 2, screenHeight / 2)
    chessBoard.size = min(screenWidth, screenHeight) * BOARD_SCALE
    chessBoard.surface = pg.Surface((chessBoard.size, chessBoard.size))
    chessBoard.topLeft = (
        centerScreen.x - chessBoard.size / 2,
        centerScreen.y - chessBoard.size / 2,
    )
    screen.fill(GRAY)
    drawChessBoard()


while running:
    # Poll for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    updateScreen()

    # flip() the display to put your work on screen
    pg.display.flip()
    clock.tick(60)  # Limit 60 fps

pg.quit()
