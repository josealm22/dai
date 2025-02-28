from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from web.models import Client, db

clients_bp = Blueprint("clients", __name__)

@clients_bp.route("/register", methods=["POST"])
def register_client():
    data = request.get_json()
    if not data or "name" not in data or "ip" not in data or "os" not in data:
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        new_client = Client(
            name=data["name"],
            ip=data["ip"],
            os=data["os"]
        )
        db.session.add(new_client)
        db.session.commit()
        return jsonify({"client_id": new_client.id, "message": "Cliente registrado correctamente"}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "La IP ya está registrada"}), 409  # Código HTTP 409: conflicto

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
@clients_bp.route("/", methods=["GET"])
def get_clients():
    clients = Client.query.all()
    return jsonify([
        {"id": c.id, "name": c.name, "ip": c.ip, "os": c.os, "last_check": c.last_check}
        for c in clients
    ])
