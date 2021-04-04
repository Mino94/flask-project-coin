import pybithumb
import time

tickers = pybithumb.get_tickers()

# BTC 저가 70523000.0 고가 71557000.0 평균 거래 금액 : 69900000.0 거래량 : 71236000.0
# ETH 저가 2206000.0 고가 2340000.0 평균 거래 금액 : 2201000.0 거래량 : 2314000.0
# LTC 저가 231700.0 고가 244200.0 평균 거래 금액 : 229600.0 거래량 : 238800.0
# ETC 저가 16090.0 고가 17600.0 평균 거래 금액 : 15980.0 거래량 : 17190.0
# for ticker in tickers:
#     price = pybithumb.get_current_price(ticker)
#     detail = pybithumb.get_market_detail(ticker)
#     print(ticker, "저가",detail[0], "고가",detail[1],"평균 거래 금액 :", detail[2], "거래량 :", detail[3])
#     time.sleep(0.1)


# BTC {'opening_price': '70523000', 'closing_price': '71209000', 'min_price': '69900000', 'max_price': '71557000', 'units_traded': '3001.20077766', 'acc_trade_value': '213201927216.5841', 'prev_closing_price': '70508000', 'units_traded_24H': '5215.26175715', 'acc_trade_value_24H': '368605994457.2907', 'fluctate_24H': '922000', 'fluctate_rate_24H': '1.31'}
# ETH {'opening_price': '2206000', 'closing_price': '2316000', 'min_price': '2201000', 'max_price': '2340000', 'units_traded': '46053.12883408', 'acc_trade_value': '105947204250.6024', 'prev_closing_price': '2206000', 'units_traded_24H': '71107.01140081', 'acc_trade_value_24H': '160676934356.3665', 'fluctate_24H': '117000', 'fluctate_rate_24H': '5.32'}
# all = pybithumb.get_current_price("ALL")
# for k, v in all.items():
#     print(k, v)

# # 코인 현재가
# all = pybithumb.get_current_price("ALL")
# for ticker, data in all.items() :
#     print(ticker, data['closing_price'])

# 현재 조회한 날짜 보여주기
# import datetime
# orderbook = pybithumb.get_orderbook("BTC")
# ms = int(orderbook["timestamp"])

# dt = datetime.datetime.fromtimestamp(ms/1000)
# print(dt)


# all = pybithumb.get_current_price("ALL")

# for ticker, data in all.items() :
#     print(data)

import tweepy
import twitter
api_key = '1JsryuSNhvd56MK1vy0POZBXn'
api_secret = 'BtRXiYCKwUYivmWskST4mYrBlS2k9rjxCHwWhWPKvCqalwCiIg'

access_token = '1372342167067185152-D0cyuUeoIkezXSUitxBezn67L2QtrG'
access_secret = 'knsV4TzlI5Gg6BEEs32t7txAMMGBHv5OygONy9E8owESb'

import twitter
from collections import Counter

twitter_api = twitter.Api(consumer_key=api_key,
                          consumer_secret=api_secret, 
                          access_token_key=access_token, 
                          access_token_secret=access_secret)

import json

query = "BTC"
stream = twitter_api.GetUserTimeline(screen_name=query, count=50,include_rts=True, exclude_replies=False)
for status in stream:
    print(status.text)
# for tweets in stream:
#     tweet_str = json.dumps(tweets, ensure_ascii=False)
#     tweet_dict = json.loads(tweet_str)
#     print(tweet_dict)