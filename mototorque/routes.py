from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Lexicon, User


@app.route("/")
def home():
    return render_template("index.html")
