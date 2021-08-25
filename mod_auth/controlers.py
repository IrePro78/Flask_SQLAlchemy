from flask_login import login_user, current_user, login_required, logout_user
from flask import render_template, flash, redirect, url_for, request, abort, current_app
from mod_auth.forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError
from urllib.parse import urlparse
from models import User
from app import db




def login():
    if current_user.is_authenticated:
        flash('Jesteś już zalogowany!', 'info')
        current_app.logger.info(f'Duplicate login attempt by user: {current_user.username}!')
        return redirect(url_for('index'))

    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(username=form.username.data).first()

            if user and user.is_password_correct(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash(f'Dziękuję za zalogowanie {current_user.username}!', 'success')
                current_app.logger.info(f'Logged in user: {current_user.username}!')

                if not request.args.get('next'):
                    return redirect(url_for('index'))

                next_url = request.args.get('next')
                if urlparse(next_url).scheme != '' or urlparse(next_url).netloc != '':
                    logout_user()
                    return abort(400)

                return redirect(next_url)
            flash('Bład! Nieprawidłowe dane logowania', 'danger')
            current_app.logger.error('Invalid user attempted to log in!')
    return render_template('login.html', form=form)


@login_required
def logout():
    logout_user()
    flash('Do zobaczenia! ', 'info')
    return redirect(url_for('login'))


def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
      if form.validate():
          try:
              new_user = User(form.username.data, form.password.data, form.email.data)
              db.session.add(new_user)
              db.session.commit()
              flash(f'Dziękuję za rejestrację, {new_user.username}', 'success')
              current_app.logger.info(f'Registered new user: {form.username.data}!')
              return redirect(url_for('login'))
          except IntegrityError:
              db.session.rollback()
              flash(f'Użytkownik ({form.username.data}) lub email ({form.email.data})'
                    f' już istnieje w bazie danych. ', 'warning')
      else:
          flash(' Wprowadzono błędne dane !', 'danger')

    return render_template('register.html', form=form)


@login_required
def user_profile():
    return render_template('profile.html')