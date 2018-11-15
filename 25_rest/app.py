# Anton Danylenko
# SoftDev1 pd8
# K25 -- Getting More REST
# 2018-11-14

import urllib, json

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    response = urllib.request.urlopen("http://developer.epa.gov/api/index.php/api_repellent?api=repellent")
    respRead = response.read()
    data = json.loads(respRead)
    print(data)
    return render_template('app.html', collection = data['api_repellent'])

if __name__ == "__main__":
    app.debug = True
    app.run()
