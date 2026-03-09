from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean, default=False)

# Create database
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return "Task Manager API Running"

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        })
    return jsonify(result)

# Add task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added"})

# Delete task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)

# Update task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task.title = data.get("title", task.title)
    task.completed = data.get("completed", task.completed)

    db.session.commit()

    return jsonify({
        "message": "Task updated",
        "task": {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
    })
    
# Mark task as completed
@app.route('/tasks/<int:id>/complete', methods=['PATCH'])
def complete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.completed = True
    db.session.commit()

    return jsonify({
        "message": "Task marked as completed",
        "task": {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
    })