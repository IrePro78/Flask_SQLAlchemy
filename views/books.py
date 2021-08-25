from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import app
from models import Book, Author, db, Publisher
from views import authors, publishers

@login_required
def index():
    all_books = Book.query.order_by(Book.id).all()
    return render_template('index.html', books=all_books)

@login_required
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        pages = request.form['pages']
        new_author = authors.add_author()
        new_publisher = publishers.add_publisher()
        date_published = request.form['date_published']
        cover_type = request.form['cover_type']
        new_book = Book(
            title=title,
            author_id=new_author,
            publisher_id=new_publisher,
            pages=pages,
            date_published=date_published,
            cover_type=cover_type
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Książka dodana poprawnie', 'success')
        app.logger.info(f"Added new book: ({request.form['title']})!")
        return redirect(url_for('index'))

@login_required
def update_book():
    if request.method == 'POST':
        book = Book.query.get(request.form.get('id'))
        book.id = request.form['id']
        book.title = request.form['title']
        author = Author.query.get(request.form.get('id'))
        authors.update_author(author)
        publisher = Publisher.query.get(request.form.get('id'))
        publishers.update_publisher(publisher)
        book.pages = request.form['pages']
        book.date_published = request.form['date_published']
        book.cover_type = request.form['cover_type']
        db.session.commit()
        flash('Edycja powiodła się', 'success')
        app.logger.info(f"Updated book: ({book.title}) by user: {current_user.username} !")
        return redirect(url_for('index'))

@login_required
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('Książka skasowana', 'warning')
    app.logger.info(f"Book removed: ({book.title}) by user: {current_user.username} !")
    return redirect(url_for('index'))
