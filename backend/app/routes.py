from flask import render_template, request, jsonify
from app import app, db
from app.models import Task
from sqlalchemy.exc import SQLAlchemyError

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/projects/store', methods=["POST"])
def tasks_store():
    try:
        #Get and validate data
        #print(request.form["content"])
        name = request.form.get("name")
        if not name:
            return jsonify({"status": "error", "message": "Task name is required"}), 400
        content = request.form.get("content", None)
        
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