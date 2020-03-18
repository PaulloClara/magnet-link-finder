from sys import argv
from scrapy import Spider


class WebCrawler(Spider):

    name = 'magnet-finder'

    def __init__(self):
        self.start_urls = [arg.split('URL=')[1]
                           for arg in argv if 'URL=' in arg]

    def parse(self, response):
        body = response.body_as_unicode()

        links = body.split('<body>')[1].split('</body>')[0].split('<a')
        links = map(lambda link: link.split("</a>")[0], links)

        magnetLinks = filter(lambda link: 'magnet' in link, links)
        magnetLinks = map(lambda link: link.split("'")[1], magnetLinks)

        with open('app/temp/results.txt', mode='w') as resultFile:
            resultFile.write('\n'.join(magnetLinks))
