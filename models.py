from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)

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

db.create_all()
