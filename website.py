#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template('patrol.html')


@app.route('/hello/')
def hello():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
