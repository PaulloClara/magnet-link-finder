from app.view import View
from app.model import Model
from app.controller import Controller


class App(object):

    def __init__(self):
        self.view = View()
        self.model = Model()

        self.controller = Controller(view=self.view, model=self.model)

    def run(self):
        self.controller.run()
        self.view.mainloop()
