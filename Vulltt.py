
import sqlite3
import os
import pickle
import subprocess
from flask import Flask, request

app = Flask(__name__)

# 1. Hardcoded credentials
SECRET_KEY = "admin123456"
DATABASE_PASSWORD = "root_password"

# 2. SQL Injection
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    result = conn.execute(query).fetchall()
    return str(result)

# 3. Command Injection
@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.check_output(
        "ping -c 1 " + host,
        shell=True
    )
    return result.decode()

# 4. Path Traversal
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open("uploads/" + filename, "r") as f:
        return f.read()

# 5. Insecure Deserialization
@app.route("/load")
def load_data():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)

# 6. Debug Information Exposure
@app.route("/debug")
def debug():
    return {
        "secret": SECRET_KEY,
        "database_password": DATABASE_PASSWORD
    }

if __name__ == "__main__":
    app.run(debug=True)
