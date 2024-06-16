import pygame

WIDTH, HEIGHT = 1400, 850

def setSize(coords: tuple):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = coords

def getSpriteSheet(dirPath):
    """returns a dictionary of images for each direction of movement,
    takes in a path to directory with each sprite"""
    sprites = {
            "N" : pygame.image.load(f"{dirPath}/N.png"),
            "E" : pygame.image.load(f"{dirPath}/E.png"),
            "S" : pygame.image.load(f"{dirPath}/S.png"),
            "W" : pygame.image.load(f"{dirPath}/W.png"),
            "NE": pygame.image.load(f"{dirPath}/NE.png"),
            "SE": pygame.image.load(f"{dirPath}/SE.png"),
            "NW": pygame.image.load(f"{dirPath}/NW.png"),
            "SW": pygame.image.load(f"{dirPath}/SW.png"),
            }
    for key in sprites.keys():
        sprites[key] = pygame.transform.rotozoom(sprites[key], 0, 2)        
    return sprites

def distanceMagnitude(p1: tuple, p2: tuple):
    """takes two points of same dimension, returns magnitude of the
    distance between them. For single vector mag use 0 vector as a point"""
    temp = 0
    for v1, v2 in zip(p1, p2):
        diff = v1 - v2
        temp += diff**2

    return temp**.5
