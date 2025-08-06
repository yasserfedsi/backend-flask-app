from flask import Blueprint, request, jsonify
from core.models import get_all_tasks, get_task_by_id, create_task, update_task, delete_task

routes = Blueprint("routes", __name__)

@routes.route("/api/tasks", methods=["GET"])
def fetch_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks)

@routes.route("/api/tasks/<string:task_id>", methods=["GET"])
def fetch_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@routes.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if "title" not in data and "description" not in data:
        return jsonify({"error": "Missing title"}), 400
    task = create_task(data["title"], data["description"])
    return jsonify(task), 201


@routes.route("/api/tasks/<string:task_id>", methods=["PUT"])
def modify_task(task_id):
    data = request.get_json()
    task = update_task(task_id, data)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@routes.route("/api/tasks/<string:task_id>", methods=["DELETE"])
def remove_task(task_id):
    success = delete_task(task_id)
    if success:
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"error": "Task not found"}), 404
