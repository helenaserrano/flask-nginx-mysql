from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

connection = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "db"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", "example"),
    database=os.environ.get("DB_NAME", "test_db"),
)

@app.route("/")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT message FROM greetings")
    rows = cursor.fetchall()
    cursor.close()
    return jsonify([row[0] for row in rows])

def init_db():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS greetings (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255));")
    cursor.execute("INSERT INTO greetings (message) VALUES ('Hola mundo');")
    connection.commit()
    cursor.close()

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
