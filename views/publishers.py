from flask import request

from models import Publisher, db



def add_publisher():
    if request.method == 'POST':
        publisher_name = request.form['publisher_name']
        new_publisher = Publisher(publisher_name=publisher_name)
        db.session.add(new_publisher)
        db.session.commit()
        return new_publisher.id


def update_publisher(publisher):
    if request.method == 'POST':
        publisher.publisher_name = request.form['publisher_name']
        db.session.commit()
        return publisher.publisher_name


def delete_publishers():
    pass
