from flask import render_template, flash, redirect, url_for, request
from app import db
from mod_auth.forms import RegisterForm
from models import User
from hashlib import pbkdf2_hmac



def login():
    return render_template('header.html')


def register():
    salt='qwer42b#$'
    form = RegisterForm(request.form)
    if request.form == 'POST':
        username = form.username.data
        hashed_password = pbkdf2_hmac('sha256', form.password.data.encode('utf8'), salt .encode('utf8'),999)
        email = form.email.data
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Użtkownik dodany poprawnie')
        return redirect(url_for('login.html'))
    return render_template('header.html', form=form)