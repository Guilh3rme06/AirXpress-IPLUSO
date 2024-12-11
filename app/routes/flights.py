from flask import Blueprint, render_template, request, jsonify
from app.services.flight_service import get_all_flights, add_flight

flights_bp = Blueprint('flights', __name__)

@flights_bp.route('/flights', methods=['GET'])
def list_flights():
    flights = get_all_flights()
    return render_template('flights.html', flights=flights)

@flights_bp.route('/flights', methods=['POST'])
def create_flight():
    data = request.json
    add_flight(data)
    return jsonify({"message": "Voo criado com sucesso!"}), 201
