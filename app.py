from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)

from config import app

db = SQLAlchemy(app)

from views import books
from mod_auth.controlers import login, register



#api urls
app.add_url_rule('/', view_func=books.index, methods=['GET'])
app.add_url_rule('/add-book', view_func=books.add_book, methods=['POST'])
app.add_url_rule('/update-book', view_func=books.update_book, methods=['GET', 'POST'])
app.add_url_rule('/delete/<id>', view_func=books.delete_book, methods=['GET', 'POST'])


#Logowanie i rejestracja
app.add_url_rule('/login', view_func=login, methods=['POST'])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)

