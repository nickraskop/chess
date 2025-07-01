import pygame as pg


class Piece:
    pieceType: str = None
    color: str = None  # Might want to switch to enum (white, black)
    location: pg.Vector2 = pg.Vector2(0, 0)
    isDead: bool = False
    image: pg.Surface = None

    def __init__(self, color, pieceType, loc):
        self.pieceType = pieceType
        self.location = loc
        self.color = color
        self.image = pg.image.load(f"images/{color}/{pieceType}.svg")
