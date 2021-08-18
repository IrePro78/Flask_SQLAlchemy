from flask import render_template, flash, redirect, url_for, request, abort
from app import db
from mod_auth.forms import RegisterForm, LoginForm
from models import User
from hashlib import pbkdf2_hmac
from flask_login import login_user




def login():
    salt = 'qwer42b#$ewrweede'
    form = LoginForm(request.form)
    print(form.validate())

    if request.method == 'POST' and form.validate():
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        crypted_pass = user.password
        password = request.form['password']
        hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()

        if crypted_pass == hashed_password:
            login_user(user)
            flash('Zostałeś pomyślnie zalogowany')
            return redirect(url_for('index'))
        # else:
        #     abort(400)
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
        return redirect(url_for('login'))

    return render_template('register.html', form=form)




