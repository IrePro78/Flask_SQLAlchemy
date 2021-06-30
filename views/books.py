from flask import render_template, request, redirect, url_for, flash
from models import Book, Author, db


def index():

    # all_books = db.session.query(Book.author_id == Author.id).all()

    all_books = Book.query.all()
    # all_authors = Author.query.all()
    return render_template('index.html', books=all_books)



def add_book():

    if request.method == 'POST':
        title = request.form['title']
        author_name = request.form['author_name']
        pages = request.form['pages']
        new_author = Author(author_name= author_name)
        db.session.add(new_author)
        db.session.commit()
        new_book = Book(title=title, author_id=new_author.id, pages=pages)
        db.session.add(new_book)
        db.session.commit()
        flash('Książka dodana poprawnie')
        return redirect(url_for('index'))


def update_book():
    if request.method == 'POST':
        book = Book.query.get(request.form.get('id'))
        book.id = request.form['id']
        book.title = request.form['title']
        book.author_name = request.form['author_name']
        book.pages = request.form['pages']
        db.session.commit()
        flash('Edycja powiodła się')
        return redirect(url_for('index'))


def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('Książka skasowana')

    return redirect(url_for('index'))
