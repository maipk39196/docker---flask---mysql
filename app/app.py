from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# Function to connect to MySQL
def ConnectorMysql():
    host = os.environ.get('DATABASE_HOST')
    user = os.environ.get('DATABASE_USER')
    password = os.environ.get('DATABASE_PASSWORD')
    database = os.environ.get('DATABASE_NAME')
    if not all([host, user, password, database]):
        raise ValueError(
            "One or more required environment variables are missing",
            f"DATABASE_HOST: {host}",
            f"DATABASE_USER: {user}",
            f"DATABASE_PASSWORD: {password}",
            f"DATABASE_NAME: {database}")

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin='mysql_native_password'
    )
    return mydb

# Database operations
def get_all_users():
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return result

def get_user(uid):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "SELECT * FROM users WHERE uid = %s"
    cursor.execute(query, (uid,))
    result = cursor.fetchone()
    return result

def create_user(name, age):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    mydb.commit()
    return "User created successfully!"

def update_user(uid, name, age):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "UPDATE users SET name = %s, age = %s WHERE uid = %s"
    cursor.execute(query, (name, age, uid))
    mydb.commit()
    return "User updated successfully!"

def delete_user(uid):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "DELETE FROM users WHERE uid = %s"
    cursor.execute(query, (uid,))
    mydb.commit()
    return "User deleted successfully!"

# Flask routes
@app.route('/')
def index():
    return "Index!"

@app.route('/user', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@app.route('/user/<int:uid>', methods=['GET'])
def get_user_by_id(uid):
    user = get_user(uid)
    return jsonify(user)

@app.route('/user/new', methods=['POST'])
def create_new_user():
    req = request.get_json()
    name = req['name']
    age = req['age']
    
    result = create_user(name, age)
    return jsonify(result)

@app.route('/user/<int:uid>', methods=['PUT'])
def update_user_by_id(uid):
    req = request.get_json()
    name = req['name']
    age = req['age']
    
    result = update_user(uid, name, age)
    return jsonify(result)

@app.route('/user/<int:uid>', methods=['DELETE'])
def delete_user_by_id(uid):
    result = delete_user(uid)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
