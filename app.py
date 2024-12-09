from flask import Flask, render_template
from src.utils.util_clients import *

app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/clientes')
def index_clientes_route():
    return index_clientes()

@app.route('/add_user', methods=['GET', 'POST'])
def add_user_route():
    return add_user()

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user_route(user_id):
    return update_user(user_id)

@app.route('/delete_user/<int:user_id>')
def delete_user_route(user_id):
    return delete_user(user_id)

if __name__ == '__main__':
    app.run(debug=True)