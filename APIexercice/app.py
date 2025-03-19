from flask import Flask, request,jsonify
import sqlite3


app = Flask(__name__)

dummydb={ "admin": {"password": "password123"} }

def get_db():
    conn = sqlite3.connect("db.sqlite")
    conn.row_factory = sqlite3.Row  # Helps return rows as dictionaries
    return conn

class User():
   
    def __init__(self, name,age,email):
        self.name=name
        self.age=age
        self.email=email

    def createUser(self):
        db=get_db()
        cursor=db.cursor()
        cursor.execute("INSERT INTO User (name, age, email) VALUES (?, ?, ?)", (self.name, self.age, self.email))
        db.commit()

        

@app.route("/")
def hello_world():

    response = {"Name": "Landy"}
    return response,200

"""
POST /users → Create a new user
GET /users → Fetch all users
GET /users/<id> → Get a single user by ID
PUT /users/<id> → Update user details
DELETE /users/<id> → Remove a user
"""
@app.route("/users", methods=['GET'])
@;miter.limit(10 per minute)
def fetchAllUser():
        db=get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM User")
        users = cursor.fetchall()
        return jsonify(users), 200


@app.route("/users", methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    email = data.get("email")

    if not name or not age or not email:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()
        conn.close()
        return jsonify({"message": "Users created successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users/<id>", methods=['GET'])
def getUsersId(id):
    db=get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Users WHERE id = ?", (id,))
    result = cursor.fetchone()
    return jsonify(result) if result else (jsonify({"error": "User not found"}), 404)

@app.route("/users/<id>", methods=['PUT'])
def updateUserDetails(id):
    db=get_db()
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    email = data.get("email")

    cursor = db.cursor()
    cursor.execute("UPDATE Users SET name = ?, age = ?, email = ? WHERE id = ?", (name, age, email, id))
    db.commit()
    
    return jsonify({"message": "Successful"}), 200

@app.route("/users/<id>",methods=['DELETE'])
def deleteUserDetails(id):
    db=get_db()
    cursor=db.cursor()
    cursor.execute("DELETE FROM Users WHERE id = ?", (id,))
    db.commit()
    return {"message":"deleteSuccessfully"},201
    
@app.route("/login",methods=['POST'])
def login():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    if username in Auth and password == Auth.Password :
        access_token=create_token(identity=username)
        return jsonify("token": access_token)


@app.route("/dashboard",methods=['GET'])
@jwt_required
def welcome():
    username = get_jwt_identity()
    return jsonify({"message": f"Welcome, {username}!"})


