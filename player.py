import pygame
from pygame import K_a, K_w, K_s, K_d
import math
import globals




class Player:
    def __init__(self):
        # center player spawn
        """
        self.x = (globals.WIDTH - 32)/2
        self.y = (globals.HEIGHT - 32)/2
"""
        self.x = 0
        self.y = 0
        self.sprites = globals.getSpriteSheet("assets/characters/player") 
        self.currentSprite = self.sprites["S"]
        self.moveSpeed = 4
        self.mouseDown = False
        self.health = 5
        self.movement = [
                [0, 0],
                [0, 0]
                ]

    def move(self, unitVec):
        """ takes in unit vec of direction from joystick
        """
        dx, dy = unitVec[0] * self.moveSpeed, unitVec[1] * self.moveSpeed 
        self.x += unitVec[0] * self.moveSpeed
        self.y += unitVec[1] * self.moveSpeed


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
                    dir = "SW"
                elif -22.5 < angle < 22.5:
                    dir = "W"
                elif -67.5 < angle < -22.5:
                    dir = "NW"
                else:
                    dir = "N"

        if dir not in ["N", "NE", "NW", "E", "W", "S", "SW", "SE"]:
            raise Exception(f"{dir} is not a valid direction")

        self.currentSprite = self.sprites[dir]
    

    def draw(self, window):
        window.blit(self.currentSprite, (self.x, self.y))



