# -*- encode: utf-8 -*-
from requests_oauthlib import OAuth1Session
from modules.base import BaseApi


class FriendShipsApi(BaseTweet):
    """
    フォロー関係のツイートクラス
    """

    @classmethod
    def create_api(cls, user_id):
        """
        friendships/create
        フォローする
        """
        url = "https://api.twitter.com/1.1/friendships/create.json"
        return cls.post_request(url, {"user_id": user_id})

    @classmethod
    def lookup_api(cls, user_ids):
        """
        friendships/lookup
        複数ユーザと自分との関係を調べる
        """
        url = "https://api.twitter.com/1.1/friendships/lookup.json"
        return cls.get_request(url, {"user_id": user_ids})
