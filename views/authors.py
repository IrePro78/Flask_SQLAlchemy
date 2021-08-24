from flask import request, render_template
from flask_login import login_required

from models import Author, db

@login_required
def index_authors():
    all_authors = Author.query.order_by(Author.id).all()
    return render_template('index.html', books=all_authors)


@login_required
def add_author():
    if request.method == 'POST':
        author_name = request.form['author_name']
        new_author = Author(author_name=author_name)
        db.session.add(new_author)
        db.session.commit()
        return new_author.id

@login_required
def update_author(author):
    if request.method == 'POST':
       author.author_name = request.form['author_name']
       db.session.commit()
       return author.author_name


def delete_author(author_id):
    pass

