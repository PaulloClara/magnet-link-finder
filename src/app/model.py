from src import RESULT_FILE_PATH


class Model(object):

    def __init__(self):
        self.links = []

    def run(self):
        self.links = [f'Magnet Link {i}' for i in range(1, 21)]

    def load_result_file(self):
        with open(RESULT_FILE_PATH, mode='r') as result_file:
            self.links =\
                [line.replace('\n', '') for line in result_file.readlines()]

    def validate_user_input(self, user_input):
        if not user_input.strip():
            return False

        return True

    def handle_url(self, url):
        handled_url = url

        if not 'http' in url:
            handled_url = f'https://{handled_url}'

        return handled_url
