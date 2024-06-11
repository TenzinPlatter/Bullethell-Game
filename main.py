# to activate venv: source gameVenv/bin/activate
import pygame
from player import Player
import globals
from ghost import Ghost
import time
from joystick import Joystick


class App:
    FPS = 100
    def __init__(self):
        pygame.init()
        self.running = True
        self.player = Player()
        self.window = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
        self.ghosts = [Ghost() for _ in range(5)]
        self.joystick = None

        #game loop
        clock = pygame.time.Clock()
        i = 0
        while self.running:
            self.events()
            self.render()

            clock.tick(App.FPS)

        pygame.quit()


    def playerEvents(self, events):
        if self.joystick is not None:
            unitVec = self.joystick.getMoveVector()
            # self.player.move(unitVec)
            #TODO: remove once joystick is fixed

    def ghostEvents(self, events):
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.joystick = Joystick(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                self.joystick = None

        if self.joystick:
            self.joystick.setCentre()

        self.playerEvents(events)
        self.ghostEvents(events)


if __name__ == "__main__":
    App()
