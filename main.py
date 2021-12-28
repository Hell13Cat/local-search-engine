import db
from bs4 import BeautifulSoup
import wget
import os
import cfscrape
import extf

def get_data(url):
    datas = {}
    scraper = cfscrape.CloudflareScraper()
    req = scraper.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    datas["url"] = url
    datas["title"] = soup.find("title").text
    datas["text"] = (soup.find("body").text).replace("\\n", " ")
    return datas

def save_data(datas):
    try:
        data = db.load("pages")
    except:
        data = {"0":{"url":"0", "title":"0", "text":""}}
    for one_page in data.keys():
        if datas["url"] == data[one_page]["url"]:
            return {"code":1}
    add_page = 1
    while add_page == 1:
        id_page = extf.gen_id()
        if id_page not in data:
            add_page = 0
    data[id_page] = datas
    print(data)
    db.save("pages", data)
