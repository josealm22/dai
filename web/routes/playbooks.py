from flask import Blueprint, jsonify

playbooks_bp = Blueprint("playbooks", __name__)

@playbooks_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Playbooks endpoint working!"})
