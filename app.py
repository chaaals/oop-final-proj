from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#Helmin
# == Model ==
class Todos (db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
class Controller:
    def home(self):
        todo = Todos(title="Hello world", desc="First data stored in db")

        db.session.add(todo)
        db.session.commit()

        all_todos = Todos.query.all()
        return render_template('index.html', todos = all_todos)

controller = Controller();

app.add_url_rule('/', 'index', lambda: controller.home())

if __name__ == "__main__":
    app.run(debug = True)