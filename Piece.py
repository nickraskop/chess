import pygame


class Piece:
    pieceType: str = None
    color: str = None  # Might want to switch to enum (white, black)
    location: pygame.Vector2 = pygame.Vector2(0, 0)
    isDead: bool = False
    image: pygame.Surface = None

    def __init__(self, color, pieceType, loc):
        self.pieceType = pieceType
        self.location = loc
        self.color = color
        self.image = pygame.image.load(f"images/{color}/{pieceType}.svg")
