from flask_login import UserMixin, LoginManager
from mototorque import db
from werkzeug.security import generate_password_hash, check_password_hash


class Dictionary(db.Model):
    # schema for the Dictionary model
    id = db.Column(db.Integer, primary_key=True)
    word_phrase = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(200), nullable=False)
    example = db.Column(db.String(200), nullable=False)
    # date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # Foreign key to link users (refer to primary key of Users)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.word_phrase


class Users(db.Model, UserMixin):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    # User can have many posts
    posts = db.relationship('Dictionary', backref='poster')

    @property
    def password(self):
        raise AttributeError('password is not a readble attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username
