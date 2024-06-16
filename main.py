# to activate venv: source gameVenv/bin/activate
import pygame
from player import Player
import globals
from ghost import Ghost
import time
from joystick import Joystick
import random


class Level:
    FPS = 60
    def __init__(self):
        pygame.init()
        self.running = True
        self.player = Player()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        globals.setSize(self.window.get_size())
        pygame.display.set_caption("GAME!!!!!!!")
        self.ghosts = self.initGhosts()
        self.joystick = None

        #game loop
        clock = pygame.time.Clock()
        i = 0
        while self.running:
            self.events()
            self.render()

            clock.tick(Level.FPS)

        pygame.quit()


    def playerOnLoop(self, events):
        if self.joystick is not None:
            unitVec = self.joystick.getMoveVector()
            self.player.move(unitVec)
        if self.player.weapon != None:
            self.player.weaponUpdate()

    def ghostOnLoop(self, events):
        for ghost in self.ghosts:
            ghost.move(self.player.x, self.player.y)

    def render(self):
        self.window.fill((105, 105, 105))
        if self.joystick is not None:
            self.joystick.draw(self.window)
        self.player.draw(self.window)
        self.drawAllEnemies(self.ghosts) 

        #update entire screen
        pygame.display.flip()

    def drawAllEnemies(self, *enemies):
        for ls in enemies:
            for enemy in ls:
                enemy.draw(self.window)

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            #check for esc press to exit fullscreen window
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.joystick = Joystick(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                self.joystick = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if self.player.weapon:
                        self.player.shoot()

        if self.joystick:
            self.joystick.setCentre()

        self.playerOnLoop(events)
        self.ghostOnLoop(events)

    def initGhosts(self):
        ghosts = []
        random.seed(1)
        for i in range(5):
            x = random.randrange(0, globals.WIDTH)
            y = random.randrange(0, globals.HEIGHT)
            center = (globals.WIDTH - 32)/2, (globals.HEIGHT - 32)/2            
            while globals.distanceMagnitude((x, y), center) < 100:
                x = random.randrange(0, globals.WIDTH)
                y = random.randrange(0, globals.HEIGHT)
            ghosts.append(Ghost(x, y)) 
        return ghosts


if __name__ == "__main__":
    Level()
