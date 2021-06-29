from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(255))
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    title = db.Column(db.String(255))
    pages = db.Column(db.Integer, nullable=False)


db.create_all()

