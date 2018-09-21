#Anton Danylenko
#SoftDev pd8
#Classwork
#2018-09-20

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

@app.route('/occupations')
def test():
    return render_template('template2.html',
                               title = "Occupations",
                               heading = "This file selects a random occupation from the table below and displays it at the top.")

if __name__ == "__main__":
    app.debug = True
    app.run()
