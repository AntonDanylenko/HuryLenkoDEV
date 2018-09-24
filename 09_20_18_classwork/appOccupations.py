#Anton Danylenko and Susan Lin
#SoftDev pd8
#10 Jinja Tuning
#2018-09-23

from flask import Flask, render_template
app = Flask(__name__)

import random
diction = {}

def convertToDict(filename):
    f = open(filename, 'r')
    text = f.read().split("\n")
    print(text)
    for x in range (1, len(text)- 2):
        cat = text[x].rsplit(',', 1)
        title = cat[0].strip('"')
        percent = float(cat[-1])
        diction[title] = percent

def randomOcc():
    randlist = []
    for key in diction:
        current = diction[key]
        freq = int(current *10)
        for i in range (freq):
            randlist.append(key)
    return (random.choice(randlist))

@app.route('/')
def home():
    return 'Welcome <br> <a href="/occupations"> Occupations </a>'

@app.route('/occupations')
def test():
    convertToDict('data/occupations.csv')
    return render_template('temp01.html',
                               title = "Occupations",
                               heading = "This file selects a random occupation from the table below and displays it at the top.",
                               collection = diction,
                               occupation = "this is your occupation: " + randomOcc())

if __name__ == "__main__":
    app.debug = True
    app.run()
