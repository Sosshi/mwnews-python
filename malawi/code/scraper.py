import bs4 as bs
import urllib.request
from ..models import News as NewsModel

from django.db import IntegrityError


class News:
    def __init__(self):
        self.a = self.open_url()
        self.b = self.process()

    def open_url(self):
        source = urllib.request.urlopen(
            "https://www.mwnation.com/section/news/national-news/"
        ).read()
        soup = bs.BeautifulSoup(source, "lxml")
        return soup

    def process(self):
        national_news = self.a
        articles = national_news.find_all("article")

        for article in articles:
            try:
                link = article.find("a")["href"]
                image = article.find("img")["data-src"]
                paragraph = article.find("p").text
                heading = article.find("h3").find("a").text
                try:
                    NewsModel.objects.create(
                        heading=heading,
                        description=paragraph,
                        image=image,
                        source="Malawi Nation",
                        link=link,
                    )
                except IntegrityError:
                    pass
            except TypeError:
                print("I tried")