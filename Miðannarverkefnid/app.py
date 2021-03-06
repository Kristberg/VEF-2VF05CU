from flask import Flask, flash, redirect, render_template, request, json
import os
import urllib.request
from jinja2 import ext
from datetime import datetime

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode())

def format_time(gogn):
    return datetime.strptime(gogn, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d. %m. %Y kl. %H:%M')

app.jinja_env.add_extension(ext.do)

app.jinja_env.filters['format_time'] = format_time

@app.route('/')
def index():
    return render_template('index.tpl', gogn=gogn)

@app.route('/company/<company>')
def comp(company):
    return render_template('company.tpl', gogn=gogn, com=company)

@app.route('/moreinfo/<key>')
def info(key):
    return render_template('moreinfo.tpl', gogn=gogn, k=key)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.tpl'), 404


if __name__ == "__main__":
    app.run(debug=True)
