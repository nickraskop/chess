import pygame as pg
from pygame._sdl2 import Window

from Player import Player

# pygame setup
pg.init()
pg.display.set_caption("NICK CHESS")
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
gameBoard = pg.Surface((50, 50))
Window.from_display_module().maximize()
running = True

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


def createGameBoard():
    screenWidth, screenHeight = pg.display.get_surface().get_size()
    centerScreen = pg.Vector2(screenWidth / 2, screenHeight / 2)
    gameBoardSize = min(screenWidth, screenHeight) * BOARD_SCALE
    gameBoard = pg.Surface((gameBoardSize, gameBoardSize))
    gameBoardTopLeft = (
        centerScreen.x - gameBoardSize / 2,
        centerScreen.y - gameBoardSize / 2,
    )

    for rank in range(BOARD_SIZE):
        for file in range(BOARD_SIZE):
            cell = pg.Rect(
                rank * (gameBoardSize / BOARD_SIZE),
                file * (gameBoardSize / BOARD_SIZE),
                gameBoardSize / BOARD_SIZE,
                gameBoardSize / BOARD_SIZE,
            )
            pg.draw.rect(gameBoard, getColor(rank, file), cell)

    whitePlayer = Player("white")
    blackPlayer = Player("black")
    for piece in whitePlayer.pieces + blackPlayer.pieces:
        piece.image = pg.transform.scale(
            piece.image, (gameBoardSize / BOARD_SIZE, gameBoardSize / BOARD_SIZE)
        )
        gameBoard.blit(piece.image, piece.location * (gameBoardSize / BOARD_SIZE))

    # Blit must come after everything in the gameBoard is updated
    screen.blit(gameBoard, gameBoardTopLeft)


def handleVideoResize():
    screen.fill(GRAY)
    createGameBoard()


while running:
    # Poll for events
    for event in pg.event.get():
        if event.type == pg.VIDEORESIZE:
            handleVideoResize()
        if event.type == pg.QUIT:
            running = False

    # flip() the display to put your work on screen
    pg.display.flip()

pg.quit()
