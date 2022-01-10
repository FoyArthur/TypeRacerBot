from flask import Flask, render_template, request
from time import sleep
from threading import Thread
from typeracerhack import *



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def startHack(link):
    sleep(0.05)
    execute(link)

def threadHack(link):
    thr = Thread(target = startHack, args = [link])
    thr.start()
    return thr



@app.route("/", methods = ["POST"])
def posted():
    link = request.form.get('input')
    threadHack(link)
    return render_template('link.html', name=link)
