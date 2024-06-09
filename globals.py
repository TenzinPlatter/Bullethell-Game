import pygame

WIDTH, HEIGHT = 800, 800

def getSpriteSheet(dirPath):
    """returns a dictionary of images for each direction of movement,
    takes in a path to directory with each sprite"""
    sprites = {
            "N" : pygame.image.load(f"{dirPath}/N.png"),
            "NE": pygame.image.load(f"{dirPath}/NE.png"),
            "E" : pygame.image.load(f"{dirPath}/E.png"),
            "SE": pygame.image.load(f"{dirPath}/SE.png"),
            "S" : pygame.image.load(f"{dirPath}/S.png"),
            "SW": pygame.image.load(f"{dirPath}/SW.png"),
            "W" : pygame.image.load(f"{dirPath}/W.png"),
            "NW": pygame.image.load(f"{dirPath}/NW.png"),
            }
    for key in sprites.keys():
        sprites[key] = pygame.transform.rotozoom(sprites[key], 0, 2)        
    return sprites
