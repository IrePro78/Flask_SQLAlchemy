from app import app


app.secret_key = 'SecretKey'
app.config['SESSION_TYPE'] = 'memcached'
app.config['DEBUG'] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app:admin123@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
