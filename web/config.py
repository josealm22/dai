import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///deployments.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_EXPIRATION = 3600  # 1 hora
    ANSIBLE_PATH = os.path.abspath("../ansible/playbooks")
