from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2

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

# Route for the transaction form with category dropdown
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch all categories from the database
    cur.execute("SELECT name FROM categories")
    categories = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('transaction_form.html', categories=categories)

# Add transaction to the database
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

# Fetch transactions
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

# Route for category form
@app.route('/categories', methods=['GET'])
def categories():
    return render_template('category_form.html')

# Add new category
@app.route('/api/categories', methods=['POST'])
def add_category():
    category_name = request.form['name']

    conn = get_db_connection()
    cur = conn.cursor()

    # Insert the new category into the database
    cur.execute("INSERT INTO categories (name) VALUES (%s) RETURNING id;", (category_name,))
    new_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('categories'))

# Fetch categories as JSON
@app.route('/api/categories', methods=['GET'])
def get_all_categories():
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch all categories
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(categories)

# Delete a category by ID
@app.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # Delete the category from the database
    cur.execute("DELETE FROM categories WHERE id = %s", (category_id,))
    conn.commit()

    cur.close()
    conn.close()

    return '', 204  # Return 'No Content' status after deletion

if __name__ == '__main__':
    app.run(debug=True, port=5001)
