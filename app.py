#Anton Danylenko
#SoftDev
#09-27-18

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inputTemplate.html')

@app.route('/auth')
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template('outputTemplate.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
