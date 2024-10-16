
1. Run the PostgreSQL Docker container:
   ```bash
   docker run --name transaction-container -p 5433:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres:9.5
   ```

2. Access the PostgreSQL prompt inside the container:
   ```bash
   docker exec -it transaction-container psql -U postgres
   ```

3. Create a new database:
   ```sql
   CREATE DATABASE transaction_db;
   ```

4. Create a new user:
   ```sql
   CREATE USER user1 WITH PASSWORD 'password1';
   ```

5. Grant all privileges on the database to the user:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE transaction_db TO user1;
   ```

6. Create a table for transactions:
   ```sql
   CREATE TABLE transactions (
       id SERIAL PRIMARY KEY,
       date DATE NOT NULL,
       amount DECIMAL(10, 2) NOT NULL,
       transaction_type VARCHAR(50) NOT NULL,
       description VARCHAR(255),
       category VARCHAR(50) NOT NULL
   );
   ```

7. Grant privileges on the transactions table to the user:
   ```sql
   GRANT ALL PRIVILEGES ON TABLE transactions TO user1;
   ```

8. Grant usage and select privileges on the sequence to the user:
   ```sql
   GRANT USAGE, SELECT ON SEQUENCE transactions_id_seq TO user1;
   ```

9. Check the created table (optional):
   ```sql
   SELECT * FROM transactions;
   ```

10. Create a table for categories:
   ```sql
   CREATE TABLE categories (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50) NOT NULL UNIQUE
   );
   ```

11. Grant privileges on the categories table to the user:
   ```sql
   GRANT ALL PRIVILEGES ON TABLE categories TO user1;
   ```

12. Grant usage and select privileges on the sequence to the user:
   ```sql
   GRANT USAGE, SELECT ON SEQUENCE categories_id_seq TO user1;
   ```

13. Create a table for transaction types:
   ```sql
   CREATE TABLE transaction_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
   );
   ```

11. Grant privileges on the transaction_types table to the user:
   ```sql
   GRANT ALL PRIVILEGES ON TABLE transaction_types TO user1;
   ```

12. Grant usage and select privileges on the sequence to the user:
   ```sql
   GRANT USAGE, SELECT ON SEQUENCE transaction_types_id_seq TO user1;
   ```

