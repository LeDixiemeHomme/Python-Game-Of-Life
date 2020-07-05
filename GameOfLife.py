import pygame
from random import *

class GameOfLife:
    window_surface = None

    def __init__(self, runner):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.runner = runner
        self.death_color = (0, 0, 0)
        self.alive_color = (255, 0, 0)
        self.scale = 8

    def launch(self):
        self.window_surface = pygame.display.set_mode((640,480), pygame.RESIZABLE)
        # self.window_surface.fill((0, 255, 0))
        self.treatment(self.runner)

        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
            self.clock.tick(12)

    def treatment(self, runner):
        for round in range(runner.rounds):
            for elements in runner.map:
                for element in elements:
                    i = randint(1,2)
                    color = self.alive_color if i == 1 else self.death_color
                    # color = self.alive_color if element.status == 'alive' else self.death_color
                    cell = pygame.Rect(element.address['x'] * self.scale, element.address['y'] * self.scale, self.scale, self.scale)
                    pygame.draw.rect(self.window_surface, color, cell)

                pygame.display.flip()
            runner.run()
