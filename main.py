from tkinter import Tk
from GameOfLife import GameOfLife
from Ihm import IHM

input_interface = IHM()

while input_interface.replay:

    input_interface.launch(Tk())
    print(input_interface.values)
    game_interface = GameOfLife(input_interface.values)
    game_interface.launch()
    input_interface.pop_up(Tk())
