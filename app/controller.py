class Controller(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def run(self):
        events = {}

        self.view.run(events=events)
        self.model.run()
