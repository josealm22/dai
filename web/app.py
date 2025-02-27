# web/app.py
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Importación corregida

app = Flask(__name__)
app.config.from_object(Config)

# Base de datos
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

# Autenticación
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registrar blueprints (rutas)
from routes.auth import auth_bp
from routes.playbooks import playbooks_bp
from routes.deployments import deployments_bp
from routes.clients import clients_bp

app.register_blueprint(auth_bp)
app.register_blueprint(playbooks_bp)
app.register_blueprint(deployments_bp)
app.register_blueprint(clients_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)