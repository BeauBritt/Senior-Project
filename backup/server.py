# Import required libraries for web framework, database, and environment configuration
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
import random

# Import user routes blueprint
from user_routes import user_bp  

# Initialize Flask application with CORS and password hashing
app = Flask(__name__)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

# Load environment variables and setup MongoDB connection
load_dotenv()
mongo_url = os.environ.get("url")
client = MongoClient(mongo_url)
db = client["CBPacks"]
player_collection = db["Player Data"]

# Register user routes blueprint
app.register_blueprint(user_bp)

# Base route: Returns all players from database
@app.route("/", methods=["GET"])
def get_players():
    players = list(player_collection.find({}, {"_id": 0}))
    return jsonify(players)

# Random players endpoint: Returns 5 random players
@app.route("/random_players", methods=["GET"])
def get_random_players():
    players = list(player_collection.find({}, {"_id": 0}))
    random.shuffle(players)
    return jsonify(players[:5])

# Start server on specified port (default: 5000)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

