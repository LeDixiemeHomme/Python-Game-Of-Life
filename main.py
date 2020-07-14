from tkinter import Tk
from GameOfLife import GameOfLife
from Ihm import IHM
from game.Runner import Runner

input_interface = IHM()

while input_interface.replay:

    input_interface.launch(Tk())
    values = input_interface.getValues()
    if values:
        runner = Runner(size=values[0], rounds=values[1], forms_amount=values[2])
    else:
        print('Running with default parameters ...')
        runner = Runner()

    game_interface = GameOfLife(runner)
    game_interface.launch()

    input_interface.pop_up(Tk())