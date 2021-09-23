from flask import Flask, request, make_response
import os
import datetime
from random import choice


app = Flask('My 1st app')


@app.route("/")
def home():
    return '<p>Nope!<p>'


@app.route("/whoami/")
def whoami():
    return (str(request.user_agent) + '<br>' + str(request.remote_addr) + '<br>' + str(datetime.datetime.now()))


@app.route("/source_code/")
def source_code():
    with open("app.py", 'r') as f:
        source = f.read()
    return str(source)


@app.route("/random/")
def random():
    a = ''
    letters = ['w','q','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    symbols = ['!','"','№',';','%',':','?','*','(',')','_','+']
    digits0_9 = ['0','1','2','3','4','5','6','7','8','9']
    if 'specials' in request.args:
        if request.args['specials'] == '1':
            letters += symbols
    if 'digits' in request.args:
        if request.args['digits'] == '1':
            letters += digits0_9
    for i in range(int(request.args["length"])):
        a += str(choice(letters))
    b = ''
    for key in request.args:
        b += str(key) + " "
    return a


if __name__ == "__main__":
    app.run(debug=True)

