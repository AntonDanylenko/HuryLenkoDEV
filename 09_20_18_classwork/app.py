#Anton Danylenko
#SoftDev pd8
#Classwork
#2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

if __name__ == "__main__":
    app.debug = True
    app.run()
