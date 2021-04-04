from flask import Blueprint, request, redirect, url_for, render_template
from coin_app.services import tweepy_api, embedding_api
from coin_app.models.coin_info_model import Coin
from coin_app.models.tweet_model import Tweet
from coin_app import db

tweet_bp = Blueprint('tweet', __name__, url_prefix='/get')

@tweet_bp.route('/tweet/')
@tweet_bp.route('/tweet/<coin_name>')
def add_coin(coin_name=None):
    try:
        # tweet text check
        tweets_text = tweepy_api.get_tweets(coin_name)
        coin_id = Coin.query.filter_by(name=coin_name).first().id
        for tweet in tweets_text:
            text_list = [tweet.text]
            embedding = embedding_api.get_embeddings(text_list)
            new_tweet = Tweet(text=text_list[0], embedding=embedding, coin_id=coin_id)
            db.session.add(new_tweet)
            db.session.commit()
        print("add tweet text")
    except Exception as e:
        print(e)
    return redirect(url_for('main.tweet_list'))
