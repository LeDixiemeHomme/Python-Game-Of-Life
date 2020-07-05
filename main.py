from tkinter import Tk
from GameOfLife import GameOfLife
from Ihm import IHM
from game.Runner import Runner

input_interface = IHM()

while input_interface.replay:

    input_interface.launch(Tk())
    runner = Runner()
    # runner = Runner(input_interface.values) initialliser le runner avec les valeurs [dimension, rounds]
    game_interface = GameOfLife(runner)
    game_interface.launch()

    input_interface.pop_up(Tk())