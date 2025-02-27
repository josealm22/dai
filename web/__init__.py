from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from web.config import Config  # Importación corregida

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from web import models
        db.create_all()

        # Importar y registrar blueprints
        from web.routes.auth import auth_bp
        from web.routes.playbooks import playbooks_bp
        from web.routes.deployments import deployments_bp
        from web.routes.clients import clients_bp

        app.register_blueprint(auth_bp, url_prefix="/api/auth")
        app.register_blueprint(playbooks_bp, url_prefix="/api/playbooks")
        app.register_blueprint(deployments_bp, url_prefix="/api/deployments")
        app.register_blueprint(clients_bp, url_prefix="/api/clients")

        @app.route("/routes", methods=["GET"])
        def list_routes():
            routes = [str(rule) for rule in app.url_map.iter_rules()]
            return jsonify(routes)


    return app



# Exponer la aplicación para Gunicorn
app = create_app()

