#Anton Danylenko
#SoftDev pd8
#Classwork
#2018-09-20

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

coll = [0,1,1,2,3,5,8]

@app.route('/my_foist_template')
def test():
    return render_template('template.html',
                               title = "Title",
                               collection = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
