from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for spidername in spider_list:
            print( "*********cralall spidername************" + spidername)
            self.crawler_process.crawl(spidername, **opts.__dict__)
        self.crawler_process.start()





























