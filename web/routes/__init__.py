from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from web import models  # Importa modelos después de inicializar db
        db.create_all()

        # Registrar blueprints
        from web.routes.auth import auth_bp
        from web.routes.playbooks import playbooks_bp
        from web.routes.deployments import deployments_bp
        from web.routes.clients import clients_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(playbooks_bp)
        app.register_blueprint(deployments_bp)
        app.register_blueprint(clients_bp)

    return app
