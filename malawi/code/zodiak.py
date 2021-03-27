from django.db.utils import IntegrityError
import lxml
import requests
from bs4 import BeautifulSoup
import parse
from datetime import datetime
import json
from requests_html import HTMLSession
from ..models import News as NewsModel


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

    def get_soup(self, url="https://www.zodiakmalawi.com/nw-2"):
        soup = BeautifulSoup(self.get_request(url), "lxml")
        return soup

    def process_zodiak(self) -> list:
        links_list = []
        zodiak_news = self.b
        article_segment = zodiak_news.find("div", {"id": "sunfw_section_compoment"})
        h3_headers = article_segment.find_all("h3")
        for header in h3_headers:
            try:
                link = header.find("a")
                links_list.append(link["href"])
            except:
                print("I tried")
        return links_list

    def parse_links(self):
        zodiak_links = self.process_zodiak()
        for link in zodiak_links:
            new_link = "https://www.zodiakmalawi.com" + link
            content = self.get_soup(new_link)
            header = content.find("h2", {"class": "itemTitle"}).text
            description = content.find("div", {"class": "itemIntroText"}).find("p").text
            image = content.find("div", {"class": "itemImageBlock"}).find("img")["src"]

            try:
                NewsModel.objects.create(
                    heading=header,
                    description=description,
                    image="https://www.zodiakmalawi.com" + image,
                    source="Zodiak Malawi",
                    link=new_link,
                )
            except IntegrityError:
                pass