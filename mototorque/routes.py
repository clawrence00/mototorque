from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Lexicon, User


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route('/browse', methods=['GET', 'POST'])
def browse():
    selected_letter = request.args.get('type')
    print(selected_letter)  # <-- should print letter
    return render_template("browse.html", letter=selected_letter)
