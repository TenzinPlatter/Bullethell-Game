import pygame

def playerSpriteSheet():
    """returns a dictionary of images for each direction of player movement"""
    return {
            "N" : pygame.image.load("assets/characters/player/N.png"),
            "NE": pygame.image.load("assets/characters/player/NE.png"),
            "E" : pygame.image.load("assets/characters/player/E.png"),
            "SE": pygame.image.load("assets/characters/player/SE.png"),
            "S" : pygame.image.load("assets/characters/player/S.png"),
            "SW": pygame.image.load("assets/characters/player/SW.png"),
            "W" : pygame.image.load("assets/characters/player/W.png"),
            "NW": pygame.image.load("assets/characters/player/NW.png"),
            }


class Player:
    def __init__(self):
        self.dirSprites = playerSpriteSheet()
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.health = 5
