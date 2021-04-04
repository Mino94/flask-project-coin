import tweepy
import twitter
import json

api_key = '1JsryuSNhvd56MK1vy0POZBXn'
api_secret = 'BtRXiYCKwUYivmWskST4mYrBlS2k9rjxCHwWhWPKvCqalwCiIg'

access_token = '1372342167067185152-D0cyuUeoIkezXSUitxBezn67L2QtrG'
access_secret = 'knsV4TzlI5Gg6BEEs32t7txAMMGBHv5OygONy9E8owESb'

twitter_api = twitter.Api(consumer_key=api_key,
                          consumer_secret=api_secret, 
                          access_token_key=access_token, 
                          access_token_secret=access_secret)


def get_tweets(screen_name):
    raw_tweets = twitter_api.GetUserTimeline(screen_name=screen_name,
                                            count=50,
                                            include_rts=True,
                                            exclude_replies=False)
    # for status in stream:
    #     print(status.text)
    return raw_tweets