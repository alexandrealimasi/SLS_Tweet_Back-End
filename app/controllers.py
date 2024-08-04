# app/controllers.py
from flask import request, jsonify
from .models import User, Tweet
from . import db
from sqlalchemy.exc import SQLAlchemyError
import csv
import io

def query_tweets():
    user_id = request.args.get('user_id')
    phrase = request.args.get('phrase')
    hashtag = request.args.get('hashtag')

    # Input validation
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    if not phrase and not hashtag:
        return jsonify({"error": "At least one of phrase or hashtag is required"}), 400

    try:
        # Query tweets
        query = Tweet.query.filter_by(user_id=user_id)
        if phrase:
            query = query.filter(Tweet.text.contains(phrase))
        if hashtag:
            query = query.filter(Tweet.hashtags.contains(hashtag))
        
        tweet = query.order_by(Tweet.created_at.desc()).first()

        # Prepare CSV response
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["TEAMID", "TEAM_AWS_ACCOUNT_ID"])
        
        if tweet:
            writer.writerow([tweet.user_id, tweet.user.screen_name, tweet.user.description, tweet.text])
        
        response = output.getvalue().strip()
        output.close()

        return response

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

