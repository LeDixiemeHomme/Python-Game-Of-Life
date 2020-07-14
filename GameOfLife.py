import pygame

class GameOfLife:
    '''Class used to setup a pygame window and
    display all of the runner map states'''

    window_surface = None

    def __init__(self, runner):
        pygame.init()
        self._runner = runner
        self._death_color = (0, 0, 0)
        self._alive_color = (255, 0, 0)
        self._scale = 8

    def launch(self):
        self.window_surface = pygame.display.set_mode((self._runner.size*self._scale,self._runner.size*self._scale))
        self.treatment(self._runner)

        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False

    def treatment(self, runner):
        while runner.rounds >= 0:
            for elements in runner.map:
                for element in elements:
                    color = self._alive_color if element.status == 'alive' else self._death_color
                    cell = pygame.Rect(element.address['x'] * self._scale, element.address['y'] * self._scale, self._scale, self._scale)
                    pygame.draw.rect(self.window_surface, color, cell)

                pygame.display.flip()
                pygame.time.delay(5)
            runner.run()