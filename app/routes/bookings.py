from flask import Blueprint
from src.utils.util_bookings import *

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/')
def index_bookings_route():
    return index_reservas()

@bookings_bp.route('/add_booking', methods=['GET', 'POST'])
def add_bookings_route():
    return add_booking()

@bookings_bp.route('/update_booking/<int:reserva_id>', methods=['GET', 'POST'])
def update_bookings_route(reserva_id):
    return update_booking(reserva_id)

@bookings_bp.route('/delete_booking/<int:reserva_id>')
def delete_bookings_route(reserva_id):
    return delete_booking(reserva_id)