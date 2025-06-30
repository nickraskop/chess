import pygame
from pygame._sdl2 import Window

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

BROWN = pygame.Color(168, 94, 50)


def getColor(r, c):
    color = "white"
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
    gameBoardSize = min(screenWidth, screenHeight) * 0.7
    gameBoard = pygame.Surface((gameBoardSize, gameBoardSize))
    gameBoard.fill("red")
    gameBoardTopLeft = (
        centerScreen.x - gameBoardSize / 2,
        centerScreen.y - gameBoardSize / 2,
    )

    for row in range(8):
        for col in range(8):
            cell = pygame.Rect(
                row * (gameBoardSize / 8),
                col * (gameBoardSize / 8),
                gameBoardSize / 8,
                gameBoardSize / 8,
            )
            pygame.draw.rect(gameBoard, getColor(row, col), cell)

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
