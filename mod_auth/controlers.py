from flask import render_template, flash, redirect, url_for, request
from app import db
from mod_auth.forms import RegisterForm, LoginForm
from models import User
from hashlib import pbkdf2_hmac




def login():
    salt = 'qwer42b#$ewrweede'
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        crypted_pass = user.password
        password = request.form['password']
        hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()
        crypted_pass == hashed_password
        print(request.form['password'])
        print(crypted_pass)
        print(hashed_password)
        quit()
        return redirect(url_for('index'))
    flash('Proszę wprowadzić poprawne dane')
    return render_template('login.html', form=form)



def register():
    salt = 'qwer42b#$ewrweede'
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Użtkownik dodany poprawnie')
        return redirect(url_for('index'))
    flash('Proszę wprowadzić poprawne dane')
    return render_template('login.html', form=form)




