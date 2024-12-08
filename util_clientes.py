from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db/airxpress.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
def insert_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    
def insert_users(users):
    for user in users:
        insert_user(user[0], user[1])

def index_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('user.html', users=users)

def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        return redirect(url_for('index_clientes_route'))
    return render_template('add_user.html')

def update_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        new_name = request.form['name']
        new_email = request.form['email']
        cursor.execute('UPDATE users SET name = ?, email = ? WHERE pk_cliente = ?', (new_name, new_email, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index_clientes_route'))
    cursor.execute('SELECT * FROM users WHERE pk_cliente = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return render_template('update_user.html', user=user)

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE pk_cliente = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index_clientes_route'))
