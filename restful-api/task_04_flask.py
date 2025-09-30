from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def list_users():
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error":"user not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 404
    
    data = request.get_json(silent=True) or {}
    username = data['username']
    if not username:
        return jsonify({"error": "Username is required"}), 404
    
    user_data = {"username":username, "name": data.get("name"), "age": data.get("age"), "city": data.get("city")}

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    # Run the development server on default port 5000
    app.run()