import pygame

class GameOfLife:
    '''Class used to setup a pygame window and
    display all of the runner map states'''

    window_surface = None

    def __init__(self, runner):
        pygame.init()
        self.runner = runner
        self.death_color = (0, 0, 0)
        self.alive_color = (255, 0, 0)
        self.scale = 8

    def launch(self):
        self.window_surface = pygame.display.set_mode((self.runner.size*self.scale,self.runner.size*self.scale))
        self.treatment(self.runner)

        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False

    def treatment(self, runner):
        while runner.rounds >= 0:
            for elements in runner.map:
                for element in elements:
                    color = self.alive_color if element.status == 'alive' else self.death_color
                    cell = pygame.Rect(element.address['x'] * self.scale, element.address['y'] * self.scale, self.scale, self.scale)
                    pygame.draw.rect(self.window_surface, color, cell)

                pygame.display.flip()
                pygame.time.delay(5)
            runner.run()
