from flask import Flask, render_template, send_from_directory
import os
import main

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/add_page')
def add_page():
    return render_template('add_page.html')
    
@app.route('/statics/<string:file_name>')
def statics(file_name):
    return send_from_directory(os.getcwd()+"/static", file_name)

app.run(host="localhost", port=9283)