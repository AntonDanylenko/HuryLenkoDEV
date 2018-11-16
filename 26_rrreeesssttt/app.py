# Anton Danylenko
# SoftDev1 pd8
# K26 -- Getting More REST
# 2018-11-15

import urllib, json

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/dogs')
def dog():
    response = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    respRead = response.read()
    data = json.loads(respRead)
    return render_template('dogs.html', pic = data['message'])

@app.route('/books')
def book():
    response = urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699")
    respRead = response.read()
    data = json.loads(respRead)
    #print(data)
    return render_template('books.html', collection = data['items'])

@app.route('/trivia')
def trivia():
    response = urllib.request.urlopen("https://opentdb.com/api.php?amount=10")
    respRead = response.read()
    data = json.loads(respRead)
    #print(data)
    return render_template('trivia.html', collection = data['results'])

if __name__ == "__main__":
    app.debug = True
    app.run()
