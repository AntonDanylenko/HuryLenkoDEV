#Anton Danylenko
#SoftDev
#13 Echo Echo Echo
#09-28-18

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inputTemplate.html')

@app.route('/auth', methods=['POST'])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.method)
    usrname=request.form["usrname"]
    return render_template('outputTemplate.html',
                            username = usrname,
                            method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
