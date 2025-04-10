from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
import random

from user_routes import user_bp  


app = Flask(__name__)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

load_dotenv()
mongo_url = os.environ.get("url")

client = MongoClient(mongo_url)
db = client["CBPacks"]
player_collection = db["Player Data"]


app.register_blueprint(user_bp)


@app.route("/", methods=["GET"])
def get_players():
    players = list(player_collection.find({}, {"_id": 0}))
    return jsonify(players)

@app.route("/random_players", methods=["GET"])
def get_random_players():
    players = list(player_collection.find({}, {"_id": 0}))
    random.shuffle(players)
    return jsonify(players[:5])


if __name__ == "__main__":
    app.run(debug=True)
