#Anton Danylenko and Susan Lin
#SoftDev pd8
#10 Jinja Tuning
#2018-09-23

from flask import Flask, render_template
app = Flask(__name__)

import random
diction = {}

def convertToDict(filename):
    text = open(filename, 'r').read().split("\n")
    #turns the csv file into a list separated by commas
    for x in range (1, len(text)- 2):
        cat = text[x].rsplit(',', 1)
        #splits each string in text into title and percent
        title = cat[0].strip('"')
        #removes quotes from title
        percent = float(cat[-1])
        #typecasts the percent into a float
        diction[title] = percent
        #sets the value of the title key in diction to percent

def findLast():
    diff = 100.0
    for key in diction:
        diff -= diction[key]
        #subtracts percent of each occupation from total
    return ("%.1f" % diff)
    #rounds the difference to the nearest tenth

def randomOcc():
    randlist = []
    for key in diction:
        current = diction[key]
        #stores the percent of each title
        freq = int(current *10)
        #we are storing each title by percent (x10 to rid decimal) in a list
        for i in range (freq):
            randlist.append(key)
        #returns a randomly selected occupation
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
                               occupation = "this is your occupation: " + randomOcc(),
                               percentage = findLast())

if __name__ == "__main__":
    app.debug = True
    app.run()
