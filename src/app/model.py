from src import RESULT_FILE_PATH


class Model(object):

    def __init__(self):
        self.links = []

    def run(self):
        self.links = [f'Magnet Link {i}' for i in range(1, 21)]

    def load_result_file(self):
        with open(RESULT_FILE_PATH, mode='r') as result_file:
            self.links = result_file.readlines()

    def handle_url(self, url):
        handled_url = url

        if not 'http' in url:
            handled_url = f'https://{handled_url}'

        return handled_url
