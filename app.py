from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)

from config import app

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'controlers.login'
bcrypt = Bcrypt(app)

from models import User


migrate = Migrate()
migrate.init_app(app, db)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from views import books
from mod_auth import controlers


#api urls
app.add_url_rule('/home', view_func=books.index, methods=['GET'])
app.add_url_rule('/add-book', view_func=books.add_book, methods=['POST'])
app.add_url_rule('/update-book', view_func=books.update_book, methods=['GET', 'POST'])
app.add_url_rule('/delete/<id>', view_func=books.delete_book, methods=['GET', 'POST'])


#Logowanie i rejestracja
app.add_url_rule('/login', view_func=controlers.login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=controlers.register, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)


