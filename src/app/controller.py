from src import WEB_CRAWLER_PATH, RESULT_FILE_PATH
from subprocess import run as run_command


class Controller(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def run(self):
        events = {}

        events['main'] = {}
        events['header'] = {}

        events['main']['copy_link'] = self.event_copy_link
        events['header']['search_link'] = self.event_search_link

        self.view.run(events=events)
        self.model.run()

        self.view.container.main.load_items(links=self.model.links)

    def find_links(self, url):
        command = ['scrapy', 'runspider',
                   f'-s URL={url}', f'-s OUTPUT={RESULT_FILE_PATH}', '--nolog',
                   WEB_CRAWLER_PATH]

        return run_command(command).returncode

    def event_copy_link(self, event, link):
        self.view.clipboard_clear()
        self.view.clipboard_append(link)

    def event_search_link(self, event):
        user_input = self.view.container.header.search_input.get()

        if not self.model.validate_user_input(user_input):
            return None

        url = self.model.handle_url(url=user_input)

        self.find_links(url=url)
        self.model.load_result_file()
        self.view.container.main.load_items(links=self.model.links)
