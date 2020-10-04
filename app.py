from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data import ActivePlayers
from config import DefaultConfig


app = Flask(__name__)
# db = SQLAlchemy(app)
app.config.from_object(DefaultConfig())  # use default settings
app.config.from_pyfile('app.cfg', silent=True)
app.app_context().push()  # update app context so SQLAlchemy works with current session


@app.route('/')
def index():
    return 'hello there'


if __name__ == '__main__':
    app.run()


