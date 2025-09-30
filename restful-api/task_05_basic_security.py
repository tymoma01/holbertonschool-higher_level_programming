#!/usr/bin/env python3
"""
Basic & JWT security for a Flask API.

Requirements covered:
- Basic HTTP Auth on /basic-protected
- JWT login (/login) returning access_token
- JWT-protected route (/jwt-protected)
- Role-based route (/admin-only) with 403 on insufficient role
- Consistent 401 for ALL authentication errors (missing/invalid/expired/malformed/revoked/fresh)
"""

from datetime import timedelta
from functools import wraps

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import generate_password_hash, check_password_hash

# -----------------------------------------------------------------------------
# App setup
# -----------------------------------------------------------------------------
app = Flask(__name__)

# Strong secret key for JWT; in production load from env/secret manager
app.config["JWT_SECRET_KEY"] = "doiqwejfoij34qpfgojw4pgjo45"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# -----------------------------------------------------------------------------
# In-memory users (hashed passwords)
# -----------------------------------------------------------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# -----------------------------------------------------------------------------
# Basic HTTP Authentication
# -----------------------------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user  # flask-httpauth will set this as current_user
    return None


@auth.error_handler
def basic_auth_error(status):
    # Ensure Basic Auth failures return a consistent 401 with JSON
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    # If we got here, Basic Auth succeeded
    return "Basic Auth: Access Granted", 200


# -----------------------------------------------------------------------------
# JWT Authentication
# -----------------------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 401  # auth error → 401

    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed identity and role in the token
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # If we got here, JWT is valid
    return "JWT Auth: Access Granted", 200


# -----------------------------------------------------------------------------
# Role-based access (Authorization)
# -----------------------------------------------------------------------------
def require_role(required_role: str):
    """Decorator to enforce role-based authorization on JWT-protected routes."""

    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()  # contains our additional_claims like role
            role = claims.get("role")
            if role != required_role:
                # Token is valid, but role is insufficient → authorization failure (403)
                return jsonify({"error": "Admin access required"}), 403
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@app.route("/admin-only", methods=["GET"])
@require_role("admin")
def admin_only():
    return "Admin Access: Granted", 200


# -----------------------------------------------------------------------------
# Consistent 401s for ALL JWT authentication errors
# -----------------------------------------------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    # Missing Authorization header / Bearer token
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    # Token cannot be decoded or is otherwise invalid
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# Optional: handle other generic JWT errors as 401 too
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    # Example placeholder: no revocation list here
    return False


# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # For local testing only
    app.run(host="0.0.0.0", port=5000, debug=True)
