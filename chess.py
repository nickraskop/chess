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


# TODO: Piece Class
class Piece:
    # This will likely contain location, isDead, isMoving, etc
    pieceType = None
    location = pygame.Vector2(0, 0)
    isDead = False

    def __init__(self, pieceType, loc):
        self.pieceType = pieceType
        self.location = loc


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

    whitePlayer = Player()
    for piece in whitePlayer.pieces:
        whitePawn = pygame.image.load("images/whitePawn.svg")
        whitePawn = pygame.transform.scale(
            whitePawn, (gameBoardSize / 8, gameBoardSize / 8)
        )
        gameBoard.blit(whitePawn, piece.location * (gameBoardSize / 8))

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
