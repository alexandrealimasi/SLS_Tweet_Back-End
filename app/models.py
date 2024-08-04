# app/models.py
from . import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(255))
    description = db.Column(db.Text)
    last_updated = db.Column(db.DateTime)

class Tweet(db.Model):
    __tablename__ = 'tweets'
    tweet_id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.user_id'))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    in_reply_to_user_id = db.Column(db.BigInteger)
    retweeted_status = db.Column(db.JSON)
    lang = db.Column(db.String(10))
    hashtags = db.Column(db.Text)
