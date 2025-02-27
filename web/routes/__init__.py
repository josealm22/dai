# web/routes/__init__.py
from web.routes.auth import auth_bp
from web.routes.playbooks import playbooks_bp
from web.routes.deployments import deployments_bp
from web.routes.clients import clients_bp

__all__ = ["auth_bp", "playbooks_bp", "deployments_bp", "clients_bp"]
