import lxml
import requests
from bs4 import BeautifulSoup
import parse
from datetime import datetime
import json
from requests_html import HTMLSession
from ..models import News as NewsModel

from django.db import IntegrityError


class News:
    def __init__(self):

        self.b = self.get_soup()
        self.c = self.parse_links()

    def get_request(self, url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        }
        html_data = requests.get(url, headers=headers)
        return html_data.text

    def get_soup(self, url="https://www.nyasatimes.com/"):
        soup = BeautifulSoup(self.get_request(url), "lxml")
        return soup

    def process_nyasatimes(self):
        links_list = []
        content = self.b
        segment = content.find("div", {"class": "float just-in"})
        links = segment.find_all("a")
        for link in links:
            links_list.append(link["href"])

        return links_list

    def parse_links(self):
        news_links = self.process_nyasatimes()
        for link in news_links:
            try:
                content = self.get_soup(link)
                heading = content.find("h1", {"class": "nyasa-title"}).text
                image = content.find("figure").find("img")["src"]
                description = (
                    content.find("div", {"class": "nyasa-content"}).find("p").text
                )
                try:
                    NewsModel.objects.create(
                        heading=heading,
                        description=description,
                        image=image,
                        source="nyasatimes",
                        link=link,
                    )
                except IntegrityError:
                    pass
            except:
                print("I tried")