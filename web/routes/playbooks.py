from flask import Blueprint, request, jsonify
from web.models import Playbook, db
from datetime import datetime

playbooks_bp = Blueprint("playbooks", __name__)

@playbooks_bp.route("/playbooks", methods=["POST"])
def create_playbook():
    data = request.get_json()
    new_playbook = Playbook(
        name=data.get("name"),
        content=data.get("content"),
        author_id=data.get("author_id"),
        created_at=datetime.utcnow()
    )
    db.session.add(new_playbook)
    db.session.commit()

    return jsonify({"message": "Playbook creado"}), 201