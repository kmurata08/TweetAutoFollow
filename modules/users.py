# -*- encode: utf-8 -*-
from requests_oauthlib import OAuth1Session
from modules.base import BaseTweet


class UsersTweet(BaseTweet):
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
