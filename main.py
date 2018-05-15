from tweet import FriendShipsTweet

if __name__ == "__main__":
    users = FriendShipsTweet.lookup_api("1528352858,2905085521")
    print(users)
