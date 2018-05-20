from modules.friend_ships import FriendShipsApi
from modules.users import UsersApi

if __name__ == "__main__":
    # 80人分のuidを取得
    uid_list = []
    for i in range(4):
        # 1回に取れるのは20人
        users_dict = UsersTweet.search_api("相互フォロー")
        _uid_list = [str(user["id"]) for user in users_dict]
        uid_list.extend(_uid_list)

    # カンマで区切ったuidリストの文字列を取得
    uid_list_str = ",".join(uid_list)

    # 関係性を見る
    follow_uid_list = []
    friend_lookup_dict = FriendShipsTweet.lookup_api(uid_list_str)
    for friend in friend_lookup_dict:
        is_following = False
        for connection in friend["connections"]:
            if connection == "following":
                is_following = True

        # フォロー
        if not is_following:
            result = FriendShipsTweet.create_api(friend["id"])
            if result:
                follow_uid_list.append(friend["id"])

        # 一定人数以上フォローしていたらループを抜ける
        if len(follow_uid_list) >= 10:
            break

    [print(uid) for uid in follow_uid_list]
