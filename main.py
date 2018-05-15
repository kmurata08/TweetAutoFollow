from modules.friend_ships import FriendShipsTweet
from modules.users import UsersTweet

if __name__ == "__main__":
    users = FriendShipsTweet.lookup_api("1528352858,2905085521")
    print(users)

    users = UsersTweet.search_api("相互フォロー")
    [print(user["name"]) for user in users]
    print("===========")
    users = UsersTweet.search_api("相互フォロー")
    [print(user["name"]) for user in users]
