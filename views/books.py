from flask import render_template, request, redirect, url_for, flash
from models import Book, db


def index():
    all_books = Book.query.all()
    return render_template('index.html', books=all_books)



def add_book():

    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']

        new_book = Book(title, author_id)
        db.session.add(new_book)
        db.session.commit()
        flash('Książka dodana poprawnie')
        return redirect(url_for('index'))


def update_book():
    if request.method == 'POST':
        book = Book.query.get(request.form.get('id'))

        book.id = request.form['id']
        book.title = request.form['title']
        book.author_id = request.form['author_id']

        db.session.commit()
        flash('Edycja powiodła się')
        return redirect(url_for('index'))


def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('Książka skasowana')

    return redirect(url_for('index'))
