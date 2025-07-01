import pygame


class Piece:
    # This will likely contain location, isDead, isMoving, etc
    pieceType = None
    location = pygame.Vector2(0, 0)
    isDead = False

    def __init__(self, pieceType, loc):
        self.pieceType = pieceType
        self.location = loc
