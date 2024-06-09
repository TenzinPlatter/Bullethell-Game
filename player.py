import pygame
from pygame import K_a, K_w, K_s, K_d
import math
import globals




class Player:
    def __init__(self):
        # center player spawn
        self.x = (globals.WIDTH - 32)/2
        self.y = (globals.HEIGHT - 32)/2
        self.sprites = globals.getSpriteSheet("assets/characters/player") 
        self.currentSprite = self.sprites["S"]
        self.moveSpeed = 4
        self.health = 5
        self.movement = [
                [0, 0],
                [0, 0]
                ]

    def setMoveKeys(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.movement[0][0] = -1
                if event.key == pygame.K_d:
                    self.movement[0][1] = 1
                if event.key == pygame.K_w:
                    self.movement[1][0] = -1
                if event.key == pygame.K_s:
                    self.movement[1][1] = 1
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.movement[0][0] = 0
                if event.key == pygame.K_d:
                    self.movement[0][1] = 0
                if event.key == pygame.K_w:
                    self.movement[1][0] = 0
                if event.key == pygame.K_s:
                    self.movement[1][1] = 0


    def move(self, events):
        self.setMoveKeys(events)
        # movement[0][0] is a and [0][1] is d, so if both are pressed then no 
        # x movement, same thing for y where [1][0] is w and [1][1] is d
        dx = (self.movement[0][0] + self.movement[0][1]) * self.moveSpeed
        dy = (self.movement[1][0] + self.movement[1][1]) * self.moveSpeed
        self.x += dx       
        self.y += dy

        if dx == 0 and dy == 0:
            return

        dir = None
        if dx == 0:
            if dy > 0:
                dir = "S"
            else:
                dir = "N"

        else:
            if dx > 0:
                angle = math.degrees(math.atan(dy/dx))
                match angle:
                    case 0:
                        dir = "E"
                    case 45:
                        dir = "SE"
                    case -45:
                        dir = "NE"
            else:
                dx = abs(dx)
                angle = math.degrees(math.atan(dy/dx))
                match angle:
                    case 0:
                        dir = "W"
                    case 45:
                        dir = "SW"
                    case -45:
                        dir = "NW"

        if dir not in ["N", "NE", "NW", "E", "W", "S", "SW", "SE"]:
            raise Exception(f"{dir} is not a valid direction")

        self.currentSprite = self.sprites[dir]
    

    def draw(self, window):
        window.blit(self.currentSprite, (self.x, self.y))



