import logging
from flask import render_template, request, redirect, url_for
from db.database import execute_query, fetch_query
from datetime import datetime


def insert_booking(fk_cliente, fk_voo,data):
    data_formatada = datetime.strptime(data, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d %H:%M:%S")
    execute_query('INSERT INTO reservas (fk_cliente, fk_voo) VALUES (?, ?)', (fk_cliente, fk_voo,data_formatada))
    logging.info("Reserva inserido com sucesso!")

def insert_bookings(bookings):
    for booking in bookings:
        insert_booking(booking[0], booking[1], booking[2])

def index_reservas():
    bookings = fetch_query('SELECT * FROM reservas')
    return render_template('booking/booking.html', bookings=bookings)


def add_booking():
    if request.method == 'POST':
        fk_cliente = request.form['fk_cliente']
        fk_voo = request.form['fk_voo']
        data = request.form['data']
        # Converter para o formato "YYYY-MM-DD HH:MM:SS"
        data_formatada = datetime.strptime(data, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d %H:%M:%S")
        execute_query('INSERT INTO reservas (fk_cliente, fk_voo, data) VALUES (?, ?, ?)', (fk_cliente, fk_voo, data_formatada))
        return redirect(url_for('index_reservas_route'))
    return render_template('booking/add_booking.html')



def update_booking(booking_id):
    if request.method == 'POST':
        new_fk_cliente = request.form['fk_cliente']
        new_fk_voo = request.form['fk_voo']
        execute_query('UPDATE reservas SET fk_cliente = ?, fk_voo = ? WHERE pk_reserva = ?', (new_fk_cliente, new_fk_voo, booking_id))
        return redirect(url_for('index_reservas_route'))
    booking = fetch_query('SELECT * FROM reservas WHERE pk_reserva = ?', (booking_id,), fetch_one=True)
    return render_template('booking/update_booking.html', booking=booking)


def delete_booking(booking_id):
    execute_query('DELETE FROM reservas WHERE pk_reserva = ?', (booking_id,))
    return redirect(url_for('index_reservas_route'))
