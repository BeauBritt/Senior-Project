# Import required libraries for web framework, database, and security
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

# Initialize Flask application with CORS and password hashing
app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

# Load environment variables and setup MongoDB connection
load_dotenv()
mongo_url = os.environ.get("url")
client = MongoClient(mongo_url)
db = client["CBPacks"]
users = db["Users"]

# Register endpoint: Creates new user with hashed password
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if users.find_one({"username": username}):
        return jsonify({"error": "Username already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    users.insert_one({
        "username": username,
        "password": hashed_pw
    })

    return jsonify({"message": "User registered successfully"}), 201

# Login endpoint: Authenticates user credentials
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.find_one({"username": username})
    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful", "username": username}), 200


