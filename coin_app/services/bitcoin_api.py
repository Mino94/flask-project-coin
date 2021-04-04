import pandas as pd
import pybithumb
import time

# DB import
from coin_app.models.coin_info_model import Coin
from coin_app import db

def get_coin():
    coin_name = []
    opening_price = []
    closing_price = []
    min_price = []
    max_price = []

    prev_closing_price = []
    units_traded = []
    units_traded_24H = []
    acc_trade_value = []           
    acc_trade_value_24H = []    
    fluctate_24H = []          # 24시간 변동금액
    fluctate_rate_24H = []
# ******수정필요******
# 1초에 1번 가져오게 바꿔야한다.
    tickers = pybithumb.get_tickers()
    try:
        all = pybithumb.get_current_price("ALL")
        for ticker, data in all.items():
            coin_name.append(ticker)
            opening_price.append(data['opening_price'])
            closing_price.append(data['closing_price'])
            min_price.append(data['min_price'])
            max_price.append(data['max_price'])
            units_traded.append(data['units_traded'])
            # 변경
            acc_trade_value.append(data['acc_trade_value'])
            prev_closing_price.append(data['prev_closing_price'])
            units_traded_24H.append(data['units_traded_24H'])
            acc_trade_value_24H.append(data['acc_trade_value_24H'])
            
            fluctate_24H.append(data['fluctate_24H'])
            fluctate_rate_24H.append(data['fluctate_rate_24H'])

        data = {'name': coin_name, "opening_price": opening_price, "closing_price": closing_price,
                'min_price':min_price, 'max_price':max_price, 'prev_closing_price':prev_closing_price,
                'units_traded':units_traded,'units_traded_24H':units_traded_24H,'acc_trade_value':acc_trade_value,
                'acc_trade_value_24H':acc_trade_value_24H,'fluctate_24H':fluctate_24H,'fluctate_rate_24H':fluctate_rate_24H}
        return data
    except Exception as e:
        print("api error", e)
        return e