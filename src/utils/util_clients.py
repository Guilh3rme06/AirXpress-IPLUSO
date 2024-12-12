import logging
from flask import render_template, request, redirect, url_for
from src.models.clients import *
    
def index_clientes():
    users = get_clientes()
    return render_template('user/user.html', users=users, title='Clientes | AirXpress')

def add_user():
    if request.method == 'POST':
        insert_cliente(request.form['nome'], request.form['email'])
        return redirect(url_for('clients.index_clientes_route'))
    return render_template('user/add_user.html', title='Adicionar Cliente | AirXpress')

def update_user(user_id):
    if request.method == 'POST':
        new_name = request.form['nome']
        new_email = request.form['email']
        update_cliente(new_name, new_email, user_id)
        return redirect(url_for('clients.index_clientes_route'))
    user = get_cliente(user_id)
    return render_template('user/update_user.html', user=user, title='Atualizar Cliente | AirXpress')

def delete_user(user_id):
    delete_cliente(user_id)
    return redirect(url_for('clients.index_clientes_route'))
