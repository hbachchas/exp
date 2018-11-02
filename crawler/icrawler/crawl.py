from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': '/home/himanshu/Documents/Projects/GIT/myexp/crawler/icrawler/download'})
filters = dict(
    size='large',
    color='orange',
    # license='commercial,modify',
    # date=((2017, 1, 1), (2017, 11, 30))
    )
google_crawler.crawl(keyword='cat', filters=filters, max_num=10, file_idx_offset=0)




# google_crawler = GoogleImageCrawler(storage={'root_dir': ''})
# google_crawler.crawl(keyword='cat', max_num=10)
# google_crawler.crawl()