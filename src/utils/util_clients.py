import logging
from flask import render_template, request, redirect, url_for
from db.database import execute_query, fetch_query
    
def insert_user(name, email):
    execute_query('INSERT INTO clientes (nome, email) VALUES (?, ?)', (name, email))
    logging.info("Usuário inserido com sucesso!")
    
def insert_users(users):
    for user in users:
        insert_user(user[0], user[1])

def index_clientes():
    users = fetch_query('SELECT * FROM clientes')
    return render_template('user/user.html', users=users)

def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        execute_query('INSERT INTO clientes (nome, email) VALUES (?, ?)', (name, email))
        return redirect(url_for('clients.index_clientes_route'))
    return render_template('user/add_user.html')

def update_user(user_id):
    if request.method == 'POST':
        new_name = request.form['nome']
        new_email = request.form['email']
        execute_query('UPDATE clientes SET nome = ?, email = ? WHERE pk_cliente = ?', (new_name, new_email, user_id))
        return redirect(url_for('clients.index_clientes_route'))
    user = fetch_query('SELECT * FROM clientes WHERE pk_cliente = ?', (user_id,), fetch_one=True)
    return render_template('user/update_user.html', user=user)

def delete_user(user_id):
    execute_query('DELETE FROM clientes WHERE pk_cliente = ?', (user_id,))
    return redirect(url_for('clients.index_clientes_route'))
