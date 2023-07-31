from mototorque import db


class Lexicon(db.Model):
    # schema for the Lexicon model
    id = db.Column(db.Integer, primary_key=True)
    word_phrase = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(200), unique=True, nullable=False)
    example = db.Column(db.String(200), nullable=False)
    # keywords = db.Column(db.String(50), nullable=False)
    user_id = db.Column(
        db.String(50), db.ForeignKey("user.id"), nullable=False,)
    users = db.relationship("User", backref="lexicon", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.word_phrase


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username
