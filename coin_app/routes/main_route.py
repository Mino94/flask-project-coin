from flask import Blueprint, request, redirect, url_for, render_template
from coin_app.models.coin_info_model import Coin
from coin_app.models.user_coin_model import UserCoin
from coin_app.models.user_model import User
from coin_app.models.tweet_model import Tweet
from coin_app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/coin')
def coin_list():
    coin_list = Coin.query.all()
    return render_template('coinlist.html', coin_list=coin_list)

@main_bp.route('/regiscoin')
def register_coin_list():

    register_coin = db.session.query(UserCoin.id, Coin.name, Coin.closing_price, Coin.fluctate_rate_24H).\
                    outerjoin(User, UserCoin.user_id == User.id).\
                    outerjoin(Coin, UserCoin.coin_id == Coin.id).\
                    all()
    print(register_coin)
    for coin in register_coin:
        print(coin)
    return render_template('registerlist.html', register_coin=register_coin)

@main_bp.route('/tweet')
def tweet_list():
    tweet_list = Tweet.query.all()
    return render_template('tweet_list.html', tweet_list=tweet_list)
    