import pygame

class GameOfLife:

    def __init__(self, values):
        self.values = values

    def launch(self):
        pygame.init()
        self.window_surface = pygame.display.set_mode((640,480), pygame.RESIZABLE)
        launched = True
        print(self.values)
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False