from flask import render_template, request, redirect, url_for, flash
from models import Book, Author, db


def index():

    all_books = db.session.query(Book.id, Book.title, Author.author_name, Book.pages)

    # all_books = Book.query.all()

    return render_template('index.html', books=all_books)



def add_book():

    if request.method == 'POST':
        title = request.form['title']
        author_name = request.form['author_name']
        pages = request.form['pages']
        if author_name not in Author:
            new_author = Author(author_name)
            new_book = Book(title, new_author.id, pages)
            db.session.add(new_author)
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
