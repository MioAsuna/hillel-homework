#!/usr/bin/env python
 # -*- coding: utf-8 -*-
import string

from flask import Flask, request, make_response
import os
import datetime
from random import choice

app = Flask('My 1st app')


@app.route("/")
def home():
    return "Yes"


@app.route("/whoami/")
def whoami():
    return str(request.user_agent) + '<br>' + str(request.remote_addr) + '<br>' + str(datetime.datetime.now())


@app.route("/source_code/")
def source_code():
    with open("app.py", 'r') as f:
        source = f.read()
    return str(source)


@app.route("/random/")
def random():
    a = ''
    random_pool = string.ascii_letters
    if 'specials' in request.args:
        if request.args['specials']:
            random_pool += string.punctuation
    if 'digits' in request.args:
        if request.args['digits']:
            random_pool += string.digits
    for i in range(int(request.args["length"])):
        a += choice(random_pool)
    return a


if __name__ == "__main__":
    app.run(debug=True)