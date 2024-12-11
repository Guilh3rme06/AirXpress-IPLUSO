from flask import Flask
from app.routes.main import main_bp
from app.routes.clients import clients_bp

def create_app():
    app = Flask(__name__, static_folder='assets')

    app.register_blueprint(main_bp)
    app.register_blueprint(clients_bp, url_prefix='/clients')

    return app
