# to activate venv: source gameVenv/bin/activate
import pygame
from player import Player


class App:
    WIDTH, HEIGHT = 800, 800
    FPS = 60
    def __init__(self):
        pygame.init()
        self.running = True
        self.player = Player()
        self.window = pygame.display.set_mode((App.WIDTH, App.HEIGHT))

        #game loop
        clock = pygame.time.Clock()
        while self.running:
            self.events()
            self.render()

            clock.tick(App.FPS)

        pygame.quit()


    def render(self):
        self.window.fill((105, 105, 105))

        #update entire screen
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return


if __name__ == "__main__":
    App()
