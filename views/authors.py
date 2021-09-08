from flask import request, jsonify
from flask_login import login_required

from app import csrf
from models import Author, db



# @login_required
@csrf.exempt
def index_authors():
        # authors = Author.query.order_by(Author.author_name).all()
        authors = Author.query.filter(Author.author_name.like('K%')).order_by(Author.author_name).limit(1)
        authors_list = [author.to_dict() for author in authors]
        return jsonify(authors_list)



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

