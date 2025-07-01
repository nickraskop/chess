import pygame
from pygame._sdl2 import Window

from Player import Player

# pygame setup
pygame.init()
pygame.display.set_caption("NICK CHESS")
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
gameBoard = pygame.Surface((50, 50))
Window.from_display_module().maximize()
clock = (
    pygame.time.Clock()
)  # Not needed right now, but potentially will use later for time controls
running = True

ROWS = 8
BOARD_SCALE = 0.7
BROWN = pygame.Color(168, 94, 50)


def getColor(r, c):
    color = "beige"
    if r % 2 == 0:
        if c % 2 == 0:
            color = "black"
    else:
        if c % 2 != 0:
            color = "black"
    return color


def createGameBoard():
    screenWidth, screenHeight = pygame.display.get_surface().get_size()
    centerScreen = pygame.Vector2(screenWidth / 2, screenHeight / 2)
    gameBoardSize = min(screenWidth, screenHeight) * BOARD_SCALE
    gameBoard = pygame.Surface((gameBoardSize, gameBoardSize))
    gameBoard.fill("red")
    gameBoardTopLeft = (
        centerScreen.x - gameBoardSize / 2,
        centerScreen.y - gameBoardSize / 2,
    )

    for row in range(ROWS):
        for col in range(ROWS):
            cell = pygame.Rect(
                row * (gameBoardSize / ROWS),
                col * (gameBoardSize / ROWS),
                gameBoardSize / ROWS,
                gameBoardSize / ROWS,
            )
            pygame.draw.rect(gameBoard, getColor(row, col), cell)

    whitePlayer = Player()
    for piece in whitePlayer.pieces:
        whitePawn = pygame.image.load("images/white/pawn.svg")
        whitePawn = pygame.transform.scale(
            whitePawn, (gameBoardSize / ROWS, gameBoardSize / ROWS)
        )
        gameBoard.blit(whitePawn, piece.location * (gameBoardSize / ROWS))

    # Blit must come after everything in the gameBoard is updated
    screen.blit(gameBoard, gameBoardTopLeft)


def handleVideoResize():
    screen.fill(BROWN)
    createGameBoard()


while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            handleVideoResize()
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
