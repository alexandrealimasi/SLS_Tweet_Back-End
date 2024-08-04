# etl.py
import json
from datetime import datetime
from app import create_app, db
from app.models import User, Tweet

def load_data():
    with open('tweets.json', 'r') as f:
        tweets = [json.loads(line) for line in f if is_valid_tweet(json.loads(line))]

    for tweet in tweets:
        user_data = tweet['user']
        user = User.query.get(user_data['id']) or User(
            user_id=user_data['id'],
            screen_name=user_data['screen_name'],
            description=user_data['description'],
            last_updated=datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        )
        db.session.merge(user)

        tweet_record = Tweet(
            tweet_id=tweet['id'],
            user_id=user_data['id'],
            text=tweet['text'],
            created_at=datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'),
            in_reply_to_user_id=tweet['in_reply_to_user_id'],
            retweeted_status=tweet.get('retweeted_status', {}),
            lang=tweet['lang'],
            hashtags=','.join([hashtag['text'] for hashtag in tweet['entities']['hashtags']])
        )
        db.session.add(tweet_record)

    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        load_data()
