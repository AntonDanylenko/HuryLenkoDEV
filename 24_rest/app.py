import urllib, json

from flask import Flask, render_template
app = Flask(__name__)

response = urllib.urlopen('https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY')
data = json.load(response)
print data

@app.route('/')
def home():
    return render_template('app.html', pic = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
