from flask import Blueprint, request, jsonify
from web.models import Client, db
from datetime import datetime

clients_bp = Blueprint("clients", __name__)

@clients_bp.route("/clients/register", methods=["POST"])
def register_client():
    data = request.get_json()
    client = Client.query.filter_by(ip=data.get("ip")).first()

    if client:
        return jsonify({"client_id": client.id})

    new_client = Client(
        name=data.get("name"),
        ip=data.get("ip"),
        os=data.get("os"),
        last_check=datetime.utcnow()
    )
    db.session.add(new_client)
    db.session.commit()

    return jsonify({"client_id": new_client.id})