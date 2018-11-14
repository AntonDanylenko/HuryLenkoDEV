# Anton Danylenko
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-13

import urllib, json

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    response = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
    respRead = response.read()
    data = json.loads(respRead)
    #print(data)
    return render_template('app.html', pic = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
