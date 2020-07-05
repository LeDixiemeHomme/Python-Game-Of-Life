from tkinter import StringVar, Label, Entry, Button
from functools import partial

class IHM:

    def __init__(self):
        self.values = list()
        self.replay = True

    def data_treatment(self, elements, values, root):
        values.clear()
        for i in elements:
            values.append(i[1].get())
        root.destroy()

    def close(self, root):
        self.replay = False
        root.destroy()

    def retry(self, root):
        root.destroy()

    def launch(self, root):
        title = Label(root, text='PARAMETERS :')
        elements = [(Label(root, text='Dimension'), Entry(root, textvariable=(StringVar(root)))),
                    (Label(root, text='Round number'), Entry(root, textvariable=(StringVar(root))))]
        button = Button(root, text='clic', command=partial(self.data_treatment, elements, self.values, root))

        title.grid(column=0, row=0)
        [value[0].grid(column=0, row=i + 1) for i, value in enumerate(elements)]
        [value[1].grid(column=1, row=i + 1) for i, value in enumerate(elements)]

        button.grid(column=1, row=5)
        root.mainloop()

    def pop_up(self, root):
        title_retry = Label(root, text='Would you like to retry ?')
        buttonYes = Button(root, text='Yes', command=partial(self.retry, root))
        buttonNo = Button(root, text='No', command=partial(self.close, root))

        title_retry.grid(column=0, row=0)

        buttonYes.grid(column=0, row=1)
        buttonNo.grid(column=1, row=1)
        root.mainloop()
