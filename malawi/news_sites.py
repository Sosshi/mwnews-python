from .code.times import News as times_news
from .code.zodiak import News as zodiak_news
from .code.nyasatimes import News as nyasatimes_news
from .code.scraper import News as national_news


def run_code():
    times_news()
    zodiak_news()
    national_news()
    nyasatimes_news()
