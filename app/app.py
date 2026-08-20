import os
import time

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "devops"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devops123"),
        port=os.getenv("DB_PORT", "5432"),
        connect_timeout=3,
    )


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Challenge API",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/ready")
def ready():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "ready", "database": "connected"}), 200
    except Exception as e:
        return jsonify({
            "status": "not ready",
            "database": "unavailable",
            "error": str(e)
        }), 503


@app.route("/db")
def database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({
        "database": "connected",
        "time": str(result[0])
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)