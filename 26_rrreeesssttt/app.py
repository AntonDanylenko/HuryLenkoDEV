# Anton Danylenko
# SoftDev1 pd8
# K26 -- Getting More REST
# 2018-11-15

import urllib, json

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    key = "3jCeyqY6wdYGtAWft"
    url = "http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key="
    full = url + key
    response = urllib.request.urlopen(full)
    respRead = response.read()
    data = json.loads(respRead)
    print(data)
    return render_template('app.html', collection = data['data'])

if __name__ == "__main__":
    app.debug = True
    app.run()
