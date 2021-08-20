from flask import render_template, flash, redirect, url_for, request
from mod_auth.forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required, logout_user
from hashlib import pbkdf2_hmac
from models import User
from app import db




def login():
    if current_user.is_authenticated:
        flash('Jesteś już zalogowany!')
        return redirect(url_for('index'))

    salt = 'qwer42b#$ewrweede'
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            username = request.form['username']
            user = User.query.filter_by(username=username).first()
            crypted_pass = user.password
            password = request.form['password']
            hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()
            if crypted_pass == hashed_password:
                login_user(user, remember=form.remember_me)
                flash(f'Dziękuję za zalogowanie {current_user.username}!')
                return redirect(url_for('index'))
            flash('Bład! Nieprawidłowe dane logowania', 'error')
    return render_template('login.html', form=form)

@login_required
def logout():
    logout_user()
    flash('Do widzenia!')
    return redirect(url_for('login'))


def register():
    salt = 'qwer42b#$ewrweede'
    form = RegisterForm(request.form)

    if request.method == 'POST':
      if form.validate():
          try:
              username = form.username.data
              password = form.password.data
              email = form.email.data
              hashed_password = pbkdf2_hmac('sha256', password.encode('utf8'), salt.encode('utf8'), 999).hex()
              new_user = User(username=username, password=hashed_password, email=email)
              db.session.add(new_user)
              db.session.commit()
              flash(f'Dziękuję za rejestrację, {new_user.username}')
              return redirect(url_for('login'))
          except IntegrityError:
              db.session.rollback()
              flash(f'Błąd! Email ({new_user.email}) już istnieje w bazie danych. ', 'error')
      else:
          flash(' Wprowadzono błędne dane !')

    return render_template('register.html', form=form)


@login_required
def user_profile():
    return render_template('profile.html')