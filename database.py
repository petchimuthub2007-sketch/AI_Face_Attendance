import os
import mysql.connector

def get_connection():
    print("DB_HOST =", os.getenv("DB_HOST"))
    print("DB_PORT =", os.getenv("DB_PORT"))
    print("DB_NAME =", os.getenv("DB_NAME"))
    print("DB_USER =", os.getenv("DB_USER"))

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Database Connected Successfully!")
        conn.close()
    except Exception as e:
        print("❌ Connection Failed")
        print(e)