from flask import Flask, render_template, request, redirect
from server import Server

# == Init app and server
app = Flask(__name__)
server = Server(app)

# == Model ==
class Todos (server.db.Model):
    _id = server.db.Column(server.db.Integer, primary_key=True)
    title = server.db.Column(server.db.String(200), nullable=False)
    desc = server.db.Column(server.db.String(500), nullable=False)
    
    def insert(self):
        server.db.session.add(self)
        server.db.session.commit()

    def delete(self):
        server.db.session.delete(self)
        server.db.session.commit()

# == Controller
class Controller:
    def fetchTodos(self):
        all_todos = Todos.query.all()
        return all_todos

    def addTodo(self):
        title = request.form['title']
        desc = request.form['description']

        todo = Todos(title=title, desc=desc)
        todo.insert()

    def deleteTodo(self, _id):
        todo = Todos.query.filter_by(_id=_id).first()
        todo.delete()

# == Routes ==
controller = Controller();

@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        controller.addTodo()

    todos = controller.fetchTodos()
    return render_template('index.html', todos = todos)

@app.route('/delete/<int:_id>')
def delete(_id):
    controller.deleteTodo(_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)
