from flask import Flask, render_template, send_from_directory, request
import os
import main

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/add_page')
def add_page():
    return render_template('add_page.html')

@app.route('/add_page', methods=('GET', 'POST'))
def add_page_r():
    url = request.form['url']
    datas = main.get_data(url)
    data = main.save_data(datas)
    html_page = open("templates/blanks.html", "r").read()
    if data["code"] == 0:
        title = "Страница присутсвует в каталоге"
        text = "<a href='/'>Главная страница</a> | <a href='/add_page'>Добавить страницу</a> <br> <p>" + data["uid"] + " - <a href='" + data["data"]["url"] + "'>"+ data["data"]["title"] + "</a>" + "</p>"
    else:
        title = "Страница добавлена в каталог"
        text = "<a href='/'>Главная страница</a> | <a href='/add_page'>Добавить страницу</a> <br> <p>" + data["uid"] + " - <a href='" + data["data"]["url"] + "'>"+ data["data"]["title"] + "</a>" + "</p>"
    return html_page.format(title=title, text=text)

@app.route('/remove_page')
def remove_page():
    return render_template('remove_page.html')

@app.route('/remove_page', methods=('GET', 'POST'))
def remove_page_r():
    uid = request.form['uid']
    data = main.remove_data(uid)
    html_page = open("templates/blanks.html", "r").read()
    if data["code"] == 0:
        title = "Страница по UID отсутсвует в каталоге"
        text = "<a href='/'>Главная страница</a> | <a href='/remove_page'>Удалить страницу</a> <br> <p>" + uid + "</p>"
    else:
        title = "Страница удалена из каталога"
        text = "<a href='/'>Главная страница</a> | <a href='/remove_page'>Удалить страницу</a> <br> <p>" + data["uid"] + " - <a href='" + data["data"]["url"] + "'>"+ data["data"]["title"] + "</a>" + "</p>"
    return html_page.format(title=title, text=text)

@app.route('/search', methods=('GET', 'POST'))
def search_r():
    text = request.form["text"]
    data = main.load_data(text)
    html_page = open("templates/blanks.html", "r").read()
    if data["code"] == 0:
        title = "Поиск не дал результатов"
        text = "<a href='/'>Главная страница</a> | <a href='/add_page'>Добавить страницу</a> <br> <p>" + text + "</p>"
    else:
        title = "Поиск по запросу '" + text + "' успешен"
        text = "<a href='/'>Главная страница</a> | <a href='/add_page'>Добавить страницу</a> <br> "
        for one_page in data["results"]:
            add_text = "<p>" + one_page["uid"] + " - <a href='" + one_page["url"] + "'>"+ one_page["title"] + "</a> </p> <br>"
            text += add_text
    return html_page.format(title=title, text=text)

@app.route('/statics/<string:file_name>')
def statics(file_name):
    return send_from_directory(os.getcwd()+"/static", file_name)

app.run(host="localhost", port=9283)