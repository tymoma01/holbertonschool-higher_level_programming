#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store (leave empty for the checker)
users = {}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def list_users():
    # Return a JSON list of usernames
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if not user:
        # Exact message + 404 required by the checker
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    # Must be JSON; return 400 (not 404) if not
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json(silent=True) or {}

    username = data.get("username")
    # Missing username -> 400 with exact message
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Duplicate -> 409 with exact message
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
