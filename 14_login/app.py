#Box2 - Anton Danylenko, Simon Tsui
#SoftDev1 pd8
#K14 -- Do I know you?
#2018-10-01

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

@app.route("/")
def start():
    #if ((session["usrname"] == "addis") and (session["pswrd"] == "ababa")):
        #return render_template("auth.html", a = session["usrname"])
    #else:
    return render_template("login.html")


@app.route("/auth", methods = ['GET'])
def authenticate():
    #print(url_for('authenticate'))
    session["usrname"] = request.args["Username"]
    session["pswrd"] = request.args["Password"]
    if (session["usrname"] == 'addis' and session["pswrd"] == 'ababa'):
        return redirect(url_for("start"))
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

#@app.route("/display_login")
#def success():
#    print(request.args)
    # return render_template("auth.html", a = request.args['Username'])
#    return render_template("auth.html", a = usr_input["Username"])


if __name__ == "__main__":
    app.debug = True
    app.run()
