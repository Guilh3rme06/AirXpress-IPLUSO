from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('airxpress.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE
    )
''')
conn.commit()

@app.route('/')
def index():
    # Retrieve all users
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        new_name = request.form['name']
        new_email = request.form['email']
        cursor.execute('''UPDATE users SET name = ?, email = ? WHERE client = ?''', (new_name, new_email, user_id))
        conn.commit()
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM users WHERE client = ?', (user_id,))
    user = cursor.fetchone()
    return render_template('update_user.html', user=user)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE client = ?', (user_id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)