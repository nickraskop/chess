import pygame
from pygame._sdl2 import Window

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
Window.from_display_module().maximize()
clock = pygame.time.Clock()
running = True
dt = 0

bgBrown = pygame.Color(168, 94, 50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    centerScreen = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    w, h = pygame.display.get_surface().get_size()
    gameBoardSize = min(w, h) * 0.7
    gameBoard = pygame.Rect(0, 0, gameBoardSize, gameBoardSize)
    gameBoard.center = centerScreen

    screen.fill(bgBrown)
    # Render checkerboard
    # First, render outer square in the center of screen
    pygame.draw.rect(screen, "red", gameBoard)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
