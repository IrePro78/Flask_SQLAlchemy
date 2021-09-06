from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask import Flask
import logging



app = Flask(__name__)

from config import app

db = SQLAlchemy(app)
#Migracja db
# db_migration = Migrate()


#Logi
file_handler = RotatingFileHandler('logs/flask-books-library-app.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [%(funcName)s in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

#Logger
app.logger.info('Uruchamianie aplikacji Flask Books Library App... ')

#Logowanie użutkowników
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Zaloguj się, aby uzyskać dostęp do tej strony.'
login.login_message_category = 'info'

#Hashowanie hasła
fbcrypt = Bcrypt(app)

#Ochrona CSRF
csrf = CSRFProtect(app)

#Mail
mail = Mail(app)



from models import User


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from views import books, authors, publishers
from mod_auth import controlers

#api urls
app.add_url_rule('/', view_func=books.index, methods=['GET'])
app.add_url_rule('/authors', view_func=authors.index_authors, methods=['GET'])
app.add_url_rule('/publishers', view_func=publishers.index_publishers, methods=['GET'])
app.add_url_rule('/add-book', view_func=books.add_book, methods=['GET', 'POST'])
app.add_url_rule('/update-book', view_func=books.update_book, methods=['GET', 'POST'])
app.add_url_rule('/delete/<id>', view_func=books.delete_book, methods=['GET', 'POST'])


#Logowanie i rejestracja
app.add_url_rule('/register', view_func=controlers.register, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=controlers.login, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=controlers.logout, methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=controlers.user_profile, methods=['GET', 'POST'])
app.add_url_rule('/confirm/<token>', view_func=controlers.confirm_email, methods=['GET', 'POST'])
app.add_url_rule('/password_reset_via_email', view_func=controlers.password_reset_via_email, methods=['GET', 'POST'])
app.add_url_rule('/password_reset_via_token/<token>', view_func=controlers.process_password_reset_token, methods=['GET', 'POST'])
app.add_url_rule('/resend_email_confirmation', view_func=controlers.resend_email_confirmation, methods=['GET', 'POST'])
app.add_url_rule('/change_password', view_func=controlers.change_password, methods=['GET', 'POST'])



if __name__ == '__main__':
    app.run(debug=True)


