from flask_sqlalchemy import SQLAlchemy

class Server:
    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(app)
