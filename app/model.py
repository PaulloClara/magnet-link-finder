class Model(object):

    def __init__(self):
        self.links = []

    def run(self):
        self.links = [f'Magnet Link {i}' for i in range(20)]

    def load_result_file(self):
        with open('app/temp/results.txt', mode='r') as resultFile:
            self.links = resultFile.readlines()

    def handle_url(self, url):
        handled_url = url

        if not 'http' in url:
            handled_url = f'https://{handled_url}'

        return handled_url
