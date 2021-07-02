from flask import Flask


app = Flask(__name__)


from views import books

app.add_url_rule('/', view_func=books.index, methods=['GET'])
app.add_url_rule('/add-book', view_func=books.add_book, methods=['POST'])
app.add_url_rule('/update-book', view_func=books.update_book, methods=['GET', 'POST'])
app.add_url_rule('/delete/<id>', view_func=books.delete_book, methods=['GET', 'POST'])



if __name__ == '__main__':
    app.run(debug=True)
