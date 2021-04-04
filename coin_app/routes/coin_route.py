from flask import Blueprint, request, redirect, url_for, render_template, Response
from coin_app.models.coin_info_model import Coin
from coin_app.models.user_coin_model import UserCoin
from coin_app.models.user_model import User
from coin_app.models.tweet_model import Tweet
from coin_app.services.bitcoin_api import get_coin
from coin_app import db

coin_bp = Blueprint('coin', __name__, url_prefix='/api')

@coin_bp.route('/coin', methods=['POST'])
def add_coin():
    data = get_coin()
    try:
        db_coin = Coin.query.filter(Coin.name==data.get('name')[0]).first()
        print("*******coin route start*********")
        if not db_coin:
            for i in range(0, len(data.get('name'))-1):
                new_coin = Coin(name=data.get('name')[i], opening_price=data.get('opening_price')[i], closing_price=data.get('closing_price')[i]
                                ,min_price=data.get('min_price')[i], max_price=data.get('max_price')[i], acc_trade_value=data.get('acc_trade_value')[i]
                                ,units_traded=data.get('units_traded')[i], prev_closing_price=data.get('prev_closing_price')[i], units_traded_24H=data.get('units_traded_24H')[i]
                                ,acc_trade_value_24H=data.get('acc_trade_value_24H')[i], fluctate_24H=data.get('fluctate_24H')[i], fluctate_rate_24H=data.get('fluctate_rate_24H')[i])
                print(new_coin)
                db.session.add(new_coin)
                db.session.commit()
            print("add Success")
        else:
            new_data = get_coin()
            for i in range(0, len(new_data.get('name'))-1):
                db_coin = Coin.query.filter(Coin.name==new_data.get('name')[i]).first()
                db_coin.opening_price = new_data.get('opening_price')[i]
                db_coin.closing_price = new_data.get('closing_price')[i]
                db_coin.min_price = new_data.get('min_price')[i]
                
                db_coin.max_price = new_data.get('max_price')[i]
                db_coin.acc_trade_value = new_data.get('acc_trade_value')[i]
                db_coin.units_traded = new_data.get('units_traded')[i]
                db_coin.prev_closing_price = new_data.get('prev_closing_price')[i]

                db_coin.units_traded_24H = new_data.get('units_traded_24H')[i]
                db_coin.acc_trade_value_24H = new_data.get('acc_trade_value_24H')[i]
                db_coin.fluctate_24H = new_data.get('fluctate_24H')[i]
                db_coin.fluctate_rate_24H = new_data.get('fluctate_rate_24H')[i]
                
                db.session.add(db_coin)
                db.session.commit()
            print("update Success")
        return redirect(url_for('main.coin_list'))
    except Exception as e:
        print("coin route error : ",e)
        return f"coin route error : {e}"
        
@coin_bp.route('/coin/')
@coin_bp.route('/coin/<coin_id>')
def coin_detail_info(coin_id=None):
    if coin_id==None:
      return Response(status=400)

    # DB check
    coin_info = Coin.query.filter(Coin.id==coin_id).first()
    if not coin_info:
      return Response(status=404)

    return render_template("coinInfo.html", coin_info=coin_info)

    
@coin_bp.route('/goodcoin', methods=["POST"])
def coin_register():
    register_coin_list = request.form.getlist('numcoin')

    if not register_coin_list:
        return Response(status=400)
    
    try:
        for coinNo in register_coin_list:
            newusercoin = UserCoin(user_id=1, coin_id=coinNo)
            db.session.add(newusercoin)
            db.session.commit()
        return redirect(url_for('main.register_coin_list'))
    except Exception() as e:
        print("coin route error : ",e)
        return f"coin route error : {e}"

@coin_bp.route('/regiscoin/')
@coin_bp.route('/regiscoin/<coin_id>')
def delete_user_coin(coin_id=None):
    if coin_id==None:
      return Response(status=400)
    
    del_id = UserCoin.query.filter(UserCoin.id==coin_id).first()
    db.session.delete(del_id)
    db.session.commit()

    return redirect(url_for('main.register_coin_list'))

