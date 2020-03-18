from sys import argv
from scrapy import Spider


RESULT_FILE_PATH = [arg.split('OUTPUT=')[1]
                    for arg in argv if '-s OUTPUT=' in arg][0]


class WebCrawler(Spider):

    name = 'magnet-finder'

    def __init__(self):
        self.start_urls = [arg.split('URL=')[1]
                           for arg in argv if '-s URL=' in arg]

    def parse(self, response):
        body = response.body_as_unicode()

        links = body.split('<body>')[1].split('</body>')[0].split('<a')
        links = map(lambda link: link.split("</a>")[0], links)

        magnet_links = filter(lambda link: 'magnet' in link, links)
        magnet_links = map(lambda link: link.split("'")[1], magnet_links)

        with open(RESULT_FILE_PATH, mode='w') as result_file:
            result_file.write('\n'.join(magnet_links))
