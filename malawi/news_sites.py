from .code.times import News as times_news
from .code.zodiak import News as zodiak_news
from .code.nyasatimes import News as nyasatimes_news
from .code.scraper import News as national_news


def run_code():
    try:
        times_news()
    except:
        print("times has issues")
    try:
        zodiak_news()
    except:
        print("zodiak has issues")

    try:
        national_news()
    except:
        print("malawi nation has issues")

    try:
        nyasatimes_news()
    except:
        print("nyasatimes has issues")