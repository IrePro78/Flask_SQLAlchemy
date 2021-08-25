from datetime import datetime
from flask_login import login_user, current_user, login_required, logout_user
from flask import render_template, flash, redirect, url_for, request, abort, current_app, copy_current_request_context
from itsdangerous import URLSafeTimedSerializer, BadSignature
from mod_auth.forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError
from urllib.parse import urlparse
from flask_mail import Message
from threading import Thread
from models import User
from app import db, mail


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
              flash(f'Dziękuję za rejestrację, {new_user.username} !Sprawdź swój adres e-mail,'
                    f' aby potwierdzić !', 'success')
              current_app.logger.info(f'Registered new user: {form.username.data}!')

              @copy_current_request_context
              def send_email(message):
                  with current_app.app_context():
                      mail.send(message)

              msg = generate_confirmation_email(form.email.data)
              email_thread = Thread(target=send_email, args=[msg])
              email_thread.start()

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



def generate_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    confirm_url = url_for('confirm_email',
                          token=confirm_serializer.dumps(user_email, salt='@4Dclkk573$^4!'),
                          _external=True)

    return Message(subject='Flask Books Library App - Potwierdź adres email',
                   html=render_template('email_confirmation.html', confirm_url=confirm_url),
                   recipients=[user_email])


def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        email = confirm_serializer.loads(token, salt='@4Dclkk573$^4!', max_age=3600)
    except BadSignature as e:
        flash(f'Link potwierdzający jest nieprawidłowy lub wygasł.', 'danger')
        current_app.logger.info(f'Nieprawidłowy lub wygasły link potwierdzający otrzymany z adresu IP:'
                                f' {request.remote_addr}')
        return redirect(url_for('login'))

    user = User.query.filter_by(email=email).first()

    if user.email_confirmed:
        flash('Konto już potwierdzone. Proszę się zalogować.', 'info')
        current_app.logger.info(f'Confirmation link received for a confirmed user: {user.username}')
    else:
        user.email_confirmed = True
        user.email_confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Dziękuję za potwierdzenie adresu e-mail!', 'success')
        current_app.logger.info(f'Email address confirmed for: {user.email}')

    return redirect(url_for('index'))