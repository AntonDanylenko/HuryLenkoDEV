#Box2 - Anton Danylenko, Simon Tsui
#SoftDev1 pd8
#K15 Oh yes, perhaps I do...
#2018-10-03

import os
from flask import Flask
from flask import session
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response

login_info = {"addis": "ababa"}
usr_input = {}
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def start():
    return render_template("login.html")

@app.route("/logout")
def back():
    session.pop("usrname")
    session.pop("pswrd")
    return redirect(url_for("start"))


@app.route("/auth", methods = ['GET'])
def authenticate():
    session["usrname"] = request.args["Username"]
    session["pswrd"] = request.args["Password"]
    if (session["usrname"] == 'addis' and session["pswrd"] == 'ababa'):
        return redirect(url_for("success"))
    else:
        return redirect(url_for('display_login'))

@app.route("/again")
def display_login():
    if(session["usrname"] != "addis" and session["pswrd"] != "ababa"):
        return render_template("failed.html", a  = "Username and Password ")
    elif(session["usrname"] != "addis"):
        return render_template("failed.html", a = "Username")
    else:
        return render_template("failed.html", a = "Password")

@app.route("/display_login")
def success():
    return render_template("auth.html", a = session["usrname"])


if __name__ == "__main__":
    app.debug = True
    app.run()
