import pygame
import math
from globals import WIDTH, HEIGHT

class Shotgun:
    def __init__(self, x, y):
        """cooldown should be in terms of frames, game is at 60FPS, pass in class
        not an instance"""
        self.image = pygame.image.load("assets/weapons/shotgun.png")
        self.bulletClass = ShotgunBullet
        self.cooldown = 120
        self.timeSinceLastShot = 0
        self.bullets = []
        self.x = x
        self.y = y

    def onLoop(self, x, y):
        self.x = x
        self.y = y
        i = 0
        while i < len(self.bullets):
            if self.bullets[i].hasExpired():
                self.bullets.pop(i)
            else:
                self.bullets[i].onLoop() 
                i += 1

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        
    def shoot(self, angle):
        dirVectors = []
        def getDirVec(angle):
            return [
                    math.cos(angle),
                    math.sin(angle)
                    ]
        for i in range(3):
            dirVectors.append(getDirVec( angle + (30 - 10 * i) ))

        for vec in dirVectors:
            self.bullets.append(self.bulletClass(vec, self.x, self.y))


class ShotgunBullet:
    def __init__(self, dirVector, x, y):
        self.velocity = 5
        self.image = "assets/weapons/yellowBullet.png"
        self.dirVector = dirVector
        self.framesAlive = 0
        self.x = x
        self.y = y
        self.image = None


    def hasExpired(self):
        #bullet is off the screen
        return (self.x > WIDTH or self.x < 0) and (self.y > HEIGHT or self.y < 0)

    def onLoop(self):
        self.move()
        self.framesAlive += 1

    def move(self):
        self.x += self.dirVector[0] * self.velocity
        self.y += self.dirVector[1] * self.velocity
