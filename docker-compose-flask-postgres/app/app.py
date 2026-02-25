from flask import Flask
import psycopg2
import os
import time

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/")
def index():
    # Retry logic (wait for DB to be ready)
    for i in range(5):
        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100)
                );
            """)

            cur.execute("""
                INSERT INTO users (name)
                SELECT 'Sample User'
                WHERE NOT EXISTS (SELECT 1 FROM users);
            """)

            conn.commit()

            cur.execute("SELECT * FROM users;")
            rows = cur.fetchall()

            cur.close()
            conn.close()

            return f"<h1>Users</h1><p>{rows}</p>"

        except Exception as e:
            print("Waiting for database...", e)
            time.sleep(2)

    return "Database connection failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
