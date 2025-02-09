# database/db.py
from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["movie_bot"]
users_collection = db["users"]
movies_collection = db["movies"]

def add_user(user_id):
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id})

def add_movie(title, download_link):
    movies_collection.insert_one({"title": title, "download_link": download_link})

def search_movies(query):
    return movies_collection.find({"title": {"$regex": query, "$options": "i"}})
