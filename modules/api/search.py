# -*- encode: utf-8 -*-
from requests_oauthlib import OAuth1Session
from modules.base import BaseApi


class SearchApi(BaseApi):
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
