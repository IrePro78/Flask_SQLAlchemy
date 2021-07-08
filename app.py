from mod_auth.controlers import login, register
from flask import Flask


app = Flask(__name__)


from views import books

#api urls
app.add_url_rule('/', view_func=books.index, methods=['GET'])
app.add_url_rule('/add-book', view_func=books.add_book, methods=['POST'])
app.add_url_rule('/update-book', view_func=books.update_book, methods=['GET', 'POST'])
app.add_url_rule('/delete/<id>', view_func=books.delete_book, methods=['GET', 'POST'])


#Logowanie i rejestracja
app.add_url_rule('/login', view_func=login)
app.add_url_rule('/register', view_func=register)


if __name__ == '__main__':
    app.run(debug=True)

