from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from web.models import User, db
from datetime import datetime, timedelta
import jwt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Usuario ya existe"}), 400

    new_user = User(
        username=username,
        password_hash=generate_password_hash(password),
        role="user"
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get("username")).first()

    if not user or not check_password_hash(user.password_hash, data.get("password")):
        return jsonify({"error": "Credenciales inválidas"}), 401

    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }, "supersecretkey", algorithm="HS256")

    return jsonify({"token": token})
