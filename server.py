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
        text = "<p>" + data["uid"] + " - " + data["data"]["title"] + "<br>" + data["data"]["url"] + "</p>"
    else:
        title = "Страница добавлена в каталог"
        text = "<p>" + data["uid"] + " - " + data["data"]["title"] + "<br>" + data["data"]["url"] + "</p>"
    return html_page.format(title=title, text=text)
    
@app.route('/statics/<string:file_name>')
def statics(file_name):
    return send_from_directory(os.getcwd()+"/static", file_name)

app.run(host="localhost", port=9283)