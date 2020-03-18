class Controller(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def run(self):
        events = {}

        events['body'] = {}
        events['header'] = {}

        events['body']['copy_link'] = self.event_copy_link
        events['header']['search_link'] = self.event_search_link

        self.view.run(events=events)
        self.model.run()

    def event_copy_link(self, event, link):
        print(link)

    def event_search_link(self, event):
        print('search...')
