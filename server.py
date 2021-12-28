from flask import Flask, render_template, send_from_directory
import os
import main

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/static/<str:file_name>')
def static(file_name):
    return send_from_directory(os.getcwd()+"/static/"+file_name, file_name)