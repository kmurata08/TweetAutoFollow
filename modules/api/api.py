# -*- encode: utf-8 -*-
from requests_oauthlib import OAuth1Session
from modules.api.base import BaseApi


class FriendShips(BaseApi):
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


class Search(BaseApi):
    """
    検索関係のツイートクラス
    """
    paging_tweet_id = 0

    @classmethod
    def tweets_api(cls, keyword):
        """
        users/search
        ユーザ検索
        """
        url = "https://api.twitter.com/1.1/search/tweets.json"

        params = {"q": keyword, "count": 10, "result_type": "recent"}
        if cls.paging_tweet_id > 0:
            # 一回検索している時には、最後のツイートのIDをページングに使用
            params["max_id"] = cls.paging_tweet_id

        result = cls.get_request(url, params)
        paging_tweet_id = result["statuses"][len(result["statuses"]) - 1]["id"] # ページング用ID更新

        return result


class Users(BaseApi):
    """
    フォロー関係のツイートクラス
    """
    pages = {}

    @classmethod
    def search_api(cls, keyword):
        """
        users/search
        ユーザ検索
        """
        url = "https://api.twitter.com/1.1/users/search.json"
        if keyword in cls.pages:
            # 同じキーワードで読み込む時には検索ページを加算
            page = cls.pages[keyword] + 1
        else:
            page = 1

        cls.pages[keyword] = page
        return cls.get_request(url, {"q": keyword, "page": page, "count": 20})
