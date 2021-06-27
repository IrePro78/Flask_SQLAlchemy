import psycopg2
from sqlalchemy import ForeignKey
from app import app, db


app.secret_key = 'SecretKey'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app:admin123@localhost/Flask_SQLAlchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(255))

    def __init__(self, author_name):
        self.author_name = author_name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'))
    title = db.Column(db.String(255))

    def __init__(self, title, author_id):
        self.author_id = author_id
        self.title = title

db.create_all()

