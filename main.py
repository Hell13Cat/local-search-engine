import db
import requests
from bs4 import BeautifulSoup
import wget
import os
import cfscrape

def whatisthis(s):
    if isinstance(s, str):
        print("ordinary string")
    elif isinstance(s, unicode):
        print("unicode string")
    else:
        print("not a string")
    print(type(s))

def get_data(url):
    datas = {}
    scraper = cfscrape.CloudflareScraper()
    req = scraper.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    datas["url"] = url
    datas["title"] = soup.find("title").text
    datas["text"] = (soup.find("body").text).replace("\\n", " ")
    whatisthis(datas["text"])
    return datas