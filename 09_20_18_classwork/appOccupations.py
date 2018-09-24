#Anton Danylenko
#SoftDev pd8
#Classwork
#2018-09-20

import random

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

dict = {}
#initializes the dictionary


def convertToDict(fileName):
    file = open(fileName, "r")
    #open the data file and reads the contents

    flines = file.readlines()[1:]
    #readlines reads the individual lines of the file starting from the second

    for line in flines:
        #print(line)
        quote = False
        #initializes whether or not the occupation is in quotes as false
        occupation = ""
        #initializes the occupation name
        num = False
        #initializes whether we are parsing through the percent as false
        percent = ""
        #initializes the percent string
        for character in line:
            if character == "\"":
                quote = not quote
                #if a char is a quote, either turn quote true to start the quote
                #or turn it false if the quote just ended.
            elif character == ",":
                if quote:
                    occupation += character
                    #if the comma in inside a quote, add it as part of the
                    #occupation name.
                else:
                    num = True
                    #if comma is not inside quote, start recording the percent
            else:
                if num:
                    percent += character
                    #if char is not a quote or a comma, and we are
                    #recording the percent, add the char to the percent string
                else:
                    occupation += character
                    #if char is not quote, comma, or part of the percent number,
                    #add char to the occupation string.
        #print(occupation)
        #print(percent)
        percent = percent.replace("\n", "")
        #newlines were added to the end of the percent string from the end
        #of every line, so we must remove them.
        dict[occupation]= (float)(percent)

convertToDict("data/occupations.csv")

@app.route('/occupations')
def test():
    return render_template('template2.html',
                               title = "Occupations",
                               heading = "This file selects a random occupation from the table below and displays it at the top.",
                               collection = dict)

if __name__ == "__main__":
    app.debug = True
    app.run()
