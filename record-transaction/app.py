from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from datetime import datetime

app = Flask(__name__)

# PostgreSQL database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="transaction_db",
        user="user1",
        password="password1",
        port="5433"
    )
    return conn

@app.route('/')
def index():
    return render_template('transaction_form.html')

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    date = request.form['date']
    amount = request.form['amount']
    transaction_type = request.form['transaction_type']
    description = request.form['description']
    category = request.form['category']

    conn = get_db_connection()
    cur = conn.cursor()

    # Store the transaction details in the database
    cur.execute("""
        INSERT INTO transactions (date, amount, transaction_type, description, category)
        VALUES (%s, %s, %s, %s, %s)
    """, (date, amount, transaction_type, description, category))
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
