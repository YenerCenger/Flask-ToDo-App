from flask import Flask,request, render_template,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Yener/Desktop/ToDoApp/todo.db"
app.secret_key= "TodoApp"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)

@app.route("/add",methods = ["POST"] )
def addTodo():
    title = request.form.get("title")
    if (len(title) == 0):
        flash("Lütfen bir Todo girin.","warning")
        return redirect(url_for("index"))
    else:
        newTodo = Todo(title = title,complete = False)
        db.session.add(newTodo)
        db.session.commit()
        flash("Todo başarıyla eklendi.", "success")
        return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    todo.complete = not todo.complete
    db.session.commit()
    flash("Todo Durumu Başarıyla Değiştirildi","success")

    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    flash("Todo Başarıyla Silindi","success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)