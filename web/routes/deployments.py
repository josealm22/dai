from flask import Blueprint, jsonify

deployments_bp = Blueprint("deployments", __name__)

@deployments_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Deployments endpoint working!"})
