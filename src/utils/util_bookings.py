from flask import render_template, request, redirect, url_for
from datetime import datetime
from src.models.bookings import delete_reserva, get_reserva, get_reservas, insert_reserva, update_reserva
from src.models.clients import get_all_clients  # Supondo que essa função recupere todos os clientes
def index_reservas():
    """
    Lista as reservas do banco de dados.
    :return: renderiza a página de reservas com as reservas do banco de dados.
    """
    bookings = get_reservas()
    return render_template('bookings/booking.html', bookings=bookings, title='Reservas | AirXpress')

def add_booking():
    """
    Adiciona uma nova reserva ao banco de dados.
    :return: redireciona para a página de reservas.
    """
    if request.method == 'POST':
        fk_cliente = request.form['fk_cliente']  # Agora será um ID de cliente selecionado
        fk_voo = request.form['fk_voo']
        data = request.form['data']
        # Converter para o formato "YYYY-MM-DD HH:MM:SS"
        data_formatada = datetime.strptime(data, "%Y-%m-%dT%H:%M").strftime("%d-%m-%Y %H:%M:%S")
        insert_reserva(fk_cliente, fk_voo, data_formatada)
        return redirect(url_for('bookings.index_bookings_route'))
    
    # Obtenha todos os clientes para o dropdown
    clientes = get_all_clients()  # Supondo que você tenha essa função que retorna todos os clientes
    return render_template('bookings/add_booking.html', title='Adicionar Reserva | AirXpress', clientes=clientes)

def update_booking(booking_id):
    """
    Atualiza uma reserva do banco de dados.
    :param booking_id: ID da reserva a ser atualizada.
    :return: redireciona para a página de reservas.
    """
    if request.method == 'POST':
        new_fk_cliente = request.form['fk_cliente']
        new_fk_voo = request.form['fk_voo']
        new_data_str = request.form['data']
        
        new_data = datetime.strptime(new_data_str, "%Y-%m-%dT%H:%M").strftime("%d-%m-%Y %H:%M:%S")
        
        update_reserva(booking_id, new_fk_cliente, new_fk_voo, new_data)
        return redirect(url_for('bookings.index_bookings_route'))
    booking = get_reserva(booking_id)
    booking['data'] = datetime.strptime(booking['data'], '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M')
    return render_template('bookings/update_booking.html', booking=booking, title='Atualizar Reserva | AirXpress')

def delete_booking(booking_id):
    """
    Deleta uma reserva do banco de dados.
    :param booking_id: ID da reserva a ser deletada.
    :return: redireciona para a página de reservas.
    """
    delete_reserva(booking_id)
    return redirect(url_for('bookings.index_bookings_route'))
