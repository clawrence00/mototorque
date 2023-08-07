from flask import render_template, request, redirect, url_for
from mototorque import app, db
from mototorque.models import Dictionary, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


# Routes for navigation


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/admin")
@login_required
def admin():
    if current_user.username == "admin":
        our_users = list(Users.query.order_by(Users.id).all())
        return render_template('admin.html', our_users=our_users)
    return render_template('index.html')


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        if user:
            if check_password_hash(user.password_hash, request.form.get("password_hash")):
                login_user(user)
                if current_user.username == "admin":
                    return redirect(url_for('admin'))
                return redirect(url_for('home'))
    return render_template("signin.html")


@ app.route('/browse', methods=['GET', 'POST'])
def browse():
    selected = request.args.get('type')
    print(selected)  # <-- should print letter
    if selected == "All":
        words = list(Dictionary.query.order_by(Dictionary.word_phrase).all())
        return render_template("browse.html", letter=selected, words=words)
    words = list(Dictionary.query.filter(
        Dictionary.word_phrase.ilike(f'{selected}%')).all())
    return render_template("browse.html", letter=selected, words=words)

# Routes for Users


@ app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        user=Users.query.filter_by(email=request.form.get("email")).first()
        if user is None:
            hash_password=generate_password_hash(
                request.form.get("password_hash"))
            user=Users(
                username=request.form.get("username"),
                email=request.form.get("email"),
                password_hash=hash_password
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("signin"))
    return redirect(url_for("home"))


@ app.route("/delete_user/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user=Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("admin"))

# Routes for Dictionary


@ app.route("/add_word", methods=["GET", "POST"])
@ login_required
def add_word():
    if request.method == "POST":
        poster=current_user.id
        entry=Dictionary(
            word_phrase=request.form.get("word_phrase"),
            definition=request.form.get("definition"),
            example=request.form.get("example"),
            user_id=poster
        )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@ app.route("/edit_word/<int:word_id>", methods=["GET", "POST"])
def edit_word(word_id):
    word=Dictionary.query.get_or_404(word_id)
    if request.method == "POST":
        word.word_phrase=request.form.get("word_phrase"),
        word.definition=request.form.get("definition"),
        word.example=request.form.get("example"),
        db.session.commit()
        return render_template("index.html")
    return render_template("edit.html", word=word)


@ app.route("/delete_word/<int:word_id>", methods=["GET", "POST"])
def delete_word(word_id):
    word=Dictionary.query.get_or_404(word_id)
    db.session.delete(word)
    db.session.commit()
    return redirect(url_for("browse", type="All"))


# login manager

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='signin'


@ login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# logout function


@ app.route("/signout", methods=["GET", "POST"])
@ login_required
def signout():
    logout_user()
    return redirect(url_for("signin"))
