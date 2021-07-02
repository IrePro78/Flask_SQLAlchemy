from flask import render_template, request, redirect, url_for, flash
from models import Book, Author, db
from views import authors, publishers


def index():
    all_books = Book.query.order_by(Book.id).all()

    return render_template('index.html', books=all_books)




def add_book():

    if request.method == 'POST':
        title = request.form['title']
        pages = request.form['pages']
        new_author = authors.add_author()
        new_publisher = publishers.add_publisher()
        new_book = Book(title=title, author_id=new_author, publisher_id=new_publisher, pages=pages)
        db.session.add(new_book)
        db.session.commit()
        flash('Książka dodana poprawnie')
        return redirect(url_for('index'))



def update_book():
    if request.method == 'POST':
        book = Book.query.get(request.form.get('id'))
        book.id = request.form['id']
        book.title = request.form['title']
        author = Author.query.get(request.form.get('id'))
        authors.update_author(author)
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