from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(255))
    books = db.relationship('Book', backref='author')


    def __init__(self, author_name):
        self.author_name = author_name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    pages = db.Column(db.Integer, nullable=False)


    def __init__(self, title, author_id, pages):
        self.author_id = author_id
        self.title = title
        self.pages = pages

db.create_all()

