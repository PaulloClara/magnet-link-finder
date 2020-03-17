class View(object):

    def __init__(self):
        self.events = {}

    def run(self, events):
        self.events = events

        print('Hello World')
