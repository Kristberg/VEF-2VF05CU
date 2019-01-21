import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <h1>Hello user</h1>
    <img src="http://loremflickr.com/600/400">
    <p><a href="/sida2"title ="Síða 2">Síða 2</a> | <a href="/sida3"title ="Síða 3">Síða 3</a></p>
    """

@app.route("/sida2")
def sida2():
    return"""
    <h1>Hello user</h1>
    <img src="http://loremflickr.com/600/400">
    <p><a href="/"title ="Síða 1">Síða 1</a> | <a href="/sida3"title ="Síða 3">Síða 3</a></p>
    """


@app.route("/sida3")
def sida3():
    return"""
    <h1>Hello user</h1>
    <img src="http://loremflickr.com/600/400">
    <p><a href="/"title ="Síða 1">Síða 1</a> | <a href="/sida2"title ="Síða 2">Síða 2</a></p>
    """




if __name__ == '__main__':
  # app.run(debug=True, use_reloader=True)
    app.run()
