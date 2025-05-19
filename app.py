from flask import Flask, request
import tweepy
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


app = Flask(__name__)

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

@app.route("/", methods=["POST"])
def tweet():
    data = request.get_json()
    message = data.get("tweet")
    if message:
        api.update_status(message)
        return {"status": "Tweet posted"}, 200
    return {"error": "No tweet found"}, 400

@app.route("/", methods=["GET"])
def ping():
    return "MMRC bot is running!", 200

