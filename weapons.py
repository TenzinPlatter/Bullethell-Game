import pygame
import globals
import math
from functools import partial

class baseWeapon:
    def __init__(self, weaponImagePath: str, bulletImagePath: str, cooldown: int, bulletClass, bulletVelocity: int):
        """cooldown should be in terms of frames, game is at 60FPS, pass in class
        not an instance"""
        # represent relative rotation to last frame
        self.rotation = 0
        self.bulletClass = partial(bulletClass, imagePath = bulletImagePath, velocity = bulletVelocity)
        self.image = pygame.image.load(weaponImagePath)
        self.cooldown = cooldown
        self.timeSinceLastShot = 0
        self.bullets = []

    def shoot(self):
        dirVector = [
                math.cos(currentRotation),
                math.sin(currentRotation)
                ] 
        self.bullets.append(self.bulletClass(dirVector))

    def rotateImage(self):
        self.image = pygame.transform.rotate(self.image, self.rotation)

    def onLoop(self):
        self.rotateImage()
        i = 0
        while i < len(self.bullets):
            if self.bullets[i].hasExpired():
                self.bullets.pop(i)
                continue
            self.bullets[i].onLoop() 
            i += 1

class baseBullet:
    def __init__(self, imagePath: str, dirVector: tuple, velocity: float):
        self.image = pygame.image.load(bulletImagePath)
        self.dirVector = direction
        self.velocity = velocity
        self.framesAlive = 0

        #needs to be called after self.dirVector has been set
        self.rotationAngle = self.findRotationAngle()

    def onLoop(self):
        self.framesAlive += 1

    def findRotationAngle(self):
        #checks that dirVector has been set
        try:
            self.dirVector
        except NameError:
            raise Exception("you need to set dirVector before calling this function")
        
        x, y = self.dirVector
        if x == 0:
            return 90 if y > 0 else 270
        else:
            return math.degrees(math.atan2(y, x))

    def hasExpired(self):
        """TODO: decide how long for a bullet to expire and return bool value"""
        #TODO:
        pass
