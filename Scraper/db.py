import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
mongo_url = os.environ.get("url")


client = MongoClient(mongo_url)
db = client["CBPacks"]
collection = db["Player Data"]


df = pd.read_csv("graded_ncaa_player_stats.csv")


data = df.to_dict(orient="records")


if data:  # Make sure it's not empty
    collection.insert_many(data)
    print("Data successfully imported to MongoDB!")
else:
    print("CSV file is empty or not loaded properly.")


