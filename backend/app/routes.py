from flask import render_template, request, jsonify
from app import app, db
from app.models import Task
from sqlalchemy.exc import SQLAlchemyError

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/api/tasks', methods=["POST"])
def tasks_store():
    try:
        name = request.json.get("name")
        if not name:
            return jsonify({"status": "error", "message": "Task name is required"}), 400
        content = request.json.get("content", None)
        
        #Save data in database
        task = Task(name = name, content = content)
        db.session.add(task)
        db.session.commit()
        return jsonify({"status": "success", "task_id": task.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/tasks', methods=["GET"])
def list_tasks(): return jsonify(Task.query.all())