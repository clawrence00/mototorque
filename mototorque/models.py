from mototorque import db


class Lexicon(db.Model):
    # schema for the Lexicon model
    id = db.Column(db.Integer, primary_key=True)
    word_phrase = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(200), nullable=False)
    example = db.Column(db.String(200), nullable=False)
    # keywords = db.Column(db.String(50), nullable=False)
    username = db.Column(
        db.String(50), nullable=False, db.ForeignKey(Users.username)


# class Users(db.Model):
#     # schema for the Users model
#     username=db.Column(db.String(50), unique=True, primary_key=True)
#     password=db.Column(db.Text, nullable=False)
#     email=db.Column(db.Boolean, default=False, nullable=False)
