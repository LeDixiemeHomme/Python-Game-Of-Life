import random
import sys
import asyncio
import threading
from GameOfLife import GameOfLife
from IHM import IHM

IHM = IHM()

IHM.launch()

while IHM.done:
    GOF = GameOfLife(IHM.values)


# while IHM.done == False:
#     asyncio.wait()
#
# GOF = GameOfLife(IHM.values)
# print(GOF.values)