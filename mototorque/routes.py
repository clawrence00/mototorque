from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Words, User


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        word = Words(
            word_phrase=request.form.get("word_phrase"),
            definition=request.form.get("definition"),
            example=request.form.get("example"),
        )
        db.session.add(word)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@ app.route('/browse', methods=['GET', 'POST'])
def browse():
    selected_letter = request.args.get('type')
    print(selected_letter)  # <-- should print letter
    word = list(Words.query.order_by(Words.word_phrase).all())
    return render_template("browse.html", letter=selected_letter, word=word)
