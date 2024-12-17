from flask import Blueprint, render_template

from src.models.flights import count_voos, count_voos_ativos
from src.models.bookings import count_reservas
from src.models.clients import count_clientes

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index_route():
    total_clientes = count_clientes()
    total_reservas = count_reservas()
    total_voos = count_voos()
    total_voos_ativos = count_voos_ativos()
    return render_template('index.html', title='Home | AirXpress', total_clientes=total_clientes, total_reservas=total_reservas, total_voos=total_voos, total_voos_ativos=total_voos_ativos)
