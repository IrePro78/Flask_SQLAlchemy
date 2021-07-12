from flask import render_template, flash, redirect, url_for, request
from app import db
# from mod_auth.forms import RegisterForm
from models import User
from hashlib import pbkdf2_hmac




def login():
    salt = 'qwer42b#$ewrweede'
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        crypted_pass = user.password
        password = request.form['password']
        hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()
        crypted_pass == hashed_password
        print(request.form['password'])
        print(crypted_pass)
        print(hashed_password)
        return redirect(url_for('index'))


def register():
    salt ='qwer42b#$ewrweede'
    # req = request.form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Użtkownik dodany poprawnie')
        return redirect(url_for('index'))

    return render_template('header.html', form='new_user')