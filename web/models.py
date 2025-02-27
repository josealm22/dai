from datetime import datetime
from flask_login import UserMixin
from web import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default="user")

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ip = db.Column(db.String(15), unique=True, nullable=False)
    os = db.Column(db.String(20))  # Windows, Linux
    last_check = db.Column(db.DateTime)

class Playbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)  # Contenido YAML
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Deployment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playbook_id = db.Column(db.Integer, db.ForeignKey("playbook.id"))
    client_ids = db.Column(db.Text)  # IDs separados por comas
    scheduled_at = db.Column(db.DateTime)
    status = db.Column(db.String(20), default="pending")  # pending, running, done
