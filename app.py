from flask import Flask, request
from flask import render_template
# import test
# import json
# import requests
# import random
app = Flask(__name__)


##
# Index/Home Route
##################
@app.route('/home', methods=['GET'])
@app.route('/')
def index():
    return render_template('home.html')

##
# Results Route
###############
# @app.route('/resultloop', methods=['POST'])
# def resultloop():
#     searchterms = request.form['searchterms']
#     r = requests.get(("http://api.giphy.com/v1/gifs/search?q="
#                     + searchterms
#                     + "&api_key=02KjSiPr9Ur2Hizm8HsEdgB0NXPJiNBh&limit=50"))
#     r = r.json()
#     gifs_list = []
#     for x in range(50):
#         a = r['data'][x]['images']['original']['url']
#         gifs_list.append(a)
#     randomers = random.sample(range(50), 25)
#     resultloop = [gifs_list[i] for i in randomers]
#     return render_template('resultloop.html', resultloop=resultloop)
