from flask import Blueprint
from src.utils.util_clients import index_clientes, add_user, update_user, delete_user

clients_bp = Blueprint('clients', __name__, template_folder='templates')

@clients_bp.route('/clientes')
def index_clientes_route():
    return index_clientes()

@clients_bp.route('/add_user', methods=['GET', 'POST'])
def add_user_route():
    return add_user()

@clients_bp.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user_route(user_id):
    return update_user(user_id)

@clients_bp.route('/delete_user/<int:user_id>')
def delete_user_route(user_id):
    return delete_user(user_id)
