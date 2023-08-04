from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Dictionary, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


# Routes for navigation


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/signup", methods=["GET", "POST"])
def signup():
    our_users = list(Users.query.order_by(Users.id).all())
    return render_template("signup.html", our_users=our_users)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user:
            if check_password_hash(user.password_hash, request.form.get("password_hash")):
                login_user(user)
                return redirect(url_for('add_word'))
    return render_template("signin.html")

# Routes for Users

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()
        if user is None:
            hash_password = generate_password_hash(request.form.get("password_hash"))
            user = Users(
            username=request.form.get("username"),
            email=request.form.get("email"),
            password_hash=hash_password
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("signin"))
    return redirect(url_for("home"))

# Routes for Dictionary

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


# login manager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

#logout function
@app.route("/signout", methods=["GET", "POST"])
@login_required
def signout():
    logout_user()
    return redirect(url_for("signin"))

@ app.route('/browse', methods=['GET', 'POST'])
def browse():
    selected_letter = request.args.get('type')
    print(selected_letter)  # <-- should print letter
    words = list(Dictionary.query.filter(
        Dictionary.word_phrase.startswith(selected_letter)).all())
    return render_template("browse.html", letter=selected_letter, words=words)