import os
import time
import mysql.connector


DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )


def init_db():
    for i in range(10):
        try:
            conn = get_connection()
            print("Connected to MySQL")
            break
        except Exception as e:
            print(f"MySQL not ready yet, retrying... ({i+1}/10) -> {e}")
            time.sleep(3)
    else:
        print("Could not connect to MySQL")
        return

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS demo_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            value INT
        )
        """
    )
    conn.commit()
    print("Table demo_table is ready")

    cursor.execute("INSERT INTO demo_table (name, value) VALUES (%s, %s)", ("Alice", 10))
    cursor.execute("INSERT INTO demo_table (name, value) VALUES (%s, %s)", ("Bob", 20))
    conn.commit()
    print("Inserted sample rows")

    cursor.execute("SELECT id, name, value FROM demo_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    init_db()
