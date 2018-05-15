# -*- encode: utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session


class BaseTweet:
    """
    ツイートを行うクラスの基底クラス
    """
    twitter = None

    @classmethod
    def oauth(cls):
        """
        認証処理
        """
        if cls.twitter is None:
            CK = config.CONSUMER_KEY
            CS = config.CONSUMER_SECRET
            AT = config.ACCESS_TOKEN
            ATS = config.ACCESS_TOKEN_SECRET
            cls.twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理
        else:
            pass

    @classmethod
    def get_request(cls, url, params):
        """
        TwitterAPIでGETリクエスト
        """
        cls.oauth()
        result = cls.twitter.get(url, params=params)
        if result.status_code == 200:
            data = json.loads(result.text)
            print("Request Success [%s]" % url)
            return data
        else:
            print("Request Failed: %d" % res.status_code)
            return False

    def post_request(cls, url, params):
        """
        TwitterAPIでPOSTリクエスト
        """
        cls.oauth()
        result = cls.twitter.post(url, params=params)
        if result.status_code == 200:
            print("Request Success [%s]" % url)
            return True
        else:
            print("Request Failed: %d" % res.status_code)
            return False
