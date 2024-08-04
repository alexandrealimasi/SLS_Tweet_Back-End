# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/twitter_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
