from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Lexicon, Users


@app.route("/")
def home():
    # lexicon = list(Task.query.order_by(Task.id).all())
    return render_template("base.html")
