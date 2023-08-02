from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Dictionary, Users


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        word = Dictionary(
            word_phrase=request.form.get("word_phrase"),
            definition=request.form.get("definition"),
            example=request.form.get("example"),
        )
        db.session.add(word)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


# @ app.route('/browse', methods=['GET', 'POST'])
# def browse():
#     selected_letter = request.args.get('type')
#     print(selected_letter)  # <-- should print letter
#     word = list(Dictionary.query.order_by(Dictionary.word_phrase).all())
#     return render_template("browse.html", letter=selected_letter, word=word)

@ app.route('/browse')
def browse():
    entry = list(Dictionary.query.order_by(Dictionary.word_phrase).all())
    return render_template("browse.html", entry=entry)
