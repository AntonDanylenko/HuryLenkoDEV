#Anton Danylenko
#SoftDev pd8
#Classwork
#2018-09-20

import random

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

diction = {}

def convertToDict(filename):
    f = open(filename, 'r')
    text = f.read().split("\n")
    for x in range (1, len(text)- 2):
        cat = text[x].split(',', 1)
        title = cat[0]
        percent = float(cat[-1])
        diction[title] = percent

def randomOcc():
    randlist = []
    for key in diction:
        current = diction[key]
        freq = int(current *10)
        for i in range (freq):
            randlist.append(key)
    print (random.choice(randlist))


@app.route('/occupations')
def test():
    return render_template('template2.html',
                               title = "Occupations",
                               heading = "This file selects a random occupation from the table below and displays it at the top.",
                               collection = diction)

if __name__ == "__main__":
    app.debug = True
    app.run()
