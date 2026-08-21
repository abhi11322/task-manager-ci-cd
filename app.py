import  os
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    if not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
    new_task = {
        'id': next_id,
        'title': data.get('title'),
        'description': data.get('description'),
        'done': False
    }
    tasks.append(new_task)
    next_id += 1
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})

    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)