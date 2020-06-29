import pygame

class GameOfLife:

    def __init__(self, values):
        self.values = values
        pygame.init()
        self.window_surface = pygame.display.set_mode((640,480), pygame.RESIZABLE)
        self.font = (255, 255, 255)
        self.color1 = (0, 0, 255)
        self.color2 = (0, 255, 0)
        self.color3 = (255, 0, 0)

    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False