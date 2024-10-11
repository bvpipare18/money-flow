from flask import Flask, render_template, request, redirect, url_for, jsonify
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

@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch all transactions from the database
    cur.execute("SELECT * FROM transactions ORDER BY date DESC")
    transactions = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('transactions_list.html', transactions=transactions)

@app.route('/categories', methods=['GET'])
def categories():
    return render_template('category_form.html')

@app.route('/api/categories', methods=['POST'])
def add_category():
    category_name = request.form['name']

    conn = get_db_connection()
    cur = conn.cursor()
    print(category_name)

    # Insert the new category into the database
    cur.execute("INSERT INTO categories (name) VALUES (%s) RETURNING id;", (category_name,))
    new_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('categories'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
