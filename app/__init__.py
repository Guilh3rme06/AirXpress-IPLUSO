import os
from flask import Flask
from app.routes.main import main_bp
from app.routes.clients import clients_bp
from app.routes.flights import flights_bp
from app.routes.bookings import bookings_bp
from app.routes.export import export_bp

def create_app():
    app = Flask(__name__, static_folder='assets')

    app.register_blueprint(main_bp)
    app.register_blueprint(clients_bp, url_prefix='/clients')
    app.register_blueprint(flights_bp, url_prefix='/flights')
    app.register_blueprint(bookings_bp, url_prefix='/bookings')
    app.register_blueprint(export_bp, url_prefix='/export')
    app.config['SECRET_KEY'] = os.urandom(24).hex()

    return app
