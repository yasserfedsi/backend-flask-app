from asyncio import tasks
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from core.routes import routes
from core.models import get_all_tasks

app = Flask(__name__)
CORS(app, origins=["https://flask-frontend.celec.codes"])

# Registering the routes blueprint
app.register_blueprint(routes)

@app.route("/")
def index():
    try:
        tasks = get_all_tasks()
        return render_template("index.html", tasks=tasks)
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to the Flask API Production!"})

@app.route("/debug-tasks", methods=["GET"])
def debug_tasks():
    try:
        tasks = get_all_tasks()
        print("DEBUG TYPE:", type(tasks))
        return jsonify({"tasks": tasks, "status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
