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
            return {"code":0, "uid":one_page, "data":data[one_page]}
    add_page = 1
    while add_page == 1:
        id_page = extf.gen_id()
        if id_page not in data:
            add_page = 0
    data[id_page] = datas
    print(data)
    db.save("pages", data)
    return {"code":1, "uid":id_page, "data":datas}

def load_data(text):
    try:
        data = db.load("pages")
    except:
        data = {"0":{"url":"0", "title":"0", "text":""}}
    res = []
    code = 0
    for one_page in data.keys():
        if text in data[one_page]["text"]:
            datas = data[one_page]
            datas["uid"] = one_page
            res.append(datas)
            code = 1
    return {"code":code, "results":res}

def remove_data(uid):
    try:
        data = db.load("pages")
    except:
        data = {"0":{"url":"0", "title":"0", "text":""}}
    if uid not in data:
        return {"code":0}
    datas = data[uid]
    del data[uid]
    db.save("pages", data)
    return {"code":1, "uid":uid, "data":datas}