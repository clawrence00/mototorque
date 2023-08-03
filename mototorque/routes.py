from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Dictionary, Users

# Routes for navigation


@app.route("/")
def home():
    return render_template("index.html")


@ app.route('/browse', methods=['GET', 'POST'])
def browse():
    selected_letter = request.args.get('type')
    print(selected_letter)  # <-- should print letter
    words = list(Dictionary.query.filter(
        Dictionary.word_phrase.startswith(selected_letter)).all())
    return render_template("browse.html", letter=selected_letter, words=words)

# Routes for user


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/enter_user")
def enter_user():
    return render_template("enter_user.html")

# Routes for CRUD records


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


@app.route("/edit_word/<int:word_id>", methods=["GET", "POST"])
def edit_word(word_id):
    word = Dictionary.query.get_or_404(word_id)
    if request.method == "POST":
        word.word_phrase = request.form.get("word_phrase"),
        word.definition = request.form.get("definition"),
        word.example = request.form.get("example"),
        db.session.commit()
        return render_template("index.html")
    return render_template("edit.html", word=word)


@app.route("/delete_word/<int:word_id>")
def delete_word(word_id):
    word = Dictionary.query.get_or_404(word_id)
    db.session.delete(word)
    db.session.commit()
    return redirect(url_for("home"))
