from flask import request

from models import Author, db



def add_author():
    if request.method == 'POST':
        author_name = request.form['author_name']
        new_author = Author(author_name=author_name)
        db.session.add(new_author)
        db.session.commit()
        return new_author.id


def update_author(author):
    if request.method == 'POST':
       author.author_name = request.form['author_name']
       db.session.commit()
       return author.author_name


def delete_author(author_id):
    pass

