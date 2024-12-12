from flask import Blueprint
from src.utils.util_flights import index_flights, add_flights, update_flights, delete_flights

flights_bp = Blueprint('flights', __name__)

@flights_bp.route('/flights')
def index_flights_route():
    return index_flights()

@flights_bp.route('/add_flight', methods=['GET', 'POST'])
def add_flights_route():
    return add_flights()

@flights_bp.route('/update_flight/<int:voos_id>', methods=['GET', 'POST'])
def update_flights_route(voos_id):
    return update_flights(voos_id)

@flights_bp.route('/delete_flight/<int:voos_id>')
def delete_flights_route(voos_id):
    return delete_flights(voos_id)