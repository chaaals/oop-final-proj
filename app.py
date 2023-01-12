from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# == Model ==
class Todos (db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

# == Controller ==
class Controller:
    def fetchTodos(self):
        all_todos = Todos.query.all()
        return all_todos

    def addTodo(self):
        title = request.form['title']
        desc = request.form['description']

        todo = Todos(title=title, desc=desc)

        db.session.add(todo)
        db.session.commit()

    def deleteTodo(self, _id):
        # apply logic here
        todo = Todos.query.filter_by(_id=_id).first()
        db.session.delete(todo)
        db.session.commit()

controller = Controller();

# == Web app routes ==
@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        controller.addTodo()

    todos = controller.fetchTodos()
    return render_template('index.html', todos = todos)

@app.route('/delete/<int:_id>')
def delete(_id):
    # apply route logic here
    controller.deleteTodo(_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)