from mototorque import db


class Dictionary(db.Model):
    # schema for the Dictionary model
    id = db.Column(db.Integer, primary_key=True)
    word_phrase = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(200), unique=True, nullable=False)
    example = db.Column(db.String(200), nullable=False)
    # Foreign key to link users (refer to primary key of Users)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.word_phrase


class Users(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True)
    # User can have many posts
    posts = db.relationship('Dictionary', backref='poster')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username
