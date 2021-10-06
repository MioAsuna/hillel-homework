import string

from flask import Flask, request, make_response
import os
import datetime
from random import choice

app = Flask('My 1st app')


@app.route("/")
def home():
    return f"""
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Random string</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.1/examples/sign-in/">
  

    <style>
      .bd-placeholder-img {{
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }}

      @media (min-width: 768px) {{
        .bd-placeholder-img-lg {{
          font-size: 3.5rem;
        }}
      }}
    </style>

    
    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">
  </head>
  <body class="text-center">
    
  <form method='GET'>
    <img class="mb-4" src="https://media.discordapp.net/attachments/603406472390639678/892162456493887508/Starege.gif" alt="" width="72" height="57">
    <h1 class="h3 mb-3 fw-normal">Please, put length from 1 to 100 and check if u wanna specials and digits</h1>

    <div class="form-floating">
      <input type="number" name ="length"/>
      <label>Length</label>
    </div>
    <div class="form-floating">
      <input type="checkbox" name = "specials" value='1'/>
      <label>Specials</label>
    </div>
    </div>
    <div class="form-floating">
      <input type="checkbox" name = 'numbers' value='1'>
      <label>Numbers</label>
    </div>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Send</button>
    <p class="mt-5 mb-3 text-muted">&copy; 2021</p>
  </form>
</main>


    
  </body>
</html>

    """


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
    letters = ['w', 'q', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
               'c', 'v', 'b', 'n', 'm']
    symbols = ['!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+']
    digits0_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if 'specials' in request.args:
        if request.args['specials'] == '1':
            letters += symbols
    if 'digits' in request.args:
        if request.args['digits'] == '1':
            letters += digits0_9
    for i in range(int(request.args["length"])):
        a += str(choice(letters))
    return a


if __name__ == "__main__":
    app.run(debug=True)
