# to activate venv: source gameVenv/bin/activate
import pygame
from player import Player
import globals
from ghost import Ghost
import time


class App:
    FPS = 100
    def __init__(self):
        pygame.init()
        self.running = True
        self.player = Player()
        self.window = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
        self.ghosts = [Ghost() for _ in range(5)]

        #game loop
        clock = pygame.time.Clock()
        currentTime = time.time()
        i = 0
        while self.running:
            if (timeDiff := currentTime - time.time()) != (1/100):
                print(f"Timediff {timeDiff}")

            print((i := i + 1))
            self.events()
            self.render()

            currentTime = time.time()
            clock.tick(App.FPS)

        pygame.quit()


    def playerEvents(self, events):
        self.player.move(events)

    def ghostEvents(self, events):
        for ghost in self.ghosts:
            ghost.move(self.player.x, self.player.y)

    def render(self):
        self.window.fill((105, 105, 105))
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
                return
            
            self.playerEvents(events)
            self.ghostEvents(events)


if __name__ == "__main__":
    App()
