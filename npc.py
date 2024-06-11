import pygame
import math
import random
import globals


class Npc:
    def __init__(self, x, y, spritePath):
        self.sprites = globals.getSpriteSheet(spritePath)
        self.currentSprite = self.sprites["S"]
        self.x = x
        self.y = y
        self.movement = [
                [0, 0],
                [0, 0]
                ]

    def move(self, playerX, playerY):
        dx = playerX - self.x
        dy = playerY - self.y
        print("player x y", playerX, playerY)
        magnitude = (dx**2 + dy**2)**.5
        if magnitude == 0:
            return
        unitVector = [dx * magnitude**-1, dy * magnitude**-1]
        dx, dy = unitVector[0] * self.moveSpeed, unitVector[1] * self.moveSpeed
        self.x += dx
        self.y += dy

        if dx == 0:
            if dy > 0:
                dir = "S"
            else:
                dir = "N"

        else:
            # look on page 5 of data notebook in goodnotes to see why i did
            # this
            if dx > 0:
                angle = math.degrees(math.atan(dy/dx))
                if 22.5 < angle < 67.5:
                    dir = "SE"
                elif -22.5 < angle < 22.5:
                    dir = "E"
                elif -67.5 < angle < -22.5:
                    dir = "NE"
                else:
                    dir = "N"
            else:
                dx = abs(dx)
                angle = math.degrees(math.atan(dy/dx))
                if 22.5 < angle < 67.5:
                    dir = "SE"
                elif -22.5 < angle < 22.5:
                    dir = "E"
                elif -67.5 < angle < -22.5:
                    dir = "NE"
                else:
                    dir = "N"

        if dir not in ["N", "NE", "NW", "E", "W", "S", "SW", "SE"]:
            raise Exception(f"{dir} is not a valid direction")

        self.currentSprite = self.sprites[dir]
        
    def draw(self, window):
        window.blit(self.currentSprite, (self.x, self.y))
