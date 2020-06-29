from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial
import threading

class IHM:

    def __init__(self):
        self.root = Tk()
        self.values = list()
        self.done = False
        self.title = Label(self.root, text='PARAMETERS :')
        self.elements = [(Label(self.root, text='un élément'), Entry(self.root, textvariable=(StringVar(self.root)))),
                    (Label(self.root, text='un autre élément'), Entry(self.root, textvariable=(StringVar(self.root))))]
        self.button = Button(self.root, text='clic', command=partial(self.data_treatment, self.elements, self.values))

    def data_treatment(self,elements, values):
        for i in elements:
            values.append(i[1].get())
        self.done = True
        self.root.destroy()

    def launch(self):
        self.title.grid(column=0, row=0)
        [value[0].grid(column=0, row=i + 1) for i, value in enumerate(self.elements)]
        [value[1].grid(column=1, row=i + 1) for i, value in enumerate(self.elements)]

        self.button.grid(column=1, row=5)
        self.root.mainloop()