from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to the Flask API Production!"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
