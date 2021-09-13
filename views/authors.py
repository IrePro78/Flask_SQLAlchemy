from flask_login import login_required
from flask import request, jsonify
from models import Author, db
from app import csrf




# @login_required
@csrf.exempt
def index_authors():
    if request.method == 'POST':
        term = request.form.get('q')
        authors = Author.query.filter(Author.author_name.ilike(f'%{term}%')).all()
        authors_list = [author.to_dict() for author in authors]
        return jsonify(authors_list)


@login_required
def add_author():
    if request.method == 'POST':
        author_id = request.form['author_name']
        if len(author_id) < 3:
            return author_id
        else:
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

