from flask import Blueprint, jsonify

clients_bp = Blueprint("clients", __name__)

@clients_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Clients endpoint working!"})
