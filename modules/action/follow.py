# -*- encode: utf-8 -*-
from modules.api.api import FriendShips, Search, Users


class FollowAction():
    """
    フォロー関係のアクション
    """

    @classmethod
    def follow_from_prof_search(cls, keyword):
        """
        ユーザプロフィールをキーワード検索して、対象のユーザをフォロー
        """
        uid_list = []
        for i in range(4):
            # 1回に取れるのは20人
            users_dict = Users.search_api(keyword)
            _uid_list = [str(user["id"]) for user in users_dict]
            uid_list.extend(_uid_list)

        cls._follow_by_uid_list(uid_list)


    @classmethod
    def follow_from_tweet_search(cls, keyword):
        """
        ツイートをキーワード検索して、対象のユーザをフォロー
        """
        uid_list = []
        for i in range(1):
            # 1回に取れるのは100ツイート
            tweets_dict = Search.tweets_api(keyword)["statuses"]
            _uid_list = [str(tweet["user"]["id"]) for tweet in tweets_dict]
            uid_list.extend(_uid_list)

        cls._follow_by_uid_list(uid_list)


    @classmethod
    def _follow_by_uid_list(cls, uid_list):
        """
        ユーザIDのリストから、フォローしていないユーザをフォローする
        """
        # カンマで区切ったuidリストの文字列を取得
        uid_list_str = ",".join(uid_list)

        # 関係性を見る
        follow_uid_list = []
        friend_lookup_dict = FriendShips.lookup_api(uid_list_str)
        for friend in friend_lookup_dict:
            is_following = False
            for connection in friend["connections"]:
                if connection == "following":
                    is_following = True

            # フォロー
            if not is_following:
                result = FriendShips.create_api(friend["id"])
                if result:
                    follow_uid_list.append(friend["id"])

            # 一定人数以上フォローしていたらループを抜ける
            if len(follow_uid_list) >= 10:
                break

        [print(uid) for uid in follow_uid_list]
        return follow_uid_list
