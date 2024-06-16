import pygame
from pygame import K_a, K_w, K_s, K_d
import math
import globals
from shotgun import Shotgun

class Player:
    def __init__(self):
        self.x = (globals.WIDTH - 32)/2
        self.y = (globals.HEIGHT - 32)/2
        self.sprites = globals.getSpriteSheet("assets/characters/player") 
        self.currentSprite = self.sprites["S"]
        self.moveSpeed = 3
        self.mouseDown = False
        self.health = 5
        self.actualRotation = 90
        self.weapon = Shotgun(self.x, self.y)
        self.movement = [
                [0, 0],
                [0, 0]
                ]

    def shoot(self):
        self.weapon.shoot(self.actualRotation)

    def move(self, unitVec):
        """ takes in unit vec of direction from joystick
        """
        dx, dy = unitVec[0] * self.moveSpeed, unitVec[1] * self.moveSpeed 
        self.x += unitVec[0] * self.moveSpeed
        self.y += unitVec[1] * self.moveSpeed
        dir = None
        self.actualRotation = math.degrees(math.atan2(dy, dx))
        #atan2 range is between -pi and pi / -180 and 180
        #for some reason N and S are switched
        if -22.5 < self.actualRotation <= 22.5: dir = "E"
        elif 22.5 < self.actualRotation <= 67.5: dir = "SE"
        elif 67.5 < self.actualRotation <= 112.5: dir = "S"
        elif 112.5 < self.actualRotation <= 157.5: dir = "SW"
        elif (157.5 < self.actualRotation <= 180) or (-180 <= self.actualRotation <= -157.5): dir = "W"
        elif -157.5 < self.actualRotation <= -112.5: dir = "NW"
        elif -112.5 < self.actualRotation <= -67.5: dir = "N"
        elif -67.5 < self.actualRotation <= -22.5: dir = "NE"

        if dir not in ["N", "NE", "NW", "E", "W", "S", "SW", "SE"]:
            raise Exception(f"rotation {self.actualRotation} is not valid")

        self.currentSprite = self.sprites[dir]

    def weaponUpdate(self):
        """call this to update weapon, rather than directly accessing the weapon"""
        try:
            self.weapon.onLoop(self.x, self.y)
        except:
            raise Exception("players weapon needs an onLoop method")
    
    def draw(self, window):
        """also draws weapon and bullets"""
        self.weapon.draw(window)
        window.blit(self.currentSprite, (self.x, self.y))
