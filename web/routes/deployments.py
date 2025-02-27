from flask import Blueprint, request, jsonify
from web.models import Deployment, db
from datetime import datetime

deployments_bp = Blueprint("deployments", __name__)

@deployments_bp.route("/deployments", methods=["POST"])
def schedule_deployment():
    data = request.get_json()
    new_deployment = Deployment(
        playbook_id=data.get("playbook_id"),
        client_ids=",".join(data.get("client_ids")),
        scheduled_at=datetime.strptime(data.get("scheduled_at"), "%Y-%m-%d %H:%M"),
        status="pending"
    )
    db.session.add(new_deployment)
    db.session.commit()

    return jsonify({"message": "Despliegue programado"}), 201