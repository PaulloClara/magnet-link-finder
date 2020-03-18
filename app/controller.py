from subprocess import run as run_command


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

    def find_links(self, url):
        command = ['scrapy', 'runspider',
                   f'-s URL={url}', '--nolog',
                   'app/web-crawler.py']
        result = run_command(command)

        return result.returncode

    def event_copy_link(self, event, link):
        print(link)

    def event_search_link(self, event):
        user_input = self.view.main_container.header_container.search_input.get()
        url = self.model.handle_url(url=user_input)

        self.find_links(url=url)
        self.model.load_result_file()
