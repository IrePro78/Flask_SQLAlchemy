from flask import request, render_template, jsonify
from flask_login import login_required
from models import Publisher, db
from app import csrf



@csrf.exempt
@login_required
def index_publishers():
    term = request.form.get('term')
    publishers = Publisher.query.filter(Publisher.publisher_name.ilike(f'%{term}%')).all()
    publishers_list = [publisher.to_dict() for publisher in publishers]
    return jsonify(publishers_list)



@login_required
def add_publisher():
    if request.method == 'POST':
        publisher_id = request.form['publisher_name']
        if publisher_id.isdigit():
            return publisher_id
        else:
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
