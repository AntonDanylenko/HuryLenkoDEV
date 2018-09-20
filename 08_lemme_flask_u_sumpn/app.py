#Anton Danylenko
#SoftDev pd8
#08_lemme_flask_u_sumpn
#2018-09-19

from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloW():
    return "Hello World!"

@app.route("/us")
def helloUS():
    return "Hello US!"

@app.route("/us/ny")
def helloNY():
    return "Hello New York!"

if __name__ == "__main__":
    app.debug = True
    app.run()
