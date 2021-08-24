from flask import request, render_template
from flask_login import login_required

from models import Publisher, db

@login_required
def index_publishers():
    all_publishers = Publisher.query.order_by(Publisher.id).all()
    return render_template('index.html', books=all_publishers)



@login_required
def add_publisher():
    if request.method == 'POST':
        publisher_name = request.form['publisher_name']
        new_publisher = Publisher(publisher_name=publisher_name)
        db.session.add(new_publisher)
        db.session.commit()
        return new_publisher.id

@login_required
def update_publisher(publisher):
    if request.method == 'POST':
        publisher.publisher_name = request.form['publisher_name']
        db.session.commit()
        return publisher.publisher_name


def delete_publishers():
    pass
