from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': '/home/himanshu/Documents/Projects/GIT/myexp/crawler/icrawler/download'})
    # FOR MORE ON FILTERS : icrawler/builtin/google.py
filters = dict(
    size='=200x200',        # large, medium, icon, >[]x[], =[]x[] ([] is an integer)          e.g. '=100x100'
    type='photo',           # photo, face, clipart, linedrawing, animated
    # color='orange',
    # license='commercial,modify',
    # date=((2017, 1, 1), (2017, 11, 30))
    )
google_crawler.crawl(keyword='natural pumpkin', filters=filters, max_num=20, file_idx_offset=0)