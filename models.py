from flask import current_app
from sqlalchemy import func
from app import db, fbcrypt


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(255))
    # books = db.relationship('Book', backref='author')



class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    date_published = db.Column(db.Date)
    cover_type = db.Column(db.String)
    author = db.relationship("Author", backref='book')
    publisher = db.relationship('Publisher', backref='book')




class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.String(255))
    # books = db.relationship('Book', backref='publisher')




class User(db.Model):
    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime)
    email_confirmation_sent_on = db.Column(db.DateTime, server_default=func.now())
    email_confirmed = db.Column(db.Boolean, default=False)
    email_confirmed_on = db.Column(db.DateTime)



    def __init__(self, username: str, password_plaintext: str, email: str):
        self.email = email
        self.username = username
        self.password = self._generate_password_hash(password_plaintext)




    def is_password_correct(self, password_plaintext: str):
        return fbcrypt.check_password_hash(self.password, password_plaintext)


    def set_password(self, password_plaintext: str):
        self.password = self._generate_password_hash(
            password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext):
        return fbcrypt.generate_password_hash(
            password_plaintext).decode('utf-8')



    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
         return False

    def get_id(self):
        return str(self.id)


db.create_all()