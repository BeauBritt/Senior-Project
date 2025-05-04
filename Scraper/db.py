# Import required libraries for environment variables, data processing, and database operations
import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables and get MongoDB connection URL
load_dotenv()
mongo_url = os.environ.get("url")

# Initialize MongoDB connection and select database/collection
client = MongoClient(mongo_url)
db = client["CBPacks"]
collection = db["Player Data"]

# Load graded player statistics from CSV file
df = pd.read_csv("graded_ncaa_player_stats.csv")

# Convert DataFrame to list of dictionaries for MongoDB insertion
data = df.to_dict(orient="records")

# Insert data into MongoDB if available
if data:  # Make sure it's not empty
    collection.insert_many(data)
    print("Data successfully imported to MongoDB!")
else:
    print("CSV file is empty or not loaded properly.")


